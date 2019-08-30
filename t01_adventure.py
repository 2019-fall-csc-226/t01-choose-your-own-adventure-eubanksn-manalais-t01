######################################################################
# Author: Noah Eubanks, Sama Manalai       TODO: Change this to your names
# Username: Eubanksn Manalais              TODO: Change this to your usernames
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("Hello, what is your name? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to Noah and Sama's ultra magical secret van.")
sleep(delay)
print("You look hungry, would you like some ice-cream?.")
print("We have three flavors to choose from; strawberry, pistachio, and chocolate.")
print()
sleep(delay * 2)
print("These flavors of ice-cream sound very interesting to you, and you want all of them!")
print("But, you only have $1 in your pocket, and can only choose one.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which flavor would you like? [Strawberry/Pistachio/Chocolate]" )

if direction == "Strawberry":
    # Good choice!
    print("Good choice!This makes you feel a lot better considering your friend disappeared mysteriously the other day.")
    sleep(delay)
elif direction == "Chocolate":
    # Oh... Bad choice
    print("Here you go, this is a van favourite!")
    sleep(delay)
    print("Oh it tastes so familiar but not in a good way")
    print("At first you don't realize it but then you start feeling nauseous")
    print("You start vomiting and ask 'what the hell was that?'")
    print("The ice cream people tells you: Don't worry! It's just your friend!")


else:
    # Neutral choice
    print("You feel a tingling sensation in your throat, and you start puking blood and pistachios.")
    print("As everything starts going black, you vaguely hear evil laughter. ")
    print("The ice cream van starts up and a merry song starts playing and slowly fades away")
    dead = True
    sleep(delay)

if dead == True:
    print("Hey friendo! Wanna make some more chocolate ice cream?")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.



# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
