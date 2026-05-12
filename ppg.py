#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ppg.py
import json
import os
import ssl
import sys
import urllib.parse
import urllib.request

"""
useage: python ppg.py 'SOME STRING TO TRANSLATE'
test: pytest -s ppg.py

papago api
https://developers.naver.com/docs/papago/papago-nmt-overview.md
"""

# get client id and secret
def load_env(env_path=".env"):
    try:
        with open(os.path.join(os.path.dirname(__file__), env_path), "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value.strip('"').strip("'")
    except FileNotFoundError:
        pass

load_env()

CLIENT_ID = os.environ.get("ncloud_client_id")
CLIENT_SECRET = os.environ.get("ncloud_client_secret")
if not CLIENT_ID or not CLIENT_SECRET:
    CLIENT_ID = "[ERR] client_id/secret을 설정하세요."
    CLIENT_SECRET = "[ERR] client id/secret is not defined."

TIER = os.environ.get("tier", "tier0")

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
    "ko": [
        "en",
        "ja",
        "zh-CN",
        "zh-TW",
        "vi",
        "id",
        "th",
        "de",
        "ru",
        "es",
        "it",
        "fr",
    ],
    "en": ["ko", "ja", "fr", "zh-CN", "zh-TW"],
    "ja": ["ko", "en", "zh-CN", "zh-TW"],
    "zh-CN": ["ko", "en", "ja", "zh-TW"],
}  # fmt: on


def get_response(request_url, data):
    context = ssl._create_unverified_context()

    request = urllib.request.Request(request_url)
    request.add_header("x-ncp-apigw-api-key-id", CLIENT_ID)
    request.add_header("x-ncp-apigw-api-key", CLIENT_SECRET)
    try:
        response = urllib.request.urlopen(
            request, data=data.encode("utf-8"), context=context
        )
        rescode = response.getcode()
    except urllib.error.HTTPError as e:
        rescode = e.code
    except urllib.error.URLError as e:
        rescode = 500  # Treat other URL errors as 500

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
    request_url = "https://papago.apigw.ntruss.com/langs/v1/dect"
    return get_response(request_url, data=data)


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
    request_url = "https://papago.apigw.ntruss.com/nmt/v1/translation"
    data = f"source={langcode_pair[0]}&target={langcode_pair[1]}&text={encText}"
    return get_response(request_url, data=data)


def return_error(title, subtitle):
    return {
        "variables": {"status": False},
        "items": [
            {
                "title": title,
                "subtitle": subtitle,
                # "icon": {"path": "clipboard.png"},
                "arg": "error",
                "valid": False,
                # 'uid': 'outputString',
            }
        ],
    }


def main(inputString=None):
    """
    This is the main function that takes an input string from the command line argument,
    translates it using the get_translated_data function, and produces an output in JSON format.
    """
    # [ERROR] Client Not Set
    if "[ERR]" in CLIENT_ID:
        title = "[Error] client_id/secret가 잘 설정되었는지 확인해주세요."
        subtitle = "Plese check client_id/secret."
        return return_error(title, subtitle)

    # Language detection
    if TIER == "tier1":
        source_langcode = "en"
    elif TIER == "tier2":
        source_langcode = get_source_langcode(inputString)

        # [ERROR] client_id/secret not valid
        if isinstance(source_langcode, int):
            title = "[Error] client_id/secret가 잘 설정되었는지 확인해주세요."
            subtitle = "Plese check client_id/secret or Detection API."
            return return_error(title, subtitle)

        source_langcode = source_langcode["langCode"]

    # TODO: Add target_langcode option
    # target_langcode = get_target_langcode(something)
    target_langcode = (
        "en" if source_langcode == "ko" else "ko"
    )  # currently only supports Korean.

    # check if the language pair is supported. (True or False)
    langcode_pair = (source_langcode, target_langcode)
    is_supported = check_langpairs(langcode_pair)

    # ERROR if not supported
    if not is_supported:
        title = f"[{LANGCODES[source_langcode]}->{LANGCODES[target_langcode]}] Not Supported Language Pair."
        subtitle = "파파고에서 지원하지 않는 언어입니다.🥲"
        return return_error(title, subtitle)

    if is_supported:
        # Translate inputString
        output_json = get_translated_data(inputString, langcode_pair)
        if isinstance(output_json, int):
            title = f"[Error] Translation Failed (Code: {output_json})"
            subtitle = "Please check your API limit or credentials."
            return return_error(title, subtitle)
        translatedString = output_json["message"]["result"]["translatedText"]

    return {
        "variables": {
            "input": inputString,
            "result": translatedString,
            "status": True,
        },
        "items": [
            {
                "uid": "copy",
                "title": f"{translatedString}",
                "subtitle": "[Enter]를 누르면 결과를 클립보드로 복사합니다.",
                "icon": {"path": "clipboard.png"},
                # "action": "copy",
                "arg": translatedString,
                "valid": True,
            },
            # { # TODO
            #     "uid": "web",
            #     "title": "Open in the Web",
            #     "subtitle": "웹페이지에서 결과를 봅니다.",
            #     "icon": {"path": "globe.png"},
            #     # "action": "web",
            #     "arg": translatedString,
            #     "valid": True,
            # },
        ],
    }


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
        # print(json.dumps(out))
        # sys.stdout.flush()


def bypass_query(query):
    # return query

    return {
        "action": "Open URL",
        "variables": {
            "input": query,
            "result": query,
            "status": True,
        },
        "items": [
            {
                "uid": "web",
                "title": f"{query}",
                "subtitle": "[Enter]를 웹에서 결과를 봅니다.",
                "icon": {"path": "globe.png"},
                "arg": query,
                # "arg": f"https://papago.naver.com/?&st={query}",
                # "valid": True,
            },
        ],
    }


if __name__ == "__main__":
    """
    main function.
    python ppg.py 'SOME STRING TO TRANSLATE'
    """
    try:
        input_string = str(sys.argv[1])
    except IndexError:
        print(json.dumps(return_error("Input Required", "Please provide a string to translate.")))
        sys.exit(0)

    if TIER == "tier0":  # Free tier
        out = bypass_query(input_string)

    else:
        # if input_string == "debug":
        #     test_main()
        out = main(input_string)
    print(json.dumps(out))
    sys.stdout.flush()
