from source import UserManager
import streamlit as st


def navigation():
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        if st.button("Trang chủ", icon= "🏠", use_container_width=True):
            st.switch_page("demo_streamlit.py")
    with col2:
        if st.button("Thông số người chơi", icon= "📈", use_container_width=True):
            st.switch_page("pages/player_stats.py")

    with col3:
        if st.button("Bảng xếp hạng", icon= "📉", use_container_width=True):
            st.switch_page("pages/ranking.py")


navigation()

username = st.session_state.get("username")
game_over = st.session_state.get("game_over")
is_win = st.session_state.get("is_win")

status = False
if game_over == True and is_win == True:
    status = True

st.set_page_config(page_title="Player Statistics", layout="centered")
st.title("Thống kê người chơi")
st.write(f"Username: {username}")

user_manager = UserManager()
user_manager.load_data()
user_manager.get_player(username)

user = user_manager.get_player(username)

st.write("Số trận đã chơi:", user.games_played)
st.write("Tổng số trận thắng:", user.total_wins)
st.write("Chuỗi thắng hiện tại:", user.cur_streak)
st.write("Chuỗi thắng dài nhất:", user.best_streak)
