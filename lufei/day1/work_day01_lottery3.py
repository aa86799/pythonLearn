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
# 使用列表类型，存储员工 class 对象；
# 若is_choice 已经为 True，则continue 跳过循环；每次抽将完成后，将员工属性 is_choice 置为 True
#

import random


def lottery_detail(employs, complete_times, awards_count, grade):
    times = 0
    while complete_times < awards_count:
        rand_item = random.choice(employs)
        if rand_item.is_choice:  # 已抽中， 进行下次循环
            continue
        times += 1
        complete_times += 1
        print(f"第{times}次抽，{grade}抽中的员工编号: {rand_item.name}")
        rand_item.is_choice = True


class Employ:
    def __init__(self, name, is_choice):
        self.name = name
        self.is_choice = is_choice  # 是否已抽中


def lottery3():
    employs_count = 300
    prefix_str = "lufei_"
    employs = []
    for i in range(employs_count):
        employs.append(Employ(prefix_str + str(i), False))
    # print(type(employs))
    # print(employs)

    awards3 = 30  # 三等奖
    awards2 = 6  # 二等奖
    awards1 = 3  # 一等奖
    complete_times = 0  # 已抽员工次数，传入函数时，值都是 0

    print("-----开始抽三等奖------")
    lottery_detail(employs, complete_times, awards3, "三等奖")

    print("-----开始抽二等奖------")
    lottery_detail(employs, complete_times, awards2, "二等奖")

    print("-----开始抽一等奖------")
    lottery_detail(employs, complete_times, awards1, "一等奖")


if __name__ == '__main__':
    lottery3()
