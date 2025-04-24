# rock, paper, scissor Game
# r>s, s>p, p>r
import random

def play():
    user = input("What's your choice 'r' for rock, 'p' for paper ,'s' for scissor?: ")
    computer = random.choice(['r', 'p', 's'])
     # Rules
    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You Won!"
    
    return "You lost!"

# r>s, s>p, p>r
def is_win(player, opponent):
    if(player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())