# 蛇形矩阵，是一个 n*n 的矩阵
from array import array  # 从 array 模块中直接导入 array 类，导入后，你可以直接使用 array 类，而不需要再通过模块名（array.array）来引用


def snake(n):
    # 列表推导式，用于创建列表的简洁方式
    # 列表推导式的基本结构：[expression for item in iterable]
    #   expression：每次迭代时计算的表达式，决定了列表中每个元素的值。
    #   item：从可迭代对象（iterable）中获取的当前元素。
    #   iterable：可以是任何可迭代对象，如列表、元组、字符串、range对象等
    # 套列表推导式来生成二维列表，如：
    #   array = [[1 + i + j for i in range(7)] for j in range(5)]
    #       for j in range(5) 是外层循环，for i in range(7)是内层循环；
    #       外层循环生成的每一行，是一个列表，确定列表的个数；内层循环生成子列表的元素

    print("---------列表推导式-----------")
    array1 = [[1 + i + j for i in range(7)] for j in range(5)]
    for i in array1:
        print(i)

    print("---------普通循环实现列表推导式同样的结果-----------")
    array2 = []
    for j in range(5):
        array2.append([])
        for i in range(7):
            array2[j].append(1+i+j)
    for i in array2:
        print(i)

    print("---------蛇形矩阵-----------")
    array3 = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    # 使用双重循环遍历列和行。
    # 如果列索引是偶数，则从上到下填充数字。
    # 如果列索引是奇数，则从下到上填充数字。
    for j in range(n):
        if j % 2 == 0:
            for i in range(n):
                array3[i][j] = count
                count += 1
        else:
            for i in range(n-1, -1, -1):  # start=n-1, end=-1(不包括), step=-1； 即  n-1递减到0
                array3[i][j] = count
                count += 1
    for row in array3:
        print(row)
    print("----")
    # 行列转换：array3的每列，转成 rearranged_matrix 的每行
    rearranged_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            rearranged_matrix[i][j] = array3[j][i]
    for row in rearranged_matrix:
        print(row)


if __name__ == "__main__":
    snake(5)
