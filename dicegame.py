
import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
while True:
    player=input("Enter the number of players(2-4)=")
    if player.isdigit():
        player=int(player)
        if 2<= player<=4:
            break
        else:
            print("Must be between 2-4 players !!")
    else:
        print("Invalid Number...please try again")
print("Lets start with",player,"players.")
max_score=10
player_scores=[0 for i in range(player)]
while max(player_scores)< max_score:
    for player_idx in range(player):
        print("Player",player_idx+1,", its your turn")
        print("Your total score is : ",player_scores[player_idx],"\n")
        current_score=0
        while True:
            should_roll=input("Would you like to roll(y/n)?")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                print("You rolled a 1 !! Opps")
                break
            else:
                current_score += value
                print("You rolled a:",value)
            print("Your score is=",current_score)
        player_scores[player_idx]+= current_score
        print("Your total score is:",player_scores[player_idx])
max_score=max(player_scores)
winning_idx= player_scores.index(max_score)
print("Congratulations!player number",winning_idx+1,"is the winner eith a score of =",max_score)














