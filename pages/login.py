import streamlit as st
from source import UserManager


def sign_up(um):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.container(border=True):
            st.markdown("## SIGN UP WORDLE")
            with st.form("sign_up_form"):
                username = st.text_input("Username", max_chars=10, placeholder="a-z, A-Z, 0-9 only")
                password = st.text_input("Password", type="password", max_chars=10, placeholder="a-z, A-Z, 0-9 only")
                confirm_password = st.text_input("Confirm Password", max_chars=10, type="password", placeholder="a-z, A-Z, 0-9 only")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    if um.player_is_exist(username):
                        st.error("Username already exists. Please choose a different username.")
                    else:
                        if password != confirm_password:
                            st.error("Passwords do not match. Please try again.")
                        else:
                            um.create_new_player(username, password)
                            um.save_data()
                            st.success("Sign up successful! You can now log in.")


def sign_in(um):
    with st.form("login_form"):
        username = st.text_input("Username", max_chars=10, placeholder="a-z, A-Z, 0-9 only")
        password = st.text_input("Password", type="password", max_chars=10, placeholder="a-z, A-Z, 0-9 only")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if um.player_is_exist(username):
                user = um.get_player(username)
                if user.password == password:
                    st.success("Login successful!")
                    st.session_state["username"] = username
                    st.session_state["game_over"] = False
                    st.session_state["is_win"] = False
                    st.switch_page("demo_streamlit.py")
                else:
                    st.error("Incorrect password. Please try again.")
            else:
                st.error("Username does not exist.")

def main():
    st.set_page_config(page_title="Login", layout="centered")

    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "login"

    um = UserManager()
    um.load_data()

    if st.session_state.auth_mode == "login":
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.container(border=True):
                st.markdown("## LOG IN WORDLE")
                sign_in(um)
                st.write("Don't have an account?")

                if st.button("Sign Up"):
                    st.session_state.auth_mode = "signup"
                    st.rerun()

    elif st.session_state.auth_mode == "signup":
        sign_up(um)
        if st.button("Back to Login"):
            st.session_state.auth_mode = "login"
            st.rerun()

if __name__ == "__main__":
    main()