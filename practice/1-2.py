# https://utokyo-ipp.github.io/1/1-2.html

# 変数
h = 188.0
h

w = 104.0
w / (h/100.0) ** 2

w = 104.0-10
w / (h/100.0) ** 2

# 代入文
w = w-10
w / (h/100.0) ** 2

# 累積代入文
w -= 10
w

w += 10
w

# 関数の定義と返値
def bmi(height, weight):
    return weight / (height/100.0) ** 2

bmi(188.0,104.0)

1.1*bmi(174.0, 119.0 * 0.454)

def felt_air_temperature(temperature, humidity):
    return temperature - 1 / 2.3 * (temperature - 10) * (0.8 - humidity / 100)

felt_air_temperature(28, 50)

def hoge(x):
    x

hoge(2)
print(hoge(2))

#　練習 ft_to_cm
def ft_to_cm(f, i):
    return (f + i / 12) * 30.48

assert round(ft_to_cm(5, 2) - 157.48, 6) == 0 # not error
assert round(ft_to_cm(6, 5) - 195.58, 6) == 0 # not error

# 練習 quadratic
def quadratic(a, b, c, x):
    return a*x**2 + b*x + c

assert quadratic(1, 2, 1, 3) == 16 # not error
assert quadratic(1, -5, -2, 7) == 12 # not error

# ローカル変数
import math

def heron(a,b,c):
    s = 0.5*(a+b+c)
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

heron(3, 4, 5)

s

# print
def heron(a,b,c):
    s = 0.5*(a+b+c)
    print('The value of s is', s)
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

heron(1,1,1)

# printとreturn
def heron(a,b,c):
    s = 0.5*(a+b+c)
    print('The value of s is', s)
    print(math.sqrt(s * (s-a) * (s-b) * (s-c)))


heron(1,1,1)
heron(1,1,1) * 2

# コメントと空行
# heronの公式により三角形の面積を返す
def heron(a,b,c): # a,b,c は三辺の長さ

    # 辺の合計の半分をsに置く
    s = 0.5*(a+b+c)
    print('The value of s is', s)

    return math.sqrt(s * (s-a) * (s-b) * (s-c))

heron(2,2,2)

# 関数の参照の書き方
# 特になし

# 練習 qe_disc qe_solution1 qe_solution1
def qe_disc(a, b, c):
    return b**2-4*a*c

def qe_solution1(a, b, c):
    return (-b-math.sqrt(qe_disc(a,b,c)))/(2*a)

def qe_solution2(a, b, c):
    return (-b+math.sqrt(qe_disc(a,b,c)))/(2*a)

assert qe_disc(1, -2, 1) == 0
assert qe_disc(1, -5, 6) == 1
assert round(qe_solution1(1, -2, 1) - 1, 6) == 0
assert round(qe_solution2(1, -2, 1) - 1, 6) == 0
assert round(qe_solution1(1, -5, 6) - 2, 6) == 0
assert round(qe_solution2(1, -5, 6) - 3, 6) == 0

# グローバル変数
g = 9.8

def force(m):
    return m*g

force(104)

g = g/6
force(104)

a = 10
def foo():
    return a
def bar():
    a = 3
    return a

foo()
bar()
a
a = 20
foo()

def boo(a):
    return(a)
boo(5)

a