import streamlit as st
import random
from user_manager import UserManager
from wordle_logic_streamlit import Wordle
import data_words.file_process as f

st.set_page_config(page_title="Wordle HCMUS", layout="centered")

def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style.css")

def get_random_word(file_path):
    try:
        with open(file_path, "r") as file:
            word_list = file.readlines()
        if not word_list: return None
        return random.choice(word_list).strip().upper()
    except FileNotFoundError:
        st.error(f"Không tìm thấy file: {file_path}")
        return None

def check_valid_words(word, file_path):
    try:
        with open(file_path, "r") as file:
            word_list = {line.strip().upper() for line in file}
        return word in word_list
    except FileNotFoundError:
        return False
    
def render_wordle_board(attempts, wordle):
    board_html = "<div class= 'wordle-grid'>"

    for guess in attempts:
        board_html += "<div class= 'wordle-row'>"
        statuses = wordle.get_guess_statuses(guess)
        
        for i, char in enumerate(guess):
            board_html += f'<div class="tile {statuses[i]}">{char}</div>'
        board_html += '</div>'

    for _ in range (wordle.attempts_remaining()):
        board_html += '<div class="wordle-row">'
        for _ in range(5):
            # Bạn có thể thêm class .tile-empty vào CSS nếu muốn viền nhạt hơn
            board_html += '<div class="tile"></div>'
        board_html += '</div>'

    board_html += '</div>' # Đóng wordle-grid
    st.markdown(board_html, unsafe_allow_html=True)

def already_guessed(guess, wordle):
    return guess in wordle.attempts


# 1. Khởi tạo Session State
if "wordle" not in st.session_state:
    st.session_state.wordle = Wordle(get_random_word("data_words/valid_word_with_length_n.txt"))
    st.session_state.game_over = False
    st.session_state.is_win = False


wordle = st.session_state.wordle
target = wordle.secret

st.title("Wordle Minimalist")

st.write(f"the word is {target}")

render_wordle_board(wordle.attempts, wordle)


if not st.session_state.game_over:
    guess = st.text_input("Guess the word: ", max_chars = 5).upper()
    
    if st.button("enter"):
        if len(guess) < 5:
            st.warning("Vui lòng nhập đủ 5 chữ cái!")
        elif already_guessed(guess,wordle):
            st.warning("Từ này đã được đoán!")
        elif not check_valid_words(guess,"data_words/word_with_length_n.txt"):
            st.warning("Từ không tồn tại")
        else:
            wordle.attempts.append(guess)
            if guess == target:
                st.session_state.game_over = True
                st.session_state.is_win = True
            elif wordle.attempts_remaining() ==0 :

                st.session_state.game_over = True
            st.rerun()  

else:
    if st.session_state.is_win:
        st.success("You win")
    else:
        st.warning("you lose")

    if st.button("Restart Game"):
        del st.session_state.is_win
        del st.session_state.wordle
        del st.session_state.game_over
        st.rerun()





 








