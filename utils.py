class Automator:
    def __init__(self):
        print "init automator"
    def __str__(self):
        print ""


class Color:
    RED = "\x1b[31;1m"
    YELLOW = "\x1b[33;1m"
    GREEN = "\x1b[32;1m"
    MAGENTA = "\x1b[35;1m"

    @staticmethod
    def set(color, s):
        return color + s + "\x1b[0m"
