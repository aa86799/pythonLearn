def test_func_a(a, b=10):  # 默认参数在后面
    print(a, b)


def test_func_b(a, *args):  # 不定长参数个数， 以*开头
    params = [a]
    for i in args:
        params.append(i)
    print(params)


def test_func_c1(c1, c2):
    print(f"v1={c1}, v2={c2}")


def test_func_c(a, *args, **dict_args):  # 参数声明这里**，是将不定长参 a=b 的参数  打包成字典，调用时 字典对应参数的 key 可以随意
    params = [a]
    for i in args:
        params.append(i)
    print(params)
    print(dict_args)
    test_func_c1(**dict_args)  # 这里的**是将字典解包；接受解包后的值的函数参数名必须和 字典中的 key 值一致，包括 参数/key 个数


if __name__ == "__main__":
    test_func_a(100)
    test_func_a(100, 88)
    test_func_a(100, b=99)
    print("------不定长参数(*)------")
    test_func_b(5)
    test_func_b(6, 1)
    test_func_b(7, 1, 2)
    print("------(**将不定长的连续的 a=b 的参数，打包成字典)------")
    test_func_c("a", "b1", 'b2', c1="C1", c2="C2")
    dict = {'c1': 'P1', 'c2': 'P2'}
    test_func_c1(**dict)

