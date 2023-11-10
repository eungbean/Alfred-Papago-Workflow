# Papago Translation Workflow for Alfred 5

![](https://img.shields.io/github/checks-status/eungbean/Alfred-Papago-Workflow/main)

<div align="center">

![overview](document/overview.gif)

쉽고 빠른 한/영, 영/한 번역이 필요해 직접 만들었습니다! <br><br>
🚀 빠르고 쉽게 번역을 하고 (<kbd>pp</kbd>) 결과를 복사합니다. (<kbd>Enter</kbd>)<br>
🛸 긴 문장 번역이 필요할 때, 웹사이트에서 결과를 볼 수도 있습니다. <br>
🌎 다양한 언어를 지원합니다. `🇰🇷 ↔️ 🇺🇸 🇯🇵 🇨🇳 🇻🇳 🇮🇩 🇹🇭 🇩🇪 🇪🇸 🇮🇹 🇫🇷`<br>

**[[DOWNLOAD]](https://github.com/eungbean/Alfred-Papago-Workflow/releases)**
**[[BLOG]](https://eungbean.io/dev/papago-alfred)**

_최신 Alfred 5를 지원합니다._

</div>

## ⚡ Quickstart

### 1. 즉시 번역 및 복사하기 <kbd>pp</kbd>

![result-copy](document/result-copy.png)

```
pp {문장}
```

- 문장을 즉시 한/영, 영/한 번역합니다.
- 엔터키를 누르면 클립보드로 복사합니다.

### 2. 웹사이트로 이동해 번역하기

![result-web](document/result-web.png)

- 긴 문장등의 번역이 필요할 때, 브라우저에서 번역 결과를 보여줍니다.

### 지원 언어 목록

- `한국어 ↔️ 영어, 일본어, 중국어 (간체, 번체), 베트남어, 인도네시아어, 태국어, 독일어, 스페인어, 이탈리아어, 프랑스어`
- 다른 언어간 번역은 추후 지원예정입니다.

## 🚀 Setup

### 0. 필수설치

(macOS Monterey 12.3 이하) Xcode의 설치가 필요합니다.
앱스토어에서 [XCode](https://developer.apple.com/download/all/?q=Xcode)를 설치해주세요.

### 1. Papago API Key 발급받기

파파고 Alfred3 Workflow를 사용하기 위해서는 초기설정이 필요합니다.

> 발급 방법은 [이 링크](https://jvvp.tistory.com/1106)를 참고해주세요.

- Papago API key (client_id)
- Papago secret key (client_secret)

### 2. Papago API Key 설정하기 <kbd>ppconfig</kbd>

![ppconfig](document/ppconfig.png)

- `client_id`에 Client ID를 입력합니다.
- `slient_secret`에 Secret을 입력합니다.
- `Test`를 통해 정상 작동 여부를 확인할 수 있습니다.

## 🎛 Workflow

![workflow](document/workflow.png)

## ❤ Contributions

질문이나 버그를 발견했나요? 특정 기능이 필요하신가요?
자유롭게 새로운 이슈나 각각의 제목과 설명과 함께 PR을 제출하세요.
문제에 대한 해결책을 이미 찾았다면 망설이지 말고 공유하세요.
새로운 제안은 언제든지 환영입니다!

## Licenses

이 프로젝트는 MIT 라이센스를 준수합니다.

```
MIT License
Copyright (c) 2021 eungbean
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
