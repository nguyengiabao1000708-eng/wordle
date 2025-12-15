word = []
valid_word =[]
all_word = word + valid_word
n = int(input())
with open ("5000_common_words.txt", "r") as common_wf:
    for i in common_wf :
        i = i.strip().upper()
        if len(i) == n:
            valid_word.append(i)

with open("valid_word_with_length_n.txt", "w") as valid_wf:
    valid_wf.write("\n".join(valid_word))

with open ("words_alpha.txt", "r") as alpha_wf:
    for i in alpha_wf :
        i = i.strip().upper()
        if len(i) == n:
            word.append(i)

with open("word_with_length_n.txt", "w") as all_wf:
    all_wf.write("\n".join(word))



