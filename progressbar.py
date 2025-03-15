# Progress bar module for import to your command line project, simply feed it the precent during a loading loop
EMPTY_CHAR = "*"
FULL_CHAR = "="
HEAD_CHAR = ">"

class ProgressBar:
    def __init__(empty_char = EMPTY_CHAR, full_char = FULL_CHAR, head_char = HEAD_CHAR):
        self.empty_char = empty_char
        self.full_char = full_char
        self.head_char = head_char

    def display(self, precent):
        pass
