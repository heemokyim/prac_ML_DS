# lec_02_linear_regression

### contents

* Hypothesis
* cost

## predicting exam socre: regression

* suprevised learning 을 한다
    * regression : 0 ~ 100
    * `Training` :hour => score label을 가지고 학습을 시킨다
        * 모델이 생성됨

## data

| x (feature) | y |
| - | - |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

## Hypothesis

가설을 세운다

* Linear한 모델이 여기에 좋을것이다.
* 그럼 어떤 선을 찾아야 하나?
    * 이걸 찾아가는 과정이 학습(**Training**)

위의 데이터와 regression 모델에서는  
이 막대 그래프가 잘맞을 것 같다!

```
H(x) = Wx + b
```

이 W와 b를 학습 시켜보자!

## Cost(loss) function

기존 Training set과 얼마나 모델이 다를까를 평가해주는 function

`H(x) = Wx + b`에 대해 `(H(x) - y) ^ 2`를 **Cost Function** 으로 잡고 평가해보자.

``` py
H(x) = Wx + b
m = num of training data set
cost = (1/m) * sum( (H(x) - y) ^ 2 )

Goal : minimize(W, b) cost(W, b)
```

## tensorflow step

1. build graph
1. sess.run
1. output or upgrade mode1.1.