# if文による条件分岐
def bmax(a,b):
    if a > b:
        return a
    else:
        return b

bmax(3, 5)
max(3, 5)

# 様々な条件
1 < 2 < 3
3 >= 2 < 5
not 3 >= 2 < 5

# 練習 absolute
def absolute(x):
    if x < 0:
        return -x
    return x

assert absolute(5) == 5
assert absolute(-5) == 5
assert absolute(0) == 0

# 練習 sign
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

assert sign(5) == 1
assert sign(-5) == -1
assert sign(0) == 0

# 真理値を返す関数
x = 3
x > 1
x < 1
x%2 == 0

def is_even(x):
    return x%2 == 0

is_even(2)
is_even(3)

def is_odd(x):
    if is_even(x):
        return False
    else:
        return True

is_odd(2)
is_odd(3)

# オブジェクト
#Pythonにおける値（式の評価結果）は全てオブジェクトと総称されます。 変数の値もオブジェクトです。
#したがって、数や真理値もオブジェクトです。 今後、文字列やリストなど、様々な種類のデータが登場しますが、 それらは全てオブジェクトです。
#今後、オブジェクトという用語がところどころで出て来ますが、 オブジェクトとデータは同義と思って差し支えありません。 正確には、式の評価結果や変数の値となるデータがオブジェクトです。

# None
None
print(None)

if None: # Noneはfalseのように扱われる
    print('OK')
else:
    print('NG')

# return の後に式を書かないことがあります。
return

# この場合、以下のように None が指定されているとみなされます。
return None

# このようなreturn文を実行すると、関数の実行はそこで終了して None が返ります。

# 条件として使われる他の値
# 数のうち、0 や 0.0 は偽、その他は真とみなされます。
if 0:
    print('OK')
else:
    print('NG')

if -1.1:
    print('OK')
else:
    print('NG')

# 文字列では、空文字列 '' のみ偽、その他は真とみなされます。（文字列については2-1を参照。）
# 組み込み定数 None は偽とみなされます。（None については上記参照。

# 再帰
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(10)
# fib(55)

# https://www.suzu6.net/posts/54-fibonacci-number/
def fb(num):
    """num番目のフィボナッチ数を返す
    """
    a, b = 1, 0
    for _ in range(num):
        a, b = a + b, a
    return b

fb(10000)