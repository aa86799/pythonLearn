import random


def test_random():
    list = [1, 2, 3]
    random_item = random.choice(list)  # 随机取一个
    print(random_item)
    random_item = random.choice("abc")
    print(random_item)

    random_item = random.randint(3, 5)  # [3, 5] 之内的随机一个数: 3/4/5
    print(random_item)

    random_item = random.sample("abcde", 3)  # 随机采样 3次， 比如可能输出 ['c', 'd', 'a']
    print(random_item)

    random_item = random.randrange(100, 110, 3)  # [100, 110] 范围内，以3为步长的 随机一个数。 stop、step 是可选的。这里 只能是 100/103/106/109
    print(random_item)


if __name__ == '__main__':
    test_random()
