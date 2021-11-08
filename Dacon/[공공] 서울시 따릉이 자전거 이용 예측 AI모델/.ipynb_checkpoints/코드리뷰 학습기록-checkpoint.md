# 코드리뷰 학습기록

## 코드 명 : [제주TP]_따릉이 공유

<br/>

### 2021.11.04

#### 학습 코드 내용

* 따릉이 데이터 확인
* EDA

#### 새롭게 알게 된 점

##### from EDA

* plt.plot을 이용하면 일반적인 점 그래프를 그릴 수 있다

* plt.axvline(x, color) : 축을 가로지르는 세로 선 생성

  plt.text(x, y, s, fontsize) : 원하는 위치에 텍스트 생성

* 상관계수는 보통 0.4 이상일 때 상관성이 있다고 얘기한다

* sns.lmplot : 점 그래프에 linearmodel을 추가한다

* sns.kdeplot : 커널밀도추정 그래프_변수의 분포를 파악하기 위해 표본 데이터의 분포로부터 모집단의 부포 특성을 추정하는 것

* sns.boxplot : 최대, 최소, 평균, 사분위수를 보기 위한 그래프, 특이치를 발견하기에 좋다.

* sns.pairplot : 데이터 셋의 숫자형 특성에 대하여 각각에 대한 히스토그램과 두 변수 사이의 scatter plot을 그린다

* sns.jointplot : 두 변수의 분포에 대한 분석과 두 변수 사이의 scatter plot을 동시에 확인할 수 있는 그래프이다. (cf. scatter plot 대신 hex plot으로 대체할 수 있다)

* sns.violinplot : box plot과 비슷하지만 분포에 대한 보충 정보가 제공

* sns.relplot : scatterplot과 lineplot의 상위 개념의 그래프다. 산점도와 선 그래프 모두 그릴 수 있다

<br/>

##### 전처리

* 결측값을 확인하고 대체하는 작업이 필요

##### KNeighborREgressor

* X_train, y_train, x_test로 나누어서 진행
* n_splits = k 에서 k 값에 따라 k개씩 묶음을 진행한 분석