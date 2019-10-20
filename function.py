import numpy as np
def select(num):
    if num == "1":
        return 1
    if num == "2":
        return 0
    if num == "3":
        return -1

class fav:
    def __init__(self, preference):
        self.pre = np.array(preference)
    def score(self, sco):
        self.sco = sco