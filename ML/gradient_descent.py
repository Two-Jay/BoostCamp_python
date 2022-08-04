

# 함수 f(x)의 미분 곡선이 있다고 가정했을 때
# 특정 시작점 (x, f(x)) 에서 기울기를 구하면
# 어느 방향으로 점을 움직여야 함수값이 증가/감소하는지 알 수 있다
# 이렇게 해서 미분값을 빼면 경사하강법이라 하여
# 함수의 극소값을 구할 수 있다.


# 경사하강법을 이용하여 함수의 극소값을 구하는 코드
# gradient : 미분계산 함수
# init : 초기값
# lr : 학습률
# eps : 종료 조건

# def gradient_descent(gradient, init, lr, eps=1e-8):
#     x = init
#     grad = gradient(x)
#     while abs(grad) < eps:
#         x = x - lr * grad
#         grad = gradient(x)
#     return x


# 경사하강법을 이용하여 그래디언트 벡터의 극소값을 구하는 코드
# gradient : 그래디언트 벡터 계산 함수
# init : 초기값
# lr : 학습률
# eps : 종료 조건

# def gradient_descent(gradient, init, lr, eps=1e-8):
#     x = init
#     grad = gradient(x)
#     while norm(grad) < eps:
#         x = x - lr * grad
#         grad = gradient(x)
#     return x