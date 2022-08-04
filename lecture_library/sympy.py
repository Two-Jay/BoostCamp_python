# sympy 를 이용하면 미분계산을 할 수 있다
import sympy as sym
from sympy.abc import x

answer = sym.diff(sym.poly(x ** 2 + 2*x +3), x)
print(answer)