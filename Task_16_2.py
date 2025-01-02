class Cherepashka(object):
    def __init__(self, hod_x, hod_y, s):
        self.s = s
        self.hod_x = hod_x
        self.hod_y = hod_y

    def go_up(self, s):
        self.hod_y +=s

    def go_down(self, s):
        self.hod_y -=s

    def go_left(self, s):
        self.hod_x -= s

    def go_right(self, s):
        self.hod_y +=s

    def evolve(self, s):
        s += 1

    def degrade(self, s):
        s -= 1
        if s<=0:
            print('Error')

    def count_moves(self, x2, y2):
        return self.hod_x - x2, self.hod_y - y2
