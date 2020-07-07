import random


class Menu:
    """
    可以随机推荐菜品的工具类，因为每次推荐会改变内部状态，
    所以每次推荐开始时，需要重新实例化一个新对象
    """

    menu = []

    def __init__(self):
        self.menu.append('黄瓜炒鸡蛋')
        self.menu.append('烧茄子')
        self.menu.append('酱香排骨')
        self.menu.append('红烧肉')
        self.menu.append('糖醋鱼')

    def random_recommend(self):
        """
        随机推荐菜品，每种菜品只推荐一次当所有菜品均推荐过后，返回None
        :return: 菜品名称或None
        """

        if len(self.menu) == 0:
            return None

        this_recommended = random.choice(self.menu)
        self.menu.remove(this_recommended)
        return this_recommended


def getUserInput(tip):
    """
    引导用户输入，只需要是/否
    :param tip:提示用户的信息
    :return:是/否
    """
    while True:
        user_input = input(tip)

        if user_input == '是' or user_input == '否':
            return user_input
        else:
            continue


while True:
    need = getUserInput('是否需要推荐菜品？(是/否)')

    if need == '是':
        menu = Menu()

        while True:
            recommended = menu.random_recommend()

            if recommended is None:
                print('本店没有合乎您味口的菜品。')
                break

            print('本次推荐菜品： ' + recommended)
            satisfied = getUserInput('请问是否满意？(是/否)')

            if satisfied == '是':
                print('您满意的菜品是：' + recommended + '。 谢谢品尝！')
                break
            else:
                continue
    else:
        break

    break
