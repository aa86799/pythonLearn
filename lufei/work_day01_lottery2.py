# 年会抽奖
# 奖项如下:路飞科技有限公司有300员工，开年会抽奖，
# 一等奖 3名:泰国5日游+手术费报销
# 二等奖 6名:iPhone16手机
# 三等奖30名: ...
# 规则:
# 1.共抽3次，第一次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
# 2.每个员工限中奖一次，不能重复
# 解题思路:
# 1.生成一个员工列表，用random模块从里面取随机值
# 2.取完值之后，立刻从员工大列表里把中奖人删掉，即可防止其再次中奖
# # # @stone
#
# 使用列表类型，存储员工 class 对象；若已存在于待删除列表，则continue 跳过循环；每次抽将完成后，将数据加入待删除列表；
# 之后将存在于待删除列表中的数据在原始员工列表中删除掉，并清空待删除列表。
#
# 数据量较小时，本方案执行效率还行的；但数据量较大时，就不行了。
# 原因：    for item in del_item_list:
#               employs.remove(item)  employs内部会遍历查找匹配的值
# 时间复杂度 O(n^2)

import random
import time


def lottery_detail(employs, del_item_list, awards_count, grade):
    times = 0
    while len(del_item_list) < awards_count:
        rand_item = random.choice(employs)
        if rand_item in del_item_list:  # 已包含item， 进行下次循环
            continue
        times += 1
        print(f"第{times}次抽，{grade}抽中的员工编号: {rand_item.name}")
        del_item_list.append(rand_item)
    for item in del_item_list:
        employs.remove(item)
    del_item_list.clear()


class Employ:
    def __init__(self, name):
        self.name = name


def lottery2():
    begin_time = time.time()  # 返回时间浮点数，时间是自1970年1月1日以来的秒数
    multiply = 250  # 如果为 1000，则整体超级耗时
    employs_count = 300*multiply
    prefix_str = "lufei_"
    employs = []
    for i in range(employs_count):
        employs.append(Employ(prefix_str + str(i)))
    # print(type(employs))
    # print(employs)

    awards3 = 30*multiply  # 三等奖
    awards2 = 6*multiply  # 二等奖
    awards1 = 3*multiply  # 一等奖
    del_item_list = []  # 待删除员工列表

    print("-----开始抽三等奖------")
    lottery_detail(employs, del_item_list, awards3, "三等奖")

    print("-----开始抽二等奖------")
    lottery_detail(employs, del_item_list, awards2, "二等奖")

    print("-----开始抽一等奖------")
    lottery_detail(employs, del_item_list, awards1, "一等奖")

    print(f"共消耗时间 {time.time() - begin_time}")
    print(f"共消耗时间 {time.time() - 0}")


if __name__ == '__main__':
    lottery2()
