import string


def test_list():
    names = ['alex', 'jack']
    print(names)
    names.append("rain")
    print(names)
    names.insert(2, "⿊黑姑娘")
    print(names)
    n2 = ["aa", "bb"]
    names.extend(n2)  # 扩展继承，实际就是 合并了 n2
    print(names)
    names.insert(0, n2)  # 嵌入了列表 n2
    print(names)
    del names[0]  # 删除列表的指定索引处
    print(names)
    names.pop()  # 删除列表最后一个元素
    print(names)
    names.remove("rain")  # 删除指定元素
    print(names)
    print(names.index("aa"))
    print(names.count("aa"))
    print("aa" in names)  # 是否在列表中

    # 切片
    print(names[0:4])  # 输出从0开始的[0, 3]元素
    print(names[:3])  # 输出<索引3的元素
    print(names[1:])  # 输出索引1之后的元素
    print(names[4:5])  # 空列表
    print(names[-1])  # 倒切时，右侧第一个索引为-1
    print(names[-3:-1])  # [-3, -1) 只输出了两个元素 -3/-2处的元素
    print(names[-3:])  # -3处之后的所有元素
    # 跳着切
    print([1, 2, 3, 4, 5, 6, 7, 8][1:6:2])  # [start:end:step]  => [2,4,6]
    print([1, 2, 3, 4, 5, 6, 7, 8][::2])  # [start:end:step]  => [1,3,5,7]

    # 排序
    names.sort()
    print("sort:", names)
    names.reverse()
    print("reverse", names)

    for i in names:
        print(i)


if __name__ == '__main__':
    test_list()
