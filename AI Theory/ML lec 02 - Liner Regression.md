# 모두를 위한 딥러닝 강좌 시즌 1

by Sung Kim 



## 02. Linear Regression



※ 회귀문제 예시 : 공부시간에 따른 시험 성적 예측



### (Linear) Hypothesis

선형 회귀 모델은 선형 가정을 기반으로 결과값을 추론한다.

​	선형 가정 : 'x값에 따라 y값이 결정된다'는 관계를 선으로 나타낼 수 있다는 가정



#### 선형모델 : **H(x) = Wx + b**

데이터를 가장 잘 설명하는 H(x)는?

실제 데이터와 가설로 설정한 H(x)와의 오차를 측정 : cost function, loss function



Cost function : H(x) - y
$$
cost = \frac{1}{m}\sum_{i=1}^{m}(H(x^{i})-y^{i})^2
$$


선형모델의 학습은 오차(cost function)을 **최소화 하는 W와 b**를 구하는 것


$$
minimize\_cost(W, b)
$$




## 02. TensorFlow로 간단한 linear regression 구현



```

```

