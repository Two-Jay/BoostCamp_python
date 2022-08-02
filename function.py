
# < how to use function >
# def name_function (parameter #1, parameter #2... ):
#     # function body
#     ...
#     return <value>
#
# name_function(parameter #1, parameter #2... )

def cal_ractangle(width, height):
    return width * height

width = int(input("width: "))
height = int(input("height: "))
print("area: ", cal_ractangle(width, height))


def cal_x (x):
    return (2 * x) + 7

def cal_g (x):
    return x * 2

x = int(input("x: "))
answer = cal_x(x) + cal_g(x) + cal_x(cal_g(x)) + cal_g(cal_x(x))
print("answer of f(x) + g(x) + f(g(x)) + g(f(x)) : ", answer)