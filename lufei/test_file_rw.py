def test_file_rw():
    """
    以读("r")、写("w")、追加("a") 3种模式中的任意一种打开⽂件，不能即写又读。
    open()有个encoding参数,默认是None, 是⽤来告诉解释器，要操作的这个文件 是什么编码。
        不填的话，就用解释器默认编码，即utf-8。
    混合模式：
        r+，读写，能读能写, 初始光标在文件开头，若直接写入，则会覆盖原内容；文件不存在会报错。
        w+，写读，文件不存在会创建。 已存在，清空内容并覆盖写入
        a+，追加读，⽂件一打开时光标会在文件尾部,写的数据全会是追加的形式
    """
    f = open("test_file_rw_temp", mode="w")  # 写模式， 若⽂文件已存在，则覆盖，不存在则创建
    f.write("crazy boy")
    f.close()
    print("------------")

    f = open("test_file_rw_temp", mode="a")  # 追加模式  若⽂文件已存在，则追加，不存在则创建
    f.write("\nfunny girl")
    f.close()
    print("------------")

    f = open("test_file_rw_temp", mode="r")
    # read = f.read()  # 读取所有，前面已读取部分，则会继续读取剩余部分
    read = f.read(5)  # 读取5个字符
    print(read)
    f.seek(len(read) + 1)  # 指定位置到第6个字节之后  注意是按字节计算的
    read = f.read(3)  # 继续读取后3个字符
    print(read)
    f.read(1)  # 读取到换行符
    print(f.readline())  # 读取整行
    f.close()


def test_file_rw2():
    print("----test_file_rw2----")
    f = open("test_file_rw_temp", mode="r")
    for line in f:
        new_str = line.replace("\n", "")
        print(new_str)
    f.close()


def test_file_rw3():
    print("----test_file_rw3----")
    f = open("person_info", mode="r")
    for line in f:
        line = line.split()
        name, addr, height, weight, phone = line
        height = int(height)
        weight = int(weight)
        if height > 170 and weight <= 50:  # 只打印身高>170 and 体重<=50的
            print(line)
    f.close()


def test_file_rw4():
    print("----test_file_rw4----")
    f1 = open("zz4.jpeg", mode="rb")  # 二进制 只读
    ary1 = bytearray(f1.read(1024 * 5))  # 读取 30kb

    f2 = open("zz5.jpeg", mode="ab")  # 二进制 追加
    f2.write(ary1)  # 多次追加写入后，图片文件占用空间会不断增长；但由于每次从头开始读取，无法在追加后预览
    f2.close()

    ary2 = f1.read()  # 读取剩余所有
    f3 = open("zz6.jpeg", mode="wb")  # 二进制 写入
    f3.write(ary1)  # 写入 数组1
    f3.write(ary2)  # 再写入 数组2
    f3.close()

    print("----other func----")
    print(f1.mode)  # 打开的模式
    print(f1.name)  # 文件名
    print(f1.fileno())  # 返回⽂件句柄在内核中的索引值，以后做IO多路复用时可以用到
    f1.flush()  # 把文件从内存buffer里强制刷新到硬盘
    print(f"readable: {f1.readable()}")
    print(f"seekable: {f1.seekable()}")
    print(f"writable: {f1.writable()}")
    print(f1.tell())  # 当前⽂件操作光标位置
    # print(f1.truncate())  # 图片文件不支持
    f1.close()

    f_temp1 = open("test_file_rw_temp", mode="r")
    f_temp2 = open("test_file_rw_temp2", mode="w")
    f_temp2.write(f_temp1.read())
    f_temp1.flush()
    f_temp1.close()
    print(f_temp2.truncate(15))  # 指定⻓度的话，就从⽂件开头开始截断指定⻓度，即保留15个字节；不指定长度的话，就从当前位置到文件尾部的内容全去掉。 按字节计算
    f_temp2.close()


if __name__ == "__main__":
    # a = input()
    # print(f"输入了 {a}")

    test_file_rw()
    test_file_rw2()
    test_file_rw3()
    test_file_rw4()

    print("----other----")
    f = open("test_file_rw_temp4", mode="w+")
    f.write("aaa")
    f.close()
    f = open("test_file_rw_temp5", mode="a+")
    f.write("bbb")
    f.close()
    f = open("test_file_rw_temp3", mode="r+")  # 文件不存在 error
    f.write("ccc")
    f.close()