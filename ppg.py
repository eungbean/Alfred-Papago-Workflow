#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ppg.py
import sys
import json

import ssl
import urllib.parse
import urllib.request


"""
useage: python ppg.py 'SOME STRING TO TRANSLATE'
test: pytest -s ppg.py

papago api
https://developers.naver.com/docs/papago/papago-nmt-overview.md
"""

LANGCODES = {
    # Supported Language Codes
    "ko": "Korean",
    "en": "English",
    "ja": "Japanese",
    "zh-CN": "Chinese(Simplified)",
    "zh-TW": "Chinese(Traditional)",
    "vi": "Vietnamese",
    "id": "Indonesian",
    "th": "Thai",
    "de": "German",
    "ru": "Russian",
    "es": "Spanish",
    "it": "Italian",
    "fr": "French",
    # Unsupported Language Codes
    "hi": "hindi",
    "pt": "Portuguese",
    "fa": "Persian",
    "ar": "Arabic",
    "mm": "Burmese",
    "unk": "Unknown",
}


SUPPORTED_PAIRS = {  # fmt: off
    "ko": ["en", "ja", "zh-CN", "zh-TW", "vi", "id", "th", "de", "ru", "es", "it", "fr"],
    "en": ["ko", "ja", "fr", "zh-CN", "zh-TW"],
    "ja": ["ko", "en", "zh-CN", "zh-TW"],
    "zh-CN": ["ko", "en", "ja", "zh-TW"],
}  # fmt: on

# Load client_id, client_secret
try:
    from client_id import client_id
    from client_secret import client_secret
except ImportError:
    client_id = "[ERR] client_id/secret을 설정하세요. ppconfig -> id/secret"
    client_secret = "[ERR] ppconfig -> id/secret"


def get_response(appcode, data):
    context = ssl._create_unverified_context()

    request = urllib.request.Request(f"https://openapi.naver.com/v1/papago/{appcode}")
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(
            request, data=data.encode("utf-8"), context=context
        )
        rescode = response.getcode()
    except urllib.error.HTTPError as e:
        rescode = e.code

    # check response code
    # HTTP response code, (200 – 299): Successful responses
    if rescode == 200:
        return json.loads(response.read().decode("utf-8"))
    else:
        return rescode


def get_source_langcode(word: str) -> dict:
    """
    This function takes a word as input and returns a dictionary containing the detected language code.
    """
    encQuery = urllib.parse.quote(word)
    data = f"query={encQuery}"
    return get_response(appcode="detectLangs", data=data)


# TODO: add target_langcode option
# def get_target_langcode(target_langcode=None):
# target_langcode = "ko" if target_langcode is None else target_langcode
# return target_langcode


def check_langpairs(langcode_pair: tuple) -> bool:
    """
    Check if the language pair is supported.
    This function takes two language codes as input and returns a boolean value.
    """
    return langcode_pair[1] in SUPPORTED_PAIRS.get(
        langcode_pair[0], []
    ) or langcode_pair[0] in SUPPORTED_PAIRS.get(langcode_pair[1], [])


def get_translated_data(word: str, langcode_pair: tuple) -> dict:
    """
    This function takes a word as input and returns a dictionary containing the translated text.
    word: string
    langcode_pair: tuple(source_langcode, target_langcode)
    """
    encText = urllib.parse.quote(word)
    data = f"source={langcode_pair[0]}&target={langcode_pair[1]}&text={encText}"
    return get_response(appcode="n2mt", data=data)


def return_client_error(rescode):
    title = f"[{rescode}error] client_id/secret을 설정하세요."
    subtitle = "ppconfig -> id/secret"
    return make_alfred_output(title, subtitle, variables={'goto_setting': True})#, valid=False)


def make_alfred_output(title, subtitle, arg=None, variables={}, valid=True):
    return {
        "variables": variables,
        "items": [
            {
                "title": title,
                "subtitle": subtitle,
                "icon": {"path": "icon.png"},
                "arg": arg,
                "valid": valid,
                # 'uid': 'outputString',
            }
        ]
    }


def main(inputString=None):
    """
    This is the main function that takes an input string from the command line argument,
    translates it using the get_translated_data function, and produces an output in JSON format.
    """
    # if client information not exist.
    if "[ERR]" in client_id:
        return return_client_error()

    # Language detection
    source_langcode = get_source_langcode(inputString)

    # client_id/secret error
    if isinstance(source_langcode, int):
        return return_client_error(source_langcode)

    source_langcode = source_langcode["langCode"]

    # TODO: Add target_langcode option
    # target_langcode = get_target_langcode(something)
    target_langcode = (
        "en" if source_langcode == "ko" else "ko"
    )  # currently only supports Korean.

    # check if the language pair is supported. (True or False)
    langcode_pair = (source_langcode, target_langcode)
    is_supported = check_langpairs(langcode_pair)

    if not is_supported:
        title = f"[{LANGCODES[source_langcode]}->{LANGCODES[target_langcode]}] Not Supported Language Pair."
        subtitle = "파파고에서 지원하지 않는 언어입니다.🥲"
        arg = inputString

    if is_supported:
        # Translate inputString
        output_json = get_translated_data(inputString, langcode_pair)
        translatedString = output_json["message"]["result"]["translatedText"]

        # Produce output
        # langpair: Supported, Translation: Success
        if translatedString:
            title = f"{translatedString}"
            subtitle = "[Enter]를 누르면 결과를 클립보드로 복사합니다."
            arg = translatedString

        # langpair: Supported, Translation: Success
        else:
            title = "No Result"
            subtitle = "[Enter]를 누르면 웹에서 검색합니다."
            arg = inputString

    return make_alfred_output(title, subtitle, arg)


def test_main():
    """
    Test main function.
    pytest -s ppg.py
    """
    input_strings = [
        "영화 보기 전에 팝콘과 콜라를 살 것이다.",  # Korean
        "映画を見る前にポップコーンとコーラを買います。",  # Japanese
        "I will buy popcorn and cola before watching a movie.",  # English
        "我会在看电影之前买爆米花和可乐。",  # Chinese(Simplified)
        "我會在看電影之前買爆米花和可樂。",  # Chinese(Traditional)
        "Tôi sẽ mua bắp rang bơ và coca trước khi xem phim.",  # Vietnamese
        "Saya akan membeli popcorn dan cola sebelum menonton film.",  # Indonesian
        "ฉันจะซื้อป๊อปคอร์นและโค๊กก่อนดูหนัง",  # Thai
        "Ich werde vor dem Anschauen eines Films Popcorn und Cola kaufen.",  # German
        "Я куплю попкорн и колу перед просмотром фильма.",  # Russian
        "Compraré palomitas de maíz y cola antes de ver una película.",  # Spanish
        "Comprerò popcorn e cola prima di guardare un film.",  # Italian
        "Je vais acheter du pop-corn et du cola avant de regarder un film.",  # French
        "الْقِطِار أَسْرَعُ مِنَ السَّيَّارَةِ",  # Arabic, FAIL TEST with unsupported language.
    ]

    for input_string in input_strings:
        out = main(input_string)
        print(out)


if __name__ == "__main__":
    """
    main function.
    python ppg.py 'SOME STRING TO TRANSLATE'
    """
    input_string = str(sys.argv[1])
    out = main(input_string)
    print(json.dumps(out))
    sys.stdout.flush()
