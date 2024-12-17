# IoT_Project

## 프로젝트 개요
본 프로젝트는 Raspberry Pi를 키보드로 사용하여 버튼 입력을 통해 Morse 부호를 수신하고 이를 영어로 번역하여 사용자와 상호 작용하는 시스템을 개발하는 것입니다. 이 시스템은 웹 인터페이스를 통해 사용자와의 실시간 대화를 지원하며, 사용자가 입력한 영어 문장에 대한 답변을 제공합니다.

- - -

## Raspberry Pi구성 요소
img/diagram.png
+ ***Push button***
  + Button 1 : Morse 부호에서 점(‘•’)입력을 담당
  + Button 2 : Morse 부호에서 점(‘-’)입력을 담당

+ ***LED Button***
  + 짧게 누를 경우, 이전까지 입력된 Morse 부호를 word 리스트에 저장
  + 길게 누를 경우, word 리스트를 웹페이지의 ChatBox에 출력
 
- - -

## 작동 순서

### 버튼 입력 처리

+ ***GPIO 핀 설정***
  + 서버가 시작되면 먼저 GPIO 핀을 설정합니다. 이를 통해 버튼과 LED의 상태를 읽고 쓸 수 있습니다.
    
+ ***버튼 상태 모니터링***
  + 서버는 버튼의 상태를 지속적으로 모니터링해 버튼이 눌리거나 떼어졌는지 감지합니다.
  + 버튼이 눌렸을 때와 떼어졌을 때의 상태 변화를 기록합니다.
    
+ ***모스 부호 입력 기록***
  + 각 Push button은 키보드로써, button을 눌렀을 때는 “•”을, button_2를 눌렀을 때는 “‒”을 입력 받습니다.
    
+ ***단어와 문장 구분***
  + LED button은 키보드의 Enter키와 같은 역할을 하며, 해당 button을 통해 단어와 문장을 구분하여 입력을 저장합니다.
    + 짧게 누르면 지금까지의 입력을 단어로 리스트에 저장합니다.
    + 길게 누르면 문장이 완성된 것으로 간주하고, 지금까지 저장된 단어들을 출력합니다.

### 입력된 모스 부호 번역

+ ***모스 부호 문자열 생성***
  + 기록된 점(•)과 대시(‒)를 조합하여 모스 부호 문자열을 만듭니다.
    
+ ***모스 부호 해석***
  + 모스 부호 문자열을 번역 함수로 전달하여 각 문자를 해석합니다.
  + 번역 함수는 모스 부호와 문자 간의 매핑을 통해 점과 대시를 알파벳과 숫자로 변환합니다.
    
+ ***번역된 텍스트 생성***
  + 해석된 모스 부호를 사용하여 단어와 문장으로 구성된 텍스트를 생성합니다.
  + 번역된 텍스트는 사용자의 입력으로서 웹페이지의 Chatbox에 사용자 질문으로 표시됩니다.
    
### 입력에 대한 응답 생성

+ ***챗봇 응답 생성***
  + 번역된 텍스트를 파이썬 함수에 전달하여 응답을 생성합니다.
  + 입력된 텍스트에 대한 적절한 응답을 사전 정의된 패턴에 따라 생성합니다.

    
+ ***응답 준비***
  + 생성된 응답을 JSON 형식으로 변환하고, 클라이언트에 전송할 준비를 합니다.
    
+ ***응답 전송***
  + 서버는 클라이언트에게 비동기 방식으로 응답을 전송합니다.
  + 클라이언트는 이 응답을 받아 웹페이지의 Chatbox에 표시합니다.
  + 사용자는 화면에서 응답을 확인할 수 있습니다.

- - -

## 향후 개선 사항

### 다국어 지원

+ 현재 시스템은 영어만 지원하므로, 다양한 언어를 지원하도록 확장할 수 있습니다.

### 고급 챗봇 기능

+ 간단한 패턴 매칭 대신 자연어 처리 AI 모델을 사용하여 더 지능적인 챗봇을 구현할 수 있습니다.

### 다양한 입력을 위한 모듈 추가

+ 이번 프로젝트에선 모듈 수의 부족으로 키보드를 재현하기 위해 모스 부호라는 추가적인 단계를 거쳐야 했지만, 더 많은 버튼을 추가하는 것으로 통상 키보드와 같이 자유로운 입력을 구현할 수 있습니다.
