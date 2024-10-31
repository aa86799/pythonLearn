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
# 使用列表类型
#
# 本方案执行效率较高。
# 原因：虽然两层循环，但外层循环次数特别有限，仅3次；时间复杂度，可以看成 O(3n)
#       但内部有一层删除原列表数据的循环；当数据量较大时，删除(内部移位)操作会较耗时。

import random
import time


def lottery_detail(employs, awards, grades):
    """
    抽奖函数
    :param employs: 员工列表
    :param awards:  各奖项等级的抽奖人数列表
    :param grades:  奖项等级列表
    """
    index = 0
    for grade in grades:
        print(f"-----开始抽{grades[index]}------")
        rand_item = random.sample(employs, awards[index])
        index += 1
        times = 1
        for item in rand_item:
            print(f"第{times}次抽，{grade}抽中的员工编号: {item}")
            times += 1
            employs.remove(item)
    print("-----抽奖结束-----")


def lottery4():
    begin_time = time.time()  # 返回时间浮点数，时间是自1970年1月1日以来的秒数
    multiply = 100  # 数据增长倍数
    employs_count = 300 * multiply  # 员工数量
    prefix_str = "lufei_"
    employs = []
    for i in range(employs_count):
        employs.append(prefix_str + str(i))
    # print(type(employs))
    # print(employs)

    awards3 = 30 * multiply  # 三等奖
    awards2 = 6 * multiply  # 二等奖
    awards1 = 3 * multiply  # 一等奖
    awards = [awards3, awards2, awards1]
    grades = ["三等奖", "二等奖", "一等奖"]

    lottery_detail(employs, awards, grades)

    print(f"共消耗时间 {time.time() - begin_time}")


if __name__ == '__main__':
    lottery4()
