import sys
import random
from pyfiglet import Figlet


figlet = Figlet()


def main(args):
    if set_figlet_font(args):
        render_message()
    else:
        sys.exit("Invalid usage ")


def set_figlet_font(args):
    font_list = figlet.getFonts()
    is_font_set = False
    if len(args) == 1:
        figlet.setFont(font=font_list[random.randint(0, 424)])
        is_font_set = True
    elif len(args) == 3:
        if args[1] == "-f" or args[1] == "--font":
            if args[2] in font_list:
                figlet.setFont(font=args[2])
                is_font_set = True

    return is_font_set


def render_message():
    message = input("Input: ")
    print("Output: ", figlet.renderText(message), sep="\n")


if __name__ == "__main__":
    main(sys.argv)
