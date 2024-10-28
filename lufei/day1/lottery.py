# 年会抽奖
# 奖项如下:路飞科技有限公司有300员工，开年会抽奖，
# 一等奖 3名:泰国5日游+手术费报销
# 二等奖 6名:iPhone16手机
# 三斤苹果三等奖30名:
# 规则:
# 1.共抽3次，第一次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
# 2.每个员工限中奖一次，不能重复
# 解题思路:
# 1.生成一个员工列表，用random模块从里面取随机值
# 2.取完值之后，立刻从员工大列表里把中奖人删掉，即可防止其再次中奖
# # # @stone

import random


def lottery_detail(employs, del_key_list, awards_count):
    while len(del_key_list) < awards_count:
        rand_item_key = random.choice(list(employs.keys()))
        if rand_item_key in del_key_list:  # 已包含key， 进行下次循环
            continue
        rand_item_value = employs[rand_item_key]
        print(f"三等奖抽中编号 {rand_item_key}")
        del_key_list.append(rand_item_key)
    for key in del_key_list:
        del employs[key]
    del_key_list.clear()


def lottery():
    employs_count = 300
    prefix_str = "lufei_"
    employs = {}  # 员工编号字典列表
    for i in range(employs_count):
        employs[prefix_str + str(i)] = i

    print(type(employs))
    print(employs)

    awards3 = 30  # 三等奖
    awards2 = 6  # 二等奖
    awards1 = 3  # 一等奖
    del_key_list = []  # 待删除员工key列表

    print("-----开始抽三等奖------")
    lottery_detail(employs, del_key_list, awards3)

    print("-----开始抽二等奖------")
    lottery_detail(employs, del_key_list, awards2)

    print("-----开始抽一等奖------")
    lottery_detail(employs, del_key_list, awards1)


if __name__ == '__main__':
    lottery()
