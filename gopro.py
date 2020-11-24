
class Legend():

    def __init__(self, name, level, exp):
        self.name = name
        self.level = level
        self.exp = exp

    def show_legend(self):
        print(self.name)
        print(self.level)
        print(self.exp)

    def level_up(self):
        self.level += 1



pers1 = Legend('Guldan', 1, 100)

pers1.show_legend()

pers1.level_up()

pers1.show_legend()