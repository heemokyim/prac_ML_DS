# 04 Case Study - News Categorization

이때까지 배운 내용으로 다른 패키지 사용없이 한 뉴스에 대해 비슷한 뉴스를 찾아내도록 작성된 코드를 실행하면서, 설명하는 방식으로 진행되는 실습 위주의 강의 정리이다.

* Categorization
* One-hot Encoding
* Bag of words
* Cosine Distance
* Corpus
* List Comprehension

## 비슷한 뉴스를 어떻게 선정할까?

### 문제점

컴퓨터는 문자를 그대로 이해하지 못함

### 문자 -> 숫자?

숫자로 유사하다는 것을 어떻게 표현해야하는가?

유사하다? 가깝다!

좌표의 거리가 가까우면 가깝다라고 표현 가능하다...


### 그래서?

그러면 뉴스를 벡터화 시켜야함!

## 문자를 vector로? = One-hot Encoding

하나의 단어를 Vector의 Index로 인식,  

단어가 존재하면 해당 인덱스가 1, 아니면 0

## Bag of words

One-hot Encdoing 방식을 한문장에 적용하여 인덱스 카운팅함

### the dog is on the table
|are|cat|dog|is|now|on|table|the|
|-|-|-|-|-|-|-|-|
|-|-|1|1|-|1|1|1|


## 유사성

### distance measure

* euclidian distance : 피타고라스 정리
* cosine distance : 두 점 사이의 각도
    * `A.B = ABcos(theta)`

데이터 셋이 클수록 cosine distance가 잘나오더라?

* ex
    * love, hate (5, 0) : love 5번 hate 0번 나온 문서임
    * (5,4), (5,0) (4,0) : 뭐가 더 유사한가?


## 신문기사 분류는 어떻게 하지?

### Process

* 파일 불러오기
* 파일 읽어서 단어사전(corpus) 만들기
* 단어별로 Index 만들기 (dict?)
* 만들어진 인덱스로 문서별로 Bag of words vector 생성
* 비교하고자 하는 문서 비교하기 : `cosine simularity`
* 얼마나 맞는지 측정하기

## 그런데 결국....

이런 과정들은 sklearn으로 다 랩핑 되어있다.

지금 까지 배운건 어떻게 구성되어 있는지 원리를 배운 것이라 생각하면됨.