# Compatibility with Python Interpreter >3.6
# Before running this program, make sure you've added the TERM environment variable with the value xterm-color.
from dialogue import Dialogue
import dialogue as dl
import sys
dl.initializeColorCodes()

# Initialization
money: int = 100
choices: int = 0

# Initialize Dialogue
dl.delayedPrint(f'Currently, you have {money} units of money. Your choices result in the loss or gain of your money.', 3, 1)
dl.delayedPrint(dl.processStyle("Choose Wisely.", 'red', 'italic'), 2, 1)
dl.loader(3)
dl.clearScreen()
dl.delayedPrint("Enter your floor number for morning registration: ", returnLine=False)
floorNum: int = int(input())
if 8 >= floorNum >= 5:
    temp1: Dialogue = Dialogue("Your form room teacher is already gone.",
        [
            "Give Mr Mobsby 50 units of money and let him to make up the MR",
            "Give PSO 25 units of money and let him to make up the MR",
            "Do nothing"
        ]
    )
    returned = temp1.fetch(1.5)
    dl.clearScreen()
    if returned == 'a':
        dl.delayedPrint("You have used 50 units of money to let Mr. Mobsby make up the MR for you.", 3, 1)
        dl.delayedPrint("He gives back you the money and says: ", 1.5, 0.5, returnLine=False)
        dl.delayedPrint(dl.processStyle("I am not in short of money.", style_name='italic'), 1, 1)
        dl.delayedPrint(dl.processStyle("He then gives you back your money and helped you make up your MR.", 'green'), 2.5, 1)
    elif returned == 'b':
        dl.delayedPrint("You have used 25 units of money to let PSO make up the MR for you.", 3, 1)
        dl.delayedPrint("The PSO helped you make up your MR.", 1.5, 1)
        money -= 25
    else:
        dl.delayedPrint(
            "Your form room teacher has found out that you didn't come for MR, so he took away 30 units of your money.",
            3, 1)
        money -= 30
    choices += 1
elif 5 > floorNum > 0:
    dl.delayedPrint(dl.processStyle("You've survived from the MR in the morning.", 'green'), 2, 2)
elif floorNum <= 0:
    temp1: Dialogue = Dialogue("You suddenly feel an immense force of gravity pulling you downwards, as if the floor of the elevator collapsed.",[
        "Try to hold on to something",
        "Scream for help"
    ])
    dl.delayedPrint("When going down the staris, you noticed an elevator that seemingly appeared out of nowhere in the wall of the stairwell.\nYou entered and messed around with the elevator buttons.", 2, 0.5)
    dl.delayedPrint("You didn't notice that the floor number of the elevator kept decreasing below 0.", 3.5, 1)
    dl.delayedPrint("The noise of the running elevator slowly became overwhelming.\nYou noticed that the elevator is beginning to shake violently.\n", 2, 1)
    temp1.fetch(3.5, 2, framed=False)
    dl.clearScreen()
    dl.delayedPrint("You tried...", 1, 0.5, returnLine=False)
    dl.delayedPrint(" But your efforts were in vain.", 3.5, 0.5)
    dl.delayedPrint("As you watched the world fade from your eyes, you felt a sudden 'thud' on your back.", 2.5, 1)
    dl.delayedPrint("You've entered... ", 1, 0.5, returnLine=False)
    dl.delayedPrint(dl.processStyle("The Backrooms.", 'yellow', 'bold'), 3, 2)
    dl.delayedPrint(dl.processStyle("error error error error failed context fetching error error error error unauthorized access to simulation error error error error", 'red', 'underlined'), 1, 0)
    dl.clearScreen()
    sys.exit()
else:
    dl.clearScreen()
    dl.delayedPrint(dl.processStyle("What were you even doing there?", 'red', 'underlined'), 3, 1)
    sys.exit()

print()
dl.delayedPrint(f'You currently have {dl.processStyle(str(money), color_name="yellow", style_name="bold")} units of money.', 2, 1)
dl.loader(3, "Loading Dialogues")
dl.clearScreen()

dl.delayedPrint(f'Input the floor of your {dl.processStyle("first", "blue")} class: ', returnLine=False)
class1 = int(input())
dl.delayedPrint(f'Input the floor of your {dl.processStyle("second", "yellow")} class: ', returnLine=False)
class2 = int(input())
dl.delayedPrint(f'Input the floor of your {dl.processStyle("third", "purple")} class: ', returnLine=False)
class3 = int(input())

dif1 = abs(class1 - class2)
dif2 = abs(class2 - class3)
dif3 = abs(floorNum - class1)

if dif1 + dif2 + dif3 + class3 > 15:
    dl.delayedPrint(f'Since there\'s too much stairs for you to climb, you have been deducted {dl.processStyle("20 units of money.", "orange")}', 3, 1)
    money -= 20
else:
    dl.delayedPrint(dl.processStyle("You have survived from climbing the stairs in the morning!", "green"), 3, 1)

print()
dl.delayedPrint(f'You currently have {dl.processStyle(str(money), color_name="yellow", style_name="bold")} units of money.', 2, 1)
dl.loader(3, "Loading Dialogues")
dl.clearScreen()

lunch: Dialogue = Dialogue(f'Now that you\'ve finished your last class of the day, choose a way to {dl.processStyle("have", "blue")}/{dl.processStyle("obtain", "orange")} your lunch:',
   [
       "Steal other students' takeaway",
       "Order food takeaway",
       "Eat in the school canteen"
   ]
)

lunchAns: chr = lunch.fetch(2, 0.5, 1.5)
if lunchAns == 'a':
    dl.delayedPrint("You stole a student's lunch...", 2, 1, False)
    dl.delayedPrint(dl.processStyle(" but Mr. Mobsby caught you.", 'red', 'italic'), 3, 1)
    dl.delayedPrint(dl.processStyle("You received a detention from Mr. Mobsby and was taken 50 units of money.", 'red'), 3, 1)
    money -= 50
elif lunchAns == 'b':
    dl.delayedPrint("You ordered a takeaway. However, a student had stole it from you. Because of it, you lost 50 units of money.", 4, 2)
    dl.delayedPrint(dl.processStyle("Luckily, Mr. Mobsby felt empathy for you and shared his lunch and some money with you. You gained 50 units of money.", 'green'), 4, 1)
    money += 50
else:
    dl.delayedPrint("You paid 50 units of money for the food in the canteen.", 2, 1)
    dl.delayedPrint(f"However, the food caused you a stomachache and you had to take care of it by paying {dl.processStyle("50 more units of money", 'orange')} by receiving medicine from the infirmary.",6, 2)
    money -= 10
choices += 1

print()
dl.delayedPrint(f'You currently have {dl.processStyle(str(money), color_name="yellow", style_name="bold")} units of money.', 2, 1)
dl.loader(3, "Loading Dialogues")
dl.clearScreen()

night: Dialogue = Dialogue(
    "The school is over. Now it is time for night study.",
    [
        "Escape night study",
        "Study Attentively"
    ]
)
nightStudy = night.fetch(2, optionDelay=2)
if nightStudy == 'a':
    dl.clearScreen()
    activity: Dialogue = Dialogue(
        "You've escaped night study. You can now do some activities.",
        [
            "Play Football",
            "Exercise in the Gym"
        ]
    )
    act = activity.fetch(2, optionDelay=1)
    if act == 'a':
        dl.delayedPrint("Sadly, you've been caught by Mr. Mobsby. That's 50 points off for you.", 2, 1)
    else:
        dl.delayedPrint("Your PE Teacher found you and encouraged you because you got U in your last fitness test. Extra 60 points for you.", 3, 1)
    choices += 1
else:
    dl.delayedPrint("Sadly, your inward curling action is discovered by your friends. Minus 10 points.", 2, 1)
choices += 1

print()
dl.delayedPrint(f'You currently have {dl.processStyle(str(money), color_name="yellow", style_name="bold")} units of money.', 2, 1)
dl.loader(5, "Processing Results")
dl.clearScreen()

if money > 0:
    dl.delayedPrint(f'You have survived SCIE! Your current amount of money is {dl.processStyle(str(money), color_name="green", style_name="bold")}.', 3, 1)
else:
    dl.delayedPrint(f'Your total amount of money is {dl.processStyle(str(money), color_name="orange", style_name="bold")}.', 3, 1, False)
    dl.delayedPrint(dl.processStyle(f' Watch out from now on, since you now owe SCIE {money} units of money.', "red", "italic"), 3, 1)

dl.delayedPrint(f'You made {dl.processStyle(str(choices), "aqua", "underlined")} big choices in SCIE today.', 3, 1)

