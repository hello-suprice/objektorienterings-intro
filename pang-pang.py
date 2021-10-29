import random as rand
class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.scores = 0

    def fire(self):
        input("Press any key to shoot!")
        if rand.uniform(0,1) >= 0.5:
            self.inc_scores()
            print("You hit the sus!")
        else:
            print("You missed the sus!")
        if rand.uniform(0,1) >= 0.5:
            self.reduce_lifes()
            print("You got hit by the sus!")
        else:
            print("The sus missed")


    def inc_scores(self):
        self.scores += 1

    def reduce_lifes(self):
        self.lifes -= 1


a_player = Player(3)
while a_player.lifes > 0:
    a_player.fire()
