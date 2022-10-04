#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ppg.py

import sys
import json

import urllib.parse
import urllib.request
# import json

from client_id import client_id
from client_secret import client_secret
# 
assert client_id, "client_id를 설정하세요. ppconfig -> id"
assert client_secret, "client_secret를 설정하세요. ppconfig -> secret"

def find_language_code(word):
    """
    python3 tested
    """
    encQuery = urllib.parse.quote(word.encode('utf-8'))
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        dt = response_body.decode('utf-8')
    else:
        dt = "Error Code:" + rescode
    
    return json.loads(dt)

def get_translated_data(word):
    encText = urllib.parse.quote(word.encode('utf-8'))

    langCode = find_language_code(word)['langCode']
    if langCode == 'ko':
        data = "source=ko&target=en&text=" + encText
    else:
        data = "source=en&target=ko&text=" + encText

    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        dt = response_body.decode('utf-8')
    else:
        dt = "Error Code:" + rescode

    return json.loads(dt)
    

def main():   
    """
    output_json = {
        'message': {
            'result': {
                'srcLangType': 'en', 
                'tarLangType': 'ko', 
                'translatedText': '이것은 테스트 입력입니다.', 
                'engineType': 'N2MT', 
                'pivot': None, 
                'dict': None, 
                'tarDict': None
                }, 
            '@type': 'response', 
            '@service': 'naverservice.nmt.proxy', 
            '@version': '1.0.0'
        }
    }

    """
    inputString = sys.argv[1] 
    # Translate inputString
    
    output_json = get_translated_data(str(inputString))
    translatedString = output_json['message']['result']['translatedText']
    
    # Produce output
    result = {"items": []}
    
    outputLangCode = output_json['message']['result']['tarLangType']

    if translatedString:
        result["items"].append({
            "title": f"{translatedString}",
            'subtitle': "[Enter]를 누르면 결과를 클립보드로 복사합니다.",
            # 'valid': True,
            # 'uid': 'outputString',
            "icon": {
                "path": 'icon.png'
            },
            'arg': translatedString,
                }) 
    else:
        result["items"].append({
            "title": 'No Result',
            "subtitle":  "[Enter]를 누르면 웹에서 검색합니다.",
            "arg": inputString,
            "valid": True # True = Pass to next action.
        })

    print (json.dumps(result))
    sys.stdout.flush()


if __name__ == '__main__':
    main()