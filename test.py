with open("data/valid_word_with_length_n.txt","r") as f:
    word_list = []
    print(word_list)
    for i in f:
        print(i)
    #     word_list.append(i.strip())
    # print(word_list)


# import random
# def words(file):
#     with open(file,"r") as f:
#         word_list = f.readlines()
    
#     if not word_list:
#         print("Lỗi: File rỗng, không có từ nào để chọn.")
#         return None

#     random_line = random.choice(word_list)
#     selected_word = random_line.strip().upper()

#     return selected_word


# def check_valid_words(word,file):
#     with open(file,"r") as f:
#         word_list = f.readlines()

#     for i in word_list:
#         print(i.strip())
    
#     if word not in word_list:
#         return False
#     else:
#         return True
# guess =input()    
# print(words("data/valid_word_with_length_n.txt"))
# if check_valid_words(guess,"data/word_with_length_n.txt") == False:
#     print("NGU")
