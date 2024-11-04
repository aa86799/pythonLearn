
def test_dict():
    info = {"a": 1, "b": 3.3, 'c': "中华"}
    print(info)

    info.pop("a")
    print(info)

    del info["b"]
    print(info)

    info["c"] = "Happy"
    print(info)

    print(info.get('c'))
    print(info.get('b'))
    print(info.get('a', "Said"))  # 获取不存在的 key 对应的值时，指定了默认值

    print("c" in info)  # key in dict
    print(info.keys())
    print(info.values())
    print(info.items())

    for k,v in info.items():
        print(f"key={k}, value={v}")

    for k in info:  # 遍历效率快
        print(f"key={k}, value={info[k]}")

    print(len(info))


def test_practice():
    """
    1. ⽣成一个包含100个key的字典，每个value的值不能⼀样
    2. {‘k0’: 1, ‘k1’: 1, ‘k2’: 2, ..., ‘k99’: 100}
        请把这个dict中key 截取出整数部分，并输出5的倍数。
    3. 把上一步结果中value是偶数的统一改成-1
    """
    nums = {}
    for i in range(1, 101):
        nums["k" + str(i)] = i
    print(nums)

    nums2 = {}
    for k in nums:
        if int(k.strip("k")) % 5 == 0:
            nums2[k] = nums[k]
    print(nums2)

    nums3 = {}
    for k in nums2:
        if nums2[k] % 2 == 0:
            nums3[k] = -1
        else:
            nums3[k] = nums2[k]
    print(nums3)


if __name__ == "__main__":
    test_dict()

    test_practice()