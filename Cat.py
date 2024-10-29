class Cat:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("dump")  # 内存回收

    # 类似 toString()
    def __str__(self):
        return '[name=' + self.name + "]," + super.__str__(self)

    def eat(self):
        print("cat like to eat fish", " name=" + self.name)

# 判断一个脚本是否作为主程序执行
# 当脚本直接运行时，__name__的值会被设置为'main'，而当脚本被导入为模块时，__name__的值会被设置为模块名


if __name__ == '__main__':
    tom = Cat("tom")
    tom.eat()
    tom.name = "abc"
    tom.eat()
    print(tom.__str__())
