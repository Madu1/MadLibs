# string concatenation (aka how to put strings together)
# ex: we wanna create a string that says "subscribe to + __"
# youtuber = "Traditional Me"
# print(f"subscribe to {youtuber}")
from colorama import Fore, Back, Style

madlib_show = f"Among all the ____ and ____ of heaven, there was one\n"\
            f"famous laughing stock of the three _____.\n\n "\
            f"Legends have it that, eight ______ years ago, there was an \n ancient kingdom in the midlands called " \
            f"the kingdom of _____. \n"

print(madlib_show)

noun1 = input("Noun:")
noun2 = input("Noun:")
noun3 = input("Noun:")
noun4 = input("Noun:")
noun5 = input("Noun:")


mad_libs = f"Among all the {Fore.BLUE}{noun1}{Fore.WHITE} and {Fore.BLUE}{noun2}{Fore.WHITE} of heaven, there was one\n" \
             f"famous laughing stock of the three {Fore.BLUE}{noun3}.\n\n {Fore.WHITE}Legends have it that, eight{Fore.BLUE} {noun4}{Fore.WHITE} years ago, there was " \
             f"an \n ancient kingdom in the midlands called the kingdom of{Fore.BLUE} {noun5}."


print(mad_libs)

