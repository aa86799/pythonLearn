# 《炸金花》底层逻辑实现
# 自己写一个程序，实现发牌、比大小判断输赢.
# 游戏规则:
# 一付扑克牌，去掉大小王，每个玩家发3张牌，最后比大小，看谁赢.有以下几种牌:
# 豹子:三张一样的牌，如3张6.
# 同花顺:即3张同样花色的顺子，如红桃5、6、7
# 顺子:又称拖拉机，花色不同，但是顺子，如红桃5、方片6、黑桃7，组成的顺子对子:2张牌一样
# 单张:单张最大的是A
# 这几种牌的大小顺序为，豹子>同花顺>同花>顺子>对子>单张需程序实现的点:
# 1.先生成一付完整的扑克牌
# 2.给5个玩家随机发牌
# 3.统一开牌，比大小，输出赢家是谁
# 4.各牌型中出现，点数一致，但不同花色时，判断结果为 大小一致。eg. ♠️2/3/4 平 ♥️2/3/4

import random

豹子 = 6
同花顺 = 5
同花 = 4
顺子 = 3
对子 = 2
单张 = 1

pokers_ch = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
pokers_color = ['♠️', '♥️', '♣️', '♦️']


def poker_mode_desc(pokers_mode):
    if pokers_mode == 6:
        result = "豹子"
    elif pokers_mode == 5:
        result = "同花顺"
    elif pokers_mode == 4:
        result = "同花"
    elif pokers_mode == 3:
        result = "顺子"
    elif pokers_mode == 2:
        result = "对子"
    else:
        result = "单张"
    return result


class Player:
    def __init__(self, name, pokers, pokers_mode):
        self.name = name  # 玩家名
        self.pokers = pokers  # 持有的三张牌列表
        self.pokers_mode = pokers_mode  # 牌型


class Poker:
    """单张牌模型"""

    def __init__(self, color, char, char_index):
        self.color = color  # 花色
        self.char = char  # 点数
        self.char_index = char_index  # 点数索引

    def __str__(self):
        return self.color + self.char


def swap(players, i, j):
    """
    交换玩家位置
    """
    temp = players[i]
    players[i] = players[j]
    players[j] = temp


def compare(players):
    """
    1. 玩家对象 按牌型排序
    2. 单玩家手中牌  按点数字符的索引排序
    3. 遍历玩家对象，首元素跳过，牌型大的位置不变，牌型小的交换元素位置到前一个位置；
            牌型相同时：
                a. 牌型 in [豹子, 同花顺, 顺子]: 判断牌列表首字符索引大的则大；eg. [2/2/2] < [3/3/3], [9/10/J] < [10/J/Q]
                    考虑特殊顺子的情况 [2/3/A] < [3/4/5] 符合判定规则。
                b. 牌型 == 对子：判断是符合 [A/A/B] 还是 [A/B/B] ，取出属于对子的点数索引，和单张的点数索引，再分别判断。
                    对子的点数索引大则大；其若相同时，再判断 单张的点数索引大则大。
                c. 牌型 in [同花、散张]：因为前面已经内部对三牌列表进行了升序排序，先判断第三张哪个大的则大，再判断第2张，再判断第一张。
    4. 注意：例如，当牌型全是单张时，且最大点数索引不一致，列表[11,12,7,5]，在一次遍历后，得到[12,11,5,7]；
            此结果，并不符合最终期望[5,7,11,12]。所以外部调用时，需要比较 (player_count-1)次
    :return: 返回 排序后的新的玩家 players 列表
    """
    print("------牌型大小排序后------")
    new_players = sorted(players, key=lambda p: p.pokers_mode)  # 玩家对象 按牌型排序
    for item in new_players:
        item.pokers = sorted(item.pokers, key=lambda p: p.char_index)  # 单玩家手中牌  按点数字符的索引排序
        print(f"玩家-{item.name}，", f"牌型-{poker_mode_desc(item.pokers_mode)}，", display(item.pokers))
    for i in range(0, len(new_players)):
        if i == 0:
            continue
        elif new_players[i].pokers_mode > new_players[i - 1].pokers_mode:  # 当前的牌型大
            continue
        elif new_players[i].pokers_mode < new_players[i - 1].pokers_mode:  # 当前的牌型小
            swap(new_players, i, i - 1)
        else:  # 后面的牌型不大，即 相等
            if new_players[i].pokers_mode in [豹子, 同花顺, 顺子]:  # 内部比大小规则一致的
                if new_players[i].pokers[0].char_index < new_players[i - 1].pokers[0].char_index:
                    swap(new_players, i, i - 1)
            elif new_players[i].pokers_mode == 对子:
                i_duizi_char_index = -1
                i_single_char_index = -1
                if new_players[i].pokers[0].char == new_players[i].pokers[1].char:
                    i_duizi_char_index = new_players[i].pokers[0].char_index
                    i_single_char_index = new_players[i].pokers[2].char_index
                else:
                    i_duizi_char_index = new_players[i].pokers[1].char_index
                    i_single_char_index = new_players[i].pokers[0].char_index
                last_duizi_char_index = -1
                last_single_char_index = -1
                if new_players[i - 1].pokers[0].char == new_players[i - 1].pokers[1].char:
                    last_duizi_char_index = new_players[i - 1].pokers[0].char_index
                    last_single_char_index = new_players[i - 1].pokers[2].char_index
                else:
                    last_duizi_char_index = new_players[i - 1].pokers[1].char_index
                    last_single_char_index = new_players[i - 1].pokers[0].char_index
                if i_duizi_char_index < last_duizi_char_index:
                    swap(new_players, i, i - 1)
                elif i_duizi_char_index == last_duizi_char_index:
                    if i_single_char_index < last_single_char_index:
                        swap(new_players, i, i - 1)
            else:  # 同花、散张，内部比大小规则一致的
                if new_players[i].pokers[-1].char_index < new_players[i - 1].pokers[-1].char_index:
                    swap(new_players, i, i - 1)
                elif new_players[i].pokers[-1].char_index == new_players[i - 1].pokers[-1].char_index:
                    if new_players[i].pokers[-2].char_index < new_players[i - 1].pokers[-2].char_index:
                        swap(new_players, i, i - 1)
                    elif new_players[i].pokers[-2].char_index == new_players[i - 1].pokers[-2].char_index:
                        if new_players[i].pokers[-3].char_index < new_players[i - 1].pokers[-3].char_index:
                            swap(new_players, i, i - 1)
    return new_players


def is_baozi(pokers):
    """
    三个点数是否一致
    """
    return pokers[0].char == pokers[1].char and pokers[0].char == pokers[2].char


def is_tonghua(pokers):
    """
    三个花色是否一致
    """
    return pokers[0].color == pokers[1].color and pokers[0].color == pokers[2].color


def is_shunzi(pokers):
    """
    先按点数字符索引排序。判断是否是特殊顺子牌型 23A；循环判断后一位的索引减去前一位的索引的差值是否为1.
    """
    flag = True
    pokers = sorted(pokers, key=lambda p: p.char_index)  # 排序
    # 特殊的顺子牌型顺序 [2, 3, A]
    if pokers[0].char == pokers_ch[0] and pokers[1].char == pokers_ch[1] and pokers[2].char == pokers_ch[-1]:
        return flag
    for i in range(0, len(pokers)):
        if i == 0:
            continue
        if pokers[i].char_index - pokers[i - 1].char_index != 1:
            flag = False
            break
    return flag


def is_duizi(pokers):
    """
    先按点数字符索引排序。前两个点数或后两个点数是否一致
    """
    pokers = sorted(pokers, key=lambda p: p.char_index)  # 排序
    if pokers[0].char == pokers[1].char or pokers[1].char == pokers[2].char:
        return True
    return False


def is_tonghuashui(pokers):
    """
    是否 既是同花且是顺子
    """
    return is_tonghua(pokers) and is_shunzi(pokers)


def mode_grade(pokers):
    """
    :param pokers: 单人手中的牌列表
    :return: 牌型等级
    """
    if is_baozi(pokers):
        return 豹子
    if is_tonghuashui(pokers):
        return 同花顺
    if is_tonghua(pokers):
        return 同花
    if is_shunzi(pokers):
        return 顺子
    if is_duizi(pokers):
        return 对子
    return 单张


def display(pokers):
    values = []
    for item in pokers:
        values.append(f"{item.color}{item.char}")
    return values


def gambling():
    print("------开始生成一幅牌------")

    pokers = []
    for ch in pokers_ch:  # 13个字符点数
        for color in pokers_color:  # 4种花色
            pokers.append(Poker(color, ch, pokers_ch.index(ch)))
    print(display(pokers))

    print("------洗牌后------")
    pokers_count = len(pokers)  # 整幅牌数量 13*4=52
    pokers = random.sample(pokers, pokers_count)
    print(display(pokers))

    print("------切牌------")
    players_count = 10  # 总玩家数
    every_players_pokers_count = 3  # 每人发三张
    players = []
    for i in range(0, players_count):
        players.append(Player(str(i + 1), [], -1))
        for j in range(0, every_players_pokers_count):
            players[i].pokers.append([])
    random_index = random.randint(1, pokers_count - 1)  # 首发牌 index
    print(f"------切牌后，从第{random_index + 1}张开始发牌------")
    # 由各玩家手中牌，组成的列表
    for i in range(0, every_players_pokers_count):
        for j in range(0, players_count):
            players[j].pokers[i] = pokers[random_index]
            if i == 2:
                players[j].pokers_mode = mode_grade(players[j].pokers)
            random_index += 1
            if random_index == pokers_count:
                random_index = 0  # 归零
    for item in players:
        print(f"玩家-{item.name}，", f"牌型-{poker_mode_desc(item.pokers_mode)}，", display(item.pokers))

    print("------比大小------")
    # grade = mode_grade(players_pokers[0])
    # grade = mode_grade([Poker('♠️','A'), Poker("♥️","A"), Poker('♦️','A')])  # 测试豹子牌型
    # grade = mode_grade([Poker('♥️','A'), Poker("♥️","3"), Poker('♥️','2')])  # 测试同花顺牌型
    # grade = mode_grade([Poker('♠️','A'), Poker("♠️","Q"), Poker('♠️','K')])  # 测试同花顺牌型
    # grade = mode_grade([Poker('♠️', 'A'), Poker("♠️", "3"), Poker('♠️', '4')])  # 测试同花牌型
    # grade = mode_grade([Poker('♠️','A'), Poker("♦️","3"), Poker('♠️','4')])  # 测试同花牌型
    # grade = mode_grade([Poker('♠️','A'), Poker("♣️","Q"), Poker('♦️','K')])  # 测试顺子牌型
    # grade = mode_grade([Poker('♠️','A'), Poker("♣️","3"), Poker('♦️','2')])  # 测试顺子牌型
    # grade = mode_grade([Poker('♠️','A'), Poker("♣️","A"), Poker('♦️','3')])  # 测试对子牌型
    # grade = mode_grade([Poker('♠️','3'), Poker("♣️","4"), Poker('♦️','4')])  # 测试对子牌型
    # grade = mode_grade([Poker('♠️','3'), Poker("♣️","2"), Poker('♦️','5')])  # 测试对子牌型
    # print("测试：", grade)

    # mode_list = []
    # for item in players_pokers:
    #     mode_list.append(Mode_Poker(mode_grade(item), item))
    # for item in mode_list:
    #     display(item.pokers)

    players.append(Player("11", [Poker('♣️', 'J', 0), Poker('♠️', 'Q', 2), Poker('♣️', 'K', 12)], 3))
    players.append(Player("12", [Poker('♥️', 'J', 0), Poker('♦️', 'Q', 2), Poker('♠️', 'K', 12)], 3))
    players_count += 2

    # 因使用内部元素比对后，交换位置的方法，所以需要类似冒泡排序一样，增加一个外部循环，进行多次排序。
    for i in range(0, players_count - 1):
        new_players = compare(players)
        players = new_players
    print("------比大小，排序最终结果------")
    for item in players:
        print(f"玩家-{item.name}，", f"牌型-{poker_mode_desc(item.pokers_mode)}，", display(item.pokers))
    print("------比大小，最大结果------")
    step = -1
    for i in range(0, players_count):
        if i == 0:  # step + i 即 [-1] ，肯定是属于最大的其一
            print(f"玩家-{players[step + i].name}，", f"牌型-{poker_mode_desc(players[step + i].pokers_mode)}，",
                  display(players[step + i].pokers))
            step -= 2
            continue
        cur = players[step + i]  # step(-3) + i(1) 即 [-2] 右向左数第2个
        pre = players[step + i + 1]
        # 后面的 每一位字符和前面的每一位相同，则一样大
        if cur.pokers_mode == pre.pokers_mode and cur.pokers[0].char == pre.pokers[0].char \
                and cur.pokers[1].char == pre.pokers[1].char and cur.pokers[2].char == pre.pokers[2].char:
            print(f"玩家-{players[step + i].name}，", f"牌型-{poker_mode_desc(players[step + i].pokers_mode)}，",
                  display(players[step + i].pokers))
            step -= 2
        else:
            break


if __name__ == "__main__":
    gambling()
