import numpy as np

class Game:

    def __init__(self, id, repeat_time, head_prop):

        self.id = id
        self.reward = -250
        self.average_reward = 0
        self.repeat_time = repeat_time
        self.head_prop = head_prop
        self.random = np.random
        self.random.seed(id)

    def simulate(self):
        toss_result=[]
        for i in range (0,20):
            if self.random.sample() < self.head_prop:
                toss_result.append('Head')
            else:
                toss_result.append('Tail')

        for j in range (2,20):
            if (toss_result[j] == 'Head') and (toss_result[j-1] == 'Tail') and (toss_result[j-2] == 'Tail'):
                self.reward += 100

        return self.reward

    def repeat(self):

        for k in range (0, self.repeat_time):
            L = Game(self.id, self.repeat_time, self.head_prop)
            self.average_reward += L.simulate()
            self.id += 1

        self.average_reward = self.average_reward/self.repeat_time

        return self.average_reward


Q = Game(1, 1000, 0.5)
print('The expected score:', Q.repeat())
