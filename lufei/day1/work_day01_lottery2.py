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

import random


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
    employs_count = 300
    prefix_str = "lufei_"
    employs = []
    for i in range(employs_count):
        employs.append(Employ(prefix_str + str(i)))
    # print(type(employs))
    # print(employs)

    awards3 = 30  # 三等奖
    awards2 = 6  # 二等奖
    awards1 = 3  # 一等奖
    del_item_list = []  # 待删除员工列表

    print("-----开始抽三等奖------")
    lottery_detail(employs, del_item_list, awards3, "三等奖")

    print("-----开始抽二等奖------")
    lottery_detail(employs, del_item_list, awards2, "二等奖")

    print("-----开始抽一等奖------")
    lottery_detail(employs, del_item_list, awards1, "一等奖")


if __name__ == '__main__':
    lottery2()
