# Importing Colorama module in python
import colorama
# Importing Fore, Back, Style
from colorama import Fore, Back, Style
# Here Fore is used for the text color, Back is used for Background color and Style is used for style of the text.
colorama.init(autoreset=True)
# Using the above three command printing the coloured text.
print(Fore.BLUE+Back.YELLOW+"Hi, My name is Shubham Dubey "+ Fore.YELLOW+ Back.GREEN+"I am learning Machine Learning Algorithms.")
print(Back.CYAN+"I love coding.")
print(Fore.YELLOW + Back.BLACK+ "Coding is now my new hobby.")

