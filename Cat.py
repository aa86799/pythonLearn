class Cat:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("dump")  # 内存回收

    def __str__(self):
        return '[name=' + self.name + "]," + super.__str__(self)

    def eat(self):
        print("cat like to eat fish", " name=" + self.name)


if __name__ == '__main__':
    tom = Cat("tom")
    tom.eat()
    tom.name = "abc"
    tom.eat()
    print(tom.__str__())
