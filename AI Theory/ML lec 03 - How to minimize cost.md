# 모두를 위한 딥러닝 강좌 시즌 1

by Sung Kim, 김성훈 교수님

링크

https://www.youtube.com/watch?v=TxIVr-nk1so&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=6

https://www.youtube.com/watch?v=Y0EF9VqRuEA&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=7



### Simplified hypothesis

$$
H(x) = Wx
$$

$$
cost(W) = \frac{1}{m}\sum_{i=1}^{m}(W(x^{i})-y^{i})^2
$$

* cost(W) 그래프는 2차 함수 형태로 나타난다

* cost가 최저인 점을 찾기 위해서 기울기가 0에 수렴하는 지점의 x값을 찾으면 된다
* Gradient descent algorithm (경사 하강법)을 이용할 수 있다



