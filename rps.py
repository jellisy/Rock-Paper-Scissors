import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        pass

    score = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RepeatPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            response = input("Enter your choice:\n"
                             "Rock\tPaper\tScissors\n>>").lower()
            if response in moves:
                return response
            else:
                print("Sorry, I don't understand.")


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            if self.my_move == moves[0]:
                return moves[1]
            elif self.my_move == moves[1]:
                return moves[2]
            else:
                return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def winner(self):
        if self.p1.score > self.p2.score:
            print("Player 1 is the Champion!\nFinal Score:\n"
                  f"Player 1: {self.p1.score}\tPlayer 2: {self.p2.score}")
        elif self.p2.score > self.p1.score:
            print("Player 2 is the Champion!\nFinal Score:\n"
                  f"Player 1: {self.p1.score}\tPlayer 2: {self.p2.score}")
        else:
            print("The Champion remains undecided!")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if (self.p1.beats(move1, move2) is True and
                self.p2.beats(move2, move1) is False):
            self.p1.score += 1
            print("Player 1 wins!")
        elif (self.p1.beats(move1, move2) is False and
              self.p2.beats(move2, move1) is True):
            print("Player 2 wins!")
            self.p2.score += 1
        else:
            print("It's a draw!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Player 1: {self.p1.score}\tPlayer 2: {self.p2.score}")

    def play_game(self):
        print("Game start!")
        self.p1.score = 0
        self.p2.score = 0
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        self.winner()
        self.play_again()

    def play_again(self):
        while True:
            answer = input("Would you like to play again?\n"
                           "Enter 'Yes' or 'No'\n>>").lower()
            if "yes" in answer:
                game.play_game()
            elif "no" in answer:
                print("Until we meet again!")
                exit(0)
            else:
                print("Sorry, I don't understand.")
                self.play_again()


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
