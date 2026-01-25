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

user_manager = UserManager()
user_manager.load_data()
st.set_page_config(page_title="Ranking", layout="centered")
st.title("Bảng xếp hạng người chơi")
ranking = user_manager.ranking_total_games()
if ranking:
    for i, (username, games_played) in enumerate (ranking, start=1):
        st.write(f"{i}. {username}  ---  Số trận đã chơi: {games_played}")