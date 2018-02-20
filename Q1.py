import numpy as np

class Game:

    def __init__(self, repeat_time, head_prop):

        self.toss_result = []
        self.reward = -250
        self.average_reward = 0
        self.repeat_time = repeat_time
        self.head_prop = head_prop

    def simulate(self):

        for i in range (0,20):
            if np.random.sample() < self.head_prop:
                self.toss_result.append('Head')
            else:
                self.toss_result.append('Tail')

        for j in range (2,20):
            if (self.toss_result[j] == 'Head') and (self.toss_result[j-1] == 'Tail') and (self.toss_result[j-2] == 'Tail'):
                self.reward += 100

        return self.reward

    def repeat(self):

        for k in range (0, self.repeat_time):
            L = Game(self.repeat_time, self.head_prop)
            self.average_reward += L.simulate()

        self.average_reward = self.average_reward/self.repeat_time

        return self.average_reward


Q = Game(1000, 0.5)
print(Q.repeat())

