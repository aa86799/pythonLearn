def test_character_set():
    """
    任意编码转换成unicode的过程，都叫解码
    任意unicode转换成指定编码的过程，都叫编码
    """

    char = '中国'
    # 编码成 gbk
    gbk_bytes = char.encode("GBK")
    print(gbk_bytes)  # 输出 b'\xd6\xd0\xb9\xfa'  16进制表示  ⼀个16进制是占4位(如1111），2个就是8位(即1字节)

    # 解码
    print(gbk_bytes.decode("GBK"))
    # print(gbk_bytes.decode("utf-8"))  # error


if __name__ == "__main__":
    test_character_set()
