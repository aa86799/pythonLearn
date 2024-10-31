def test_1_variable():
    a = 10
    print(a)
    print(type(a))  # <class 'int'>  整数
    del a  # 删除变量后，再使用 报异常
    # print(a)

    print(type(True))  # <class 'bool'>  布尔
    print(type(1.1))  # <class 'float'>  浮点
    print(type({1, 2, 3, 3}))  # <class 'set'>  集合（无序且不重复)
    print(type([1, 2, 3]))  # <class 'list'>  列表
    print(type({"k1": 1, "k2": 2}))  # <class 'dict'>  字典（k-v)
    print(type(""))  # <class 'str'>  字符串
    print(type(None))  # <class 'NoneType'>   空值类型


def test_2_str():
    age = "22"
    msg = '''My name is Alex, 
I am 22 years old!'''  # 多行 str
    hometown = 'ShanDong'
    print(f"My age is {age} and I was born in {hometown}. {msg}")
    print(age + hometown)
    print(5 * hometown)
    print(hometown * 2)


if __name__ == '__main__':
    test_1_variable()
    aa = {1, 2, 3, 3}
    print(aa)

    test_2_str()
