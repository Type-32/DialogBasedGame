import string
import asyncio
import os
import sys
import random


class Dialogue:
    def __init__(self, ask, responses, actions: list[callable] = None):
        # The constructor. Initializes the objects of this class's instance
        self.ask = ask
        self.responses = responses
        self.actions = actions

    def fetch(self, delay: float = 1, afterDelay: float = 0, optionDelay: float = 1, framed: bool = True, clearScreenBefore: bool = False, setLowerCase: bool = True):
        result = ""
        if clearScreenBefore:
            clearScreen() # Clears screen before printing the prompt and answers.
        if framed:
            delayedPrint("-" * (len(self.ask) + 20), 0) # Prints out the top separator of the prompt.
            delayedPrint(f"     {self.ask}     ", delay) # Prints out the prompt with its respective margin.
            delayedPrint(("-" * (len(self.ask) + 20)) + "\n", 0, afterDelay) # Prints out the bottom separator.
        else:
            delayedPrint(f"{self.ask}", delay, afterDelay) # Prints only the prompt.
        for i in range(len(self.responses)):
            delayedPrint(f"{chr(97+i).upper()}. " + self.responses[i], optionDelay) # Prints out the available answer choices.
        while True:
            result = input(">> ") # Detects user input.

            # Check for Validity:
            # if the answer is empty or out of bounds of available answers, the function re-prompts the user for an answer.
            if result == "":
                continue
            if (ord('a') - ord(result.lower()[0])) <= len(self.responses):
                result = result.upper()[0] if not setLowerCase else result.lower()[0]
                break
        return result # returns a result, either the letter of the choice or the capital letter of the choice.

    def execute(self, delay: float = 1, afterDelay: float = 0, optionDelay: float = 1, framed: bool = True, clearScreenBefore: bool = False, setLowerCase: bool = True):
        ans = ord('a') - ord(self.fetch(delay, afterDelay, optionDelay, framed, clearScreenBefore, setLowerCase).lower())
        print(ans)
        self.actions[ans].__call__()

    def determine(self):
        ans = (ord('a') - ord(self.fetch(True)[0]))
        for i in range(len(self.dialogues)):
            if i == ans:
                return self.dialogues[i]
        return -1

def initializeColorCodes():
    if sys.platform == "win32":
        os.system('')

def pause(): # A simple pause function
    input(processStyle("Press return to continue...", style_name='italic'))

def delayedPrint(content: string, delay: float = 0, afterDelay: float = 0, returnLine: bool = True):
    asyncio.run(__delayedPrint__(content, delay, afterDelay, returnLine)) # uses Asyncio to run the asynchronous function. mimics the effects of sys.sleep(0)


def loader(duration: float = 2, placeholder: string = "Processing"):
    asyncio.run(__loaderText__(duration, placeholder)) # uses Asyncio to run the asynchronous function. mimics the effects of sys.sleep(0)


def clearScreen():
    # if the Operating System is Windows
    if sys.platform == "win32":
        os.system("cls")
    # if the Operating System is Linux or MacOS
    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
        os.system("clear") # Clears the terminal screen.

# The core function of delayedPrint().
async def __delayedPrint__(content: string, delay: float, afterDelay: float, returnLine: bool):
    temp = float(delay / len(content)) # Calculates the duration needed for pause between printing out each letter.
    for i in content: # Prints out the content letter by letter.
        print(i, end='')
        await asyncio.sleep(temp) # Uses an asynchronous await to sleep. similar to sys.sleep().
    if returnLine:
        print() # Returns the Line.
    await asyncio.sleep(afterDelay) # Delays the function after printing out the content. For custom purposes.

# The core function of loader().
async def __loaderText__(duration: float, placeholder: string):
    for _ in range(3):  # Adjust the range for the desired number of cycles
        for dot_count in range(4):  # The number of dot_count will cycle from 0 to 3, with each index representing a character in a loop
            print(f'\r{placeholder}...  [ {__loaderSpinner__(dot_count)} ]', end='')
            await asyncio.sleep(duration / 12)


# The function that returns the characters representing the indexes in the spinner.
def __loaderSpinner__(index: int):
    temp = index % 4
    return processStyle("|" if temp == 0 else "/" if temp == 1 else "-" if temp == 2 else "\\", 'aqua', 'bold')


#I just wanted to make stuff look cooler since we don't have the time to make fabulous UI
# ansi color codes for the color parameter in processStyle()
color = {
    'red': '\033[31m',
    'blue': '\033[34m',
    'aqua': '\033[36m',
    'green': '\033[32m',
    'dark_green': '\033[38;5;2m',
    'yellow': '\033[33m',
    'orange': '\033[38;5;202m',
    'purple': '\033[35m',
    'light_purple': '\033[38;5;93m',
    'dark_purple': '\033[38;5;54m',
    'gray': '\033[37m',
    'light_gray': '\033[38;5;250m',
    'dark_blue': '\033[38;5;18m'
}

# ansi style codes for the style parameter in processStyle()
style = {
    'bold': '\033[1m',
    'italic': '\033[3m',
    'underlined': '\033[4m'
}


# Takes in a string, processes it into a colored or style formatted string, then returns it
def processStyle(content: str, color_name=None, style_name=None):
    color_code = color[color_name] if color_name else ''
    style_code = style[style_name] if style_name else ''
    # Reset code
    reset = '\033[0m'
    return f"{color_code}{style_code}{content}{reset}"


# Unused function that obfuscates the text, but was never used
def obfuscate(text):
    return ''.join(random.choice(string.printable) for _ in text)


# Unused Code

# I deleted this because this was extremely experimental
# def print_obfuscated(text):
#     obfuscated = obfuscate(text)
#     print(obfuscated, end='\r')
#     sys.stdout.flush()
#     time.sleep(1)
#
#     revealed = list(obfuscated)
#     for i in range(len(text)):
#         revealed[i] = text[i]
#         print(''.join(revealed), end='\r')
#         sys.stdout.flush()
#         time.sleep(0.5)  # Adjust this to change the speed of revealing