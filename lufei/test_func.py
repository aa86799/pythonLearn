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


xp = "xp"
hobby = ["唱歌", "插花"]


def test_func_global(hob):
    # print(xp)  # 直接使用外部的全局变量，报错了
    # xp = "vp"  # 这只是局部变量
    # print("局部变量 xp=", xp)
    global xp  # 声明使用全局变量。 要注意，不能在这之前 声明同名的局部变量
    print("全局变量", xp)
    hob[0] = "跑步"  # 列表、字典形参，本身不可变，但


class Clz:
    # 封装成类方法，可通过 Clz.func() 调用，第一个是隐含参数，调用时不用输入。但这不是类似 java 中的静态方法，@staticmethod声明静态方法
    # 文档中有更多的声明，特别是在不同的 python 版本中，有一些特定说明
    field_a = "fa"

    @classmethod
    def func(cls):
        print(cls)

    @staticmethod  # 封装成静态方法
    def func_static():
        print("func_static")


class SubClz(Clz):

    def child_method(self):
        print("child")


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

    print("------全局变量-----")
    test_func_global(hobby)
    print("全局变量", xp, hobby)

    print("------内置函数------")
    print(all([0, 1, 2, 3, 4]))  # 所有为 true ， 非0零 true
    print(all((0, 1, 2, 3, 4)))
    print(any([0, 1, 2, 3, 4]))  # 任意一个为 true
    print(ascii("中国abc1234"))  # '\u4e2d\u56fdabc1234'
    print(eval(ascii("中国abc1234")))  # 中国abc1234
    print(bin(9999))  # 0b 开头的二进制  0b10011100001111
    # breakpoint()
    print(bytearray("中国", "utf-8"))  # bytearray(b'\xe4\xb8\xad\xe5\x9b\xbd')   返回一个可变字节序列
    print(bytearray(2))  # bytearray(b'\x00\x00')
    print(bytearray())  # bytearray(b'')
    print(bytes('中', "gbk"))  # 返回 不可变字节序列
    print(callable(hobby))  # 是否是可调用的函数 false
    print(callable(test_func_global))  # 是否是可调用的函数  true
    print(chr(97))  # 返回 Unicode 码位为整数 i 的字符的字符串格式. 'a'
    print(ord('A'))  # 返回 字符的 Unicode 码位整数
    Clz.func()
    Clz.func_static()
    # compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)  # 编译源码文件 更多见文档
    print(complex("+1.23"))  # 将特定的字符串或数字转换为一个复数，或基于特定的实部和虚部创建一个复数。虚部必须带有 j或 J 后缀。
    print(complex(1.23))
    print(complex("+1.23-4.5j"))
    print(complex('-Infinity+NaNj'))
    setattr(Clz, "name_a", "sun")  # 设置对象属性值，属性可以不预先存在于类声明中
    print(getattr(Clz, "name_a"))  # 获取属性
    print(getattr(Clz, "field_a"))  # 获取属性
    print(hasattr(Clz, "field_c"))  # 是否包含属性
    print(globals())  # 返回实现当前模块命名空间的字典。对于函数内的代码，这是在定义函数时设置的，无论函数在哪里被调用都保持不变。
    print(hash(Clz))  # 返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）
    # help()  # 交互式帮助系统
    print(hex(989898).upper())  # 将整数转换为带前缀 "0x" 前缀的小写十六进制数字符串
    print(id(Clz))  # 返回对象的“标识值”。该值是一个整数，在此对象的生命周期中保证是唯一且恒定的。两个生命期不重叠的对象可能具有相同的 id() 值。
    # in_str = input("请输入")  # 接收标准输入；如果有参数，则写入标准输出
    # print("你输入的是", in_str)
    clz_obj = Clz()
    print(isinstance(clz_obj, Clz))  # 如果 object 参数是 classinfo 参数的实例，或者是其 (直接、间接或 虚拟) 子类的实例则返回 True。
    clz_sub = SubClz()
    print(issubclass(Clz, Clz))  # 如果 class 是 classinfo 的子类（直接、间接或 虚的 ），则返回 True。类将视为自己的子类。
    print(issubclass(SubClz, (Clz)))  # 如果 class 是 classinfo 的子类（直接、间接或 虚的 ），则返回 True。类将视为自己的子类。

    print(1234)
