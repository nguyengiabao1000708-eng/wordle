
class Letter_state:
    def __init__(self, char):
        self.character = char
        self.right_position = False
        self.right_letter = False

    def __repr__(self):
        # Định nghĩa các mã màu ANSI
        GREEN = '\033[32m' # Đúng vị trí
        YELLOW = '\033[33m' # Đúng chữ, sai vị trí
        WHITE = "\033[37m" # Sai hoàn toàn
        RESET = '\033[0m'
        result =[]
        # if self.right_position == True and self.right_letter == True:
        #     return (f"{GREEN}{self.character}{RESET}")
        # elif self.right_position == False and self.right_letter == True:
        #     return (f"{YELLOW}{self.character}{RESET}")
        # else:
        #     return (f"{WHITE}{self.character}{RESET}")
        if self.right_position == True:
            return (f"{GREEN}{self.character}{RESET}")
        elif self.right_letter == True:
            return (f"{YELLOW}{self.character}{RESET}")
        else:
            return (f"{WHITE}{self.character}{RESET}")
         