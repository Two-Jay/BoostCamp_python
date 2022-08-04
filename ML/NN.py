# Neural Network
# 비선형 데이터셋을 사용하여 네트워크를 구축하고 훈련하고 예측하기

# 각 행벡터 O가 데이터 X 와 가중치 행렬 W 사이의 행렬곱에 절편 B의 합이라고 하자.
# O == X*W+B

# 데이터 X 가 입력 데이터이고, W 가 가중치 행렬이다.
# 이를 이용하여 예측하는 함수를 구성한다.
# 레이어 X 의 노드에서 출력 노드 O 의 노드로 연결될 때
# W의 행렬은 입력 노드에서 출력 노드로의 학습 가중치(방향)을 결정한다.

# 소프트맥스 : 분류문제에서 활용
# 모델의 출력을 확률로 변환하여 예측하는 것을 소프트맥스라고 한다.
# 학습을 하는 경우에는 softmax를 활용
# 추론을 하는 경우에는 소프트맥스를 사용하지 않는다. - 대신 최대값 주소만 1로 출력하는 one-hot 벡터를 사용한다.

# 예제
import numpy as np
def softmax(vec): # softmax (Wx + b)
    denumerator = np.exp(vec - np.max(vec, axis = -1, keepdims = True))
    return denumerator / np.sum(denumerator, axis = -1, keepdims = True)
vec = np.array([[0.3, 2.9, 4.0], [-1, 0, -0.5], [-10.0, 0, 10.0]])
print(softmax(vec))

# 선형모델을 활성함수로 변환하여 잠재벡터를 도출하는 것을 신경망이라고 한다.\

# 활성함수 activation function
# sigmod : 시그모이드 함수, tanh : 탄젠트 함수 - 전통적으로 활용
# ReLU : ReLU 함수 - max{0,x}
# Leaky ReLU : Leaky ReLU 함수 - max{0,x}와 같은 효과를 얻는다.

def sigmod(x):
    return 1 / (1 + np.exp(-x)) # 수치상 안정화 x

def sigmod_np(x):
    return np.where(x < 0, np.exp(x)/(1 + np.exp(x)), 1/(1 + np.exp(-x)))

# scipy.special.expit
from scipy.special import expit
sig = expit(np.array([0.25, 0.5, 0.6, 0.7, 0.4]))
print(sig)


# 하이퍼볼릭 탄젠트 함수
def tanh(x):
    p_exp_x = np.exp(x)
    n_exp_x = np.exp(-x)
    return (p_exp_x - n_exp_x) / (p_exp_x + n_exp_x)
# 시그모이드 함수는 정규분포와 유사하다.
# 탄젠트 함수는 시그모이드 함수와 다르게 정규분포와 유사하지 않다.
# 하이퍼볼릭 탄젠트 함수의 경우 범위가 -1 ~ 1 사이
# 시그모이드 함수의 경우 범위가 0 ~ 1 사이
# 하이퍼볼릭 탄젠트 함수의 경우 중앙값이 0, 미분최대값이 1이다
# 시그모이드 함수의 경우 중앙값이 0.5, 미분최대값이 0.3이다

# 학습률에 있어서 하이퍼볼릭 탄젠트 함수가 더 유리하다.... 왜?!

def ReLU(x): return np.maximum(0, x)
# ReLU 함수는 은닉층에서 많이 사용된다.
# 기울기 소실 문제가 발생하는 경우에는 ReLU 함수를 사용한다.
# 기존 활성화 함수에 비해 속도가 빠르다.

# Dying ReLU
# 음수 값이 들어가는 경우 모두 0으로 반환되기에, 기울기도 모두 0으로 나와버린다.
# 가중치가 업데이트 되면서 가중치 합이 음수가 되는 순간 렐루는 0으로 반환된다.
# 따라서 해당 뉴런은 0만 반환하는 죽은 뉴런이 된다.
# 이런 죽은 뉴런을 초래하는 현상을 죽어가는 렐루 현상이라고 한다.

# 이를 해결하기 위해 PReLU, Leaky ReLU, ELU 등이 있다.
# 이러한 경우 음수 값이 들어가는 경우 특정값을 반환하도록 한다.
# 0.01 (Leaky ReLU) 또는 파라미터 값 (PReLU)을 반환한다.

def ELU(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))


# 다층 신경망의 구조
# 다층 퍼셉트론은 신경망이 여러층 합성된 함수
# ! : 이론적으로 2층 신경망으로도 임의의 연속함수를 근사할 수 있다.
# ! : 하지만 층이 깊을수록 목적함수를 근사하는데 필요한 뉴런의 수가 빨리 줄어들어
# ! : 효율적 학습이 가능하다. 