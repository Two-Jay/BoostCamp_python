import numpy as np
import numpy.linalg as LA

v = np.array([1, 2, 3])
print(v)
print(v.shape)

# 노름 - 원점에서의 거리
# L1 norm : 각 성분의 변화량의 절대값의 합
# L2 norm : 각 성분의 변화량^2의 합의 제곱근 - 피타고라스 정리를 이용한 유클리드 거리
la = LA.norm(v) # LA.norm 은 L2 norm 을 이용하여 계산한다.
print("{0:.2f}".format(la))

# 각 노름의 특성에 따라 머신러닝 상에서 용도가 다르다.
# L1 노름은 Robust 학습, Lasso 회귀
# L2 노름은 회귀, Ridge 회귀, Elastic Net 회귀, Lapalace 근사에 사용된다.

# L1 norm implementation
def l1_norm(v): return np.sum(np.abs(v))

# L2 norm implementation
def l2_norm(v): return np.sqrt(sum(v**2))

print(l1_norm(v))
print(l2_norm(v))

# 예제
# 두 벡터사이의 거리 계산
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(LA.norm(v1))
# 위의 예제는 L1 norm 을 이용하여 계산한다.

# 예제
# 두 벡터사이의 각도 계산
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(LA.norm(v1 + v2))
# 위의 예제는 L2 norm 을 이용하여 계산한다.

# cos 값을 구하는 함수
def cos_sim(v1, v2):
    return np.inner(v1, v2) / (LA.norm(v1) * LA.norm(v2)) # 두 벡터의 내적을 이용하여 cos 값을 구한다.


# 행렬의 내적
# 두 행렬의 내적을 구하는 함수
def dot(A, B):
    return np.dot(A, B)

np.random.seed(0)
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
print(dot(A, B))
print(A)
print(LA.inv(A))
print(LA.pinv(A))  # pseudo inverse


