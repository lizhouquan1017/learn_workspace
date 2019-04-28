class Fruit:
    def info(self):
        print("我是一个水果！重%g 克" %self.weight)


class Food:
    def taste(self):
        print("不同实物的口感不同")


class Apple(Fruit, Food):
    pass


a = Apple()
a.weight = 15
a.info()
a.taste()