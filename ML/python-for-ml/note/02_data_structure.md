# 02 Data Structure

`collections` 모듈에 기본적으로 배웠던 자료구조들이 구현되어 있다

* deque
* OrderedDict
    * dict와 달리, 데이터를 입력한 순서대로 dict를 반환함
    * dict type위 값을, value 또는 key값으로 정렬할 때 사용가능 (lambda 이용)
* defaultdict
    * 기본값을 지정 가능할 수 있는 dict
* Counter
    * sequence type의 data element들 갯수를 카운트해 dict 로 반환해줌
    * 정렬까지 알아서 해줌
* namedtuple
    * C struct 같은거?