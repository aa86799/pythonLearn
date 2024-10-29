import string


def test_string_module():
    print(string.ascii_letters)  # 小写和大小字母
    print(string.ascii_uppercase)
    print(string.ascii_lowercase)
    print(string.punctuation)  # 特殊字符
    print(string.digits)  # 数字 0~9


def test_string():
    print("---test_string_section()---")
    s = 'Hello,my name is Alex,golden king.'
    # 字符串的切片操作
    print(s[3:6])  # [3, 6)
    print(s[0:5])

    s = "  abc_ab "
    print("center():", s.center(len(s) + 6, "*"))  # 居中对齐，结果字符串的长度大于原字符串长度，返回新的字符串；否则原字符串；两侧填充指定字符
    print(s.count("ab"))  # 指定字符串的数量
    print(s.count("ab", 3))  # 指定字符串的数量  指定索引开始查询   还可以再指定结束索引
    print(s.encode("utf-8"))  # <class 'bytes'> ，输出 b'  abc_ab '
    print(s.find("ab", 3))  # 查找指定子串的首次开始索引。可以另指定从某个索引开始查询   还可以再指定结束索引
    print(s.rfind("ab"))  # 从右向左,查找指定子串的首次开始索引
    print(s.rfind("ab", 7))  # 未搜索到 返回 -1
    print(s.endswith("ab"))
    print("startswith(): ", s.startswith("ab"))
    print(s.isdigit())
    print(s.islower())
    print("join:", s.join("def"))  # "def"中的每个元素，各自连结s 整体
    print("join:", "".join("def"))  # d,e,f
    print("replace:", s.replace(" ", ""))
    print(f"{s.strip(' ')} len={len(s.strip(' '))}")  # 头尾两端剥除删除指定字符
    print("___abbba".strip("a"))  # out: ___abbb


if __name__ == '__main__':
    test_string_module()
    test_string()