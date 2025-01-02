class Kassa(object):
    def __init__(self, money=0):
        self.money = money

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, x):
        if x > self.money:
            print("В кассе осталось недостаточно денег для снятия")
        else:
            self.money -= x


k = Kassa()
k.top_up(7000)
print(k.count_1000())
k.take_away(9000)
print(k.money)