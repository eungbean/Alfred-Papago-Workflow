#!/usr/bin/python
# encoding: utf-8

import sys
import os
from workflow import Workflow3, web
from six.moves import urllib
import json
from client_id import client_id
from client_secret import client_secret

reload(sys)
sys.setdefaultencoding("utf-8")

assert client_id, "client_id를 설정하세요. ppconfig -> id"
assert client_secret, "client_secret를 설정하세요. ppconfig -> secret"

def find_language_code(word):
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


def main(wf):
    
    args = wf.args[0]
    res_json = get_translated_data(args.encode('utf-8'))
    
    if res_json:

        wf.add_item(
            title = u'%s' % args,
            subtitle = u"Result : %s"% res_json['message']['result']['translatedText'],
            arg = u"%s"% res_json['message']['result']['translatedText'],
            valid = True, # True = Pass to next action.
        ) # add items

    else:
        wf.add_item(
            title = 'No Result',
            subtitle = 'Search in the web',
            arg = args,
            valid = True # True = Pass to next action.
        ) # when there's no result

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))
