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

import random

豹子 = 6
同花顺 = 5
同花 = 4
顺子 = 3
对子 = 2
单张 = 1

pokers_ch = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
pokers_color = ['♠️', '♥️', '♣️', '♦️']


class Player:
    def __init__(self, name, pokers, pokers_mode):
        self.name = name
        self.pokers = pokers
        self.pokers_mode = pokers_mode


class Poker:
    def __init__(self, color, char):
        self.color = color
        self.char = char

    def __str__(self):
        return self.color + self.char


def swap(players, i, j):
    temp = players[i]
    players[i] = players[j]
    players[j] = temp


def compare(players):
    print("------牌型大小排序后------")
    new_players = sorted(players, key=lambda p: p.pokers_mode)
    for item in new_players:
        item.pokers = sorted(item.pokers, key=lambda p: pokers_ch.index(p.char))
        print(f"玩家{item.name}", item.pokers_mode, display(item.pokers))
    for i in range(0, len(new_players)):
        if i == 0:
            continue
        elif new_players[i].pokers_mode > new_players[i - 1].pokers_mode:  # 当前的牌型大
            continue
        elif new_players[i].pokers_mode < new_players[i - 1].pokers_mode:  # 当前的牌型小
            swap(new_players, i, i - 1)
        else:  # 后面的牌型不大，即 相等
            if new_players[i].pokers_mode in [豹子, 同花顺, 顺子]:  # 内部比大小规则一致的
                if pokers_ch.index(new_players[i].pokers[0].char) < pokers_ch.index(new_players[i - 1].pokers[0].char):
                    swap(new_players, i, i-1)
            elif new_players[i].pokers_mode == 对子:
                i_duizi_char = ""
                i_single_char = ""
                if new_players[i].pokers[0].char == new_players[i].pokers[1].char:
                    i_duizi_char = new_players[i].pokers[0].char
                    i_single_char = new_players[i].pokers[2].char
                else:
                    i_duizi_char = new_players[i].pokers[1].char
                    i_single_char = new_players[i].pokers[0].char
                last_duizi_char = ""
                last_single_char = ""
                if new_players[i - 1].pokers[0].char == new_players[i - 1].pokers[1].char:
                    last_duizi_char = new_players[i - 1].pokers[0].char
                    last_single_char = new_players[i - 1].pokers[2].char
                else:
                    last_duizi_char = new_players[i - 1].pokers[1].char
                    last_single_char = new_players[i - 1].pokers[0].char
                if pokers_ch.index(i_duizi_char) < pokers_ch.index(last_duizi_char):
                    swap(new_players, i, i-1)
                elif pokers_ch.index(i_duizi_char) == pokers_ch.index(last_duizi_char):
                    if pokers_ch.index(i_single_char) < pokers_ch.index(last_single_char):
                        swap(new_players, i, i-1)
            else:  # 同花、散张，内部比大小规则一致的
                if pokers_ch.index(new_players[i].pokers[-1].char) < pokers_ch.index(new_players[i - 1].pokers[-1].char):
                    swap(new_players, i, i-1)
                elif pokers_ch.index(new_players[i].pokers[-1].char) == pokers_ch.index(new_players[i - 1].pokers[-1].char):
                    if pokers_ch.index(new_players[i].pokers[-2].char) < pokers_ch.index(new_players[i - 1].pokers[-2].char):
                        swap(new_players, i, i-1)
                    elif pokers_ch.index(new_players[i].pokers[-2].char) == pokers_ch.index(new_players[i - 1].pokers[-2].char):
                        if pokers_ch.index(new_players[i].pokers[-3].char) < pokers_ch.index(new_players[i - 1].pokers[-3].char):
                            swap(new_players, i, i-1)
    return new_players

def is_baozi(pokers):
    # flag = True
    # for i in range(0, len(pokers)):
    #     if i == 0:
    #         continue
    #     if pokers[i].char != pokers[i - 1].char:
    #         flag = False
    #         continue
    # return flag
    return pokers[0].char == pokers[1].char and pokers[0].char == pokers[2].char


def is_tonghua(pokers):
    # flag = True
    # for i in range(0, len(pokers)):
    #     if i == 0:
    #         continue
    #     if pokers[i].color != pokers[i - 1].color:
    #         flag = False
    #         continue
    # return flag
    return pokers[0].color == pokers[1].color and pokers[0].color == pokers[2].color


def is_shunzi(pokers):
    flag = True
    pokers = sorted(pokers, key=lambda p: pokers_ch.index(p.char))  # 排序
    # 特殊的顺子牌型顺序 [2, 3, A]
    if pokers[0].char == pokers_ch[0] and pokers[1].char == pokers_ch[1] and pokers[2].char == pokers_ch[-1]:
        return flag
    for i in range(0, len(pokers)):
        if i == 0:
            continue
        if pokers_ch.index(pokers[i].char) - pokers_ch.index(pokers[i - 1].char) != 1:
            flag = False
            continue
    return flag


def is_duizi(pokers):
    pokers = sorted(pokers, key=lambda p: pokers_ch.index(p.char))  # 排序
    if pokers[0].char == pokers[1].char or pokers[1].char == pokers[2].char:
        return True
    return False


def is_tonghuashui(pokers):
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
    for ch in pokers_ch:
        for color in pokers_color:
            pokers.append(Poker(color, ch))
    print(display(pokers))

    print("------洗牌后------")
    pokers_count = len(pokers)  # 整幅牌数量
    pokers = random.sample(pokers, pokers_count)
    print(display(pokers))

    print("------切牌------")
    players_count = 5  # 总玩家数
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
            if random_index >= pokers_count - 1:
                random_index = 0  # 归零
    for item in players:
        print(item.pokers_mode, display(item.pokers))

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

    # 因使用内部元素比对后，交换位置的方法，所以需要类似冒泡排序一样，增加一个外部循环，进行多次排序。
    for i in range(0, players_count):
        new_players = compare(players)
        players = new_players
    print("------比大小，最终结果------")
    for item in players:
        print(f"玩家{item.name}", item.pokers_mode, display(item.pokers))

if __name__ == "__main__":
    gambling()
