
import random


moves = ['rock', 'paper', 'scissors']

class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2, rounds):
        self.p1 = p1
        self.p2 = p2
        self.player1_score = 0
        self.player2_score = 0
        self.rounds = rounds

    def play_round(self):
        move1 = self.p1.move()
        move2 = input('rock or paper or scissors? :').lower()
        while move2 not in moves:
            move2 = input('Invalid choice. Please enter rock, paper, or scissors: ').lower()  
        
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        
        if beats(move1, move2):
            self.player1_score += 1
            print("\nPlayer 1 wins this round!")
        elif beats(move2, move1):
            self.player2_score += 1
            print("\nPlayer 2 wins this round!")
        else:
            print("\nIt's a tie!")
            
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        
        print(f"Score: Player 1 = {self.player1_score}, Player 2 = {self.player2_score}") 

    def play_game(self):
        
        for round in range(self.rounds):
            print(f"\n\nRound {round + 1}:")
            self.play_round()
            
        print("\nGame over!")
        print(f"Final Score: Player 1 = {self.player1_score}, Player 2 = {self.player2_score}")


        if self.player1_score > self.player2_score:
            print("\nPlayer 1 wins the game!")
        elif self.player2_score > self.player1_score:
            print("\nCongratulations, you win!")
        else:
            print("\nThe game is a tie!")



def replay_game():
    replay = input("\nDo you want to play again? (yes or no): ").lower()
    return replay == "yes"



def get_valid_rounds():
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? "))
            if rounds > 0:
                return rounds
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    while True:
        rounds = get_valid_rounds()
        game = Game(Player(), Player(),rounds)
        print("Let's start, I'm Player 1 and you're Player 2")
        game.play_game()
        
        if not replay_game():
            print("Thanks for playing!")
            break