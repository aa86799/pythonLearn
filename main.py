# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# import module_minus # 使用时以 module_minus开头
import module_minus as mi

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# 不能定义在 main 函数之后，否则，main 函数中无法访问
def hello():
    print("hello")


def sum(a, b):
    return a+b


# Press the green button in the gutter to run the script.
# main 函数
if __name__ == '__main__':
    print_hi('PyCharm')
    hello()
    print(sum(3, 8))
    print(mi.minus(3, 8))
    a = ["a", "aa"]
    print(a.count(a))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
