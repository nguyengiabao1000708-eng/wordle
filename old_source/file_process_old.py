# pre = "../data/words_data/"
# valid_words_n = "../data/words_data/valid_word_with_length_n.txt"
# words_n = "../data/words_data/word_with_length_n.txt"

import os

# 1. Lấy đường dẫn tuyệt đối đến thư mục chứa file hiện tại (old_source)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Đi lên một cấp để vào thư mục gốc 'wordle' rồi vào 'data/words_data'
# os.path.join sẽ tự động xử lý dấu gạch chéo cho đúng hệ điều hành (Win/Linux)
base_data_path = os.path.join(current_dir, "..", "data", "words_data")

# 3. Định nghĩa lại các đường dẫn
pre = base_data_path + "/"
valid_words_n = os.path.join(base_data_path, "valid_word_with_length_n.txt")
words_n = os.path.join(base_data_path, "word_with_length_n.txt")

def choose_file(n,file_input,file_output):
    valid_word =[]
    with open (file_input, "r") as common_wf:
        for i in common_wf :
            i = i.strip().upper()
            if len(i) == n:
                valid_word.append(i)

    with open(file_output, "w") as valid_wf:
        valid_wf.write("\n".join(valid_word))

def default():
    choose_file(5, pre + "common_words_eng.txt",valid_words_n)
    choose_file(5, pre + "all_words_eng.txt",words_n)
    
def main():
    while True:
        language = input("vietnamese/english/math: ").lower()
        if language == "vietnamese":
            n = int(input("Chooose the word's length: "))   
            choose_file(n, pre + "common_words_vn.txt", valid_words_n)
            choose_file(n, pre + "all_words_vn.txt", words_n)
            break
        elif language == "english":
            n = int(input("Chooose the word's length: ")) 
            choose_file(n, pre + "common_words_eng.txt", valid_words_n)
            choose_file(n, pre + "all_words_eng.txt", words_n)
            break
        elif language == "math":
            n = int(input("Chooose the equation length: "))
            choose_file(n, pre + "math.txt", valid_words_n)
            break
        else:
            print("Unvalid, please type again!!")


# words = []
# with open("vi_dictionary.csv", "r") as f:
#     line = f.readlines()
#     print(len(line))
#     for i in line:
#         i = i.strip().split(",")
#         words.append(i[0])
#     print(words)
# with open("word_with_length_n.txt", "w") as wf:
#     for i in words:
#         wf.write(f"{i}\n")




