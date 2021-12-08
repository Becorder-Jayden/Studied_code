# 모두를 위한 딥러닝 강좌 시즌 1

by Sung Kim, 김성훈 교수님

링크

https://www.youtube.com/watch?v=Hax03rCn3UI&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=4

https://www.youtube.com/watch?v=mQGwjrStQgg&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=5





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



#### Tensorflow 작동원리 

<img src="C:\Users\gmkim\Desktop\12333.PNG" alt="12333" style="zoom:67%;" />





### 1) 변수 x, y의 선언을 통한 방법

#### 선형 함수 정의

```python
# Lab 2 Linear Regression
import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility

# X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

# Try to find values for W and b to compute y_data = x_data * W + b
# We know that W should be 1 and b should be 0
# But let TensorFlow figure it out
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

# tf가 인식할 변수를 지정
# 랜덤 변수 1개를 1차원 array에 할당


# Our hypothesis XW+b
hypothesis = x_train * W + b
```

$$
H(x) = Wx+b
$$



```python
# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# reduce_mean으로 평균을 구함
```

$$
cost = \frac{1}{m}\sum_{i=1}^{m}(H(x^{i})-y^{i})^2
$$



#### GradientDescent (경사하강법) 적용

* 함수의 최적값(오차의 최소값)을 찾기 위해 optimizer로 사용되는 방법 중 하나
* 손실함수의 기울기 변화를 통해 손실함수를 줄이는 방법

```python
# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost) # cost를 minimize 함
```



#### 그래프 구현을 위한 과정

```python
# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# tf의 변수(위에서 지정한 W, b)를 사용하기 위해서는 반드시global_variables_initializer()를 실행시켜야 함

# Fit the line
for step in range(2001): # 2000번 정도 스텝을 돌려볼 예정
	sess.run(train)
	if step % 20 == 0: # 잘 진행되는 지 확인하기 위해, 매 20번마다 결과값을 출력
            print(step, sess.run(cost), sess.run(W), sess.run(b))
            

# 결과값 
# Learns best fit W:[ 1.],  b:[ 0.]

"""
0 2.82329 [ 2.12867713] [-0.85235667]
20 0.190351 [ 1.53392804] [-1.05059612]
40 0.151357 [ 1.45725465] [-1.02391243]
...
1960 1.46397e-05 [ 1.004444] [-0.01010205]
1980 1.32962e-05 [ 1.00423515] [-0.00962736]
2000 1.20761e-05 [ 1.00403607] [-0.00917497]
"""

# 처음 시작할 때 cost가 크고 b가 작은 값임을 볼 수 있음
# 2000회 반복을 통해 W가 1에, b가 0에 수렴함을 볼 수 있다.
```



### 2) Placeholders를 사용한 방법

* Placeholders라는 변수 공간을 먼저 설정하고, feed__dict를 통해 학습 데이터를 입력

```python
# Lab 2 Linear Regression
import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility

# 1) 방법과 달리, 아래 과정을 진행하지 않음 
'''
# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
'''

# Try to find values for W and b to compute Y = W * X + b
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

# placeholders for a tensor that will be always fed using feed_dict
# See http://stackoverflow.com/questions/36693740/
X = tf.placeholder(tf.float32, shape=[None]) # 변수 공간 설정
Y = tf.placeholder(tf.float32, shape=[None])

# Our hypothesis is X * W + b
hypothesis = X * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# optimizer
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Launch the graph in a session.
with tf.Session() as sess:
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    # Fit the line
    for step in range(2001):
        _, cost_val, W_val, b_val = sess.run([train, cost, W, b], feed_dict={X: [1, 2, 3], Y: [1, 2, 3]})
        if step % 20 == 0:
            print(step, cost_val, W_val, b_val)
    # feed_dict에 train data 값을 기입         
            
            
    # Testing our model
    print(sess.run(hypothesis, feed_dict={X: [5]}))
    print(sess.run(hypothesis, feed_dict={X: [2.5]}))
    print(sess.run(hypothesis, feed_dict={X: [1.5, 3.5]}))

    # Learns best fit W:[ 1.],  b:[ 0]
    """
    0 3.5240757 [2.2086694] [-0.8204183]
    20 0.19749963 [1.5425726] [-1.0498911]
    ...
    1980 1.3360998e-05 [1.0042454] [-0.00965055]
    2000 1.21343355e-05 [1.0040458] [-0.00919707]
    [5.0110054]           # feed_dict={X: [5]}일 때 예측 값
    [2.500915]            # feed_dict={X: [2.5]}일 때 예측 값
    [1.4968792 3.5049512] # feed_dict={X: [1.5, 3.5]}일 때 예측 값
    """
```



#### 위 코드의 Tensorflow 작동구조를 표현한 이미지

<img src="C:\Users\gmkim\Desktop\12333rreqr.PNG" alt="12333rreqr" style="zoom: 67%;" />
