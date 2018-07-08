# 01 pythonic code

**Pythonic Code**
* 남 코드에 대한 이해도
* 효율
* 간지

**Topics**
* split & join
* list comprehension
* enumerate & zip

**Good Materials**
* 파이썬을 여행하는 히치하이커를 위한 안내서
* 파이썬 코딩의 기술

## split & join

`practice/01_pythonic_code/01_split_join.py` 참고

## list comprehension

기존 리스트를 사용하여 다른 리스트를 만드는 방법

`practice/01_pythonic_code/02_list_comprehension.py` 참고

## enumerate & zip

### enumerate
* list 의 element를 추출할 때 번호랑 같이 붙여서 추출

### zip

* 여러 리스트를 병렬적으로 추출 가능하게함

`practice/01_pythonic_code/03_zip.py` 참고

## lambda & map reduce

### lambda

* 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
* 수학 람다 대수에서 유래함
* 맵 리듀스랑 같이 사용했을 때 효율성을 발휘 할 수 있다?

파이썬 3 부터는 권장하지 않으나 여전히 많이 쓰임

* 하지만 넘파이, 판다스랑 같이 쓰면 좋은점은 여전히 있음

### map

* sequence 자료형 각 element에 동일한 (lambda) 함수를 적용함

### reduce

* sequence 자료형에 lambda를 적용해 하나의 결과로 내보냄

이 모든 건 `practice/01_pythonic_code/04_lambda_mapreduce.py`에서 참고

### 주의사항

* python3의 권장사항이 아님
* 하지만 각종 데이터분석이나 머신러닝에서 그대로 쓰이고 있는 중


## Asterisk

* 흔히 알고있는 *
* 단순 곱셈, 제곱연산, 가변인자 활용 등 다양하게 사용됨

`practice/01_pythonic_code/05_asterisk.py`에서 참고