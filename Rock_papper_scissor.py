import random
play_character = ["rock","papper","scissor"]
computer_choice = random.choice(play_character)
print("Welcome to the game if you want to play then type 'yes' or type 'no' to exit ")
welcome_message = input("Enter 'yes'or'no' : ")
if welcome_message != "yes":
    c = input("If you want to play click 'yes' Exit = 'no':")
    if c != "yes":
        exit()
    else:
        print("welcome to the game")
else:
    print("welcome to the game")
user_name = input("Enter your Name :")
welcome_message_1 = "LETS BEGIN OUR GAME"
user_1 = ""
def game_start():
    user_1 = input("Enter 'scissor','rock','papper' :")
    if computer_choice != user_1 :
        return "You lose ! or you entered wrong character."
    else:
        quit (user_name +" \nCongratulation! You Win the game")
endi = game_start()
print(endi)
while user_1 != computer_choice:
    print(game_start())


