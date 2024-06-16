import streamlit as st
from config.navbar import navbar
from config.page_config import page_config
from layout.upload import DatabaseManager, UploadButton
from layout.sidebar import sidebar


def init_session_state():
    if "selected_functionality" not in st.session_state:
        st.session_state["selected_functionality"] = None


def run_app():
    page_config()
    page = navbar()
    init_session_state()

    if page in ["Upload", "Jarvis", "Github", "About"]:
        get_page_content(page)
    else:
        options = sidebar()
        get_page_content(options)


def get_page_content(page):
    if page == "Upload":
        db_mng = DatabaseManager()
        db_mng.connect_to_database()
        selected_table = db_mng.select_table()
        uploadbttn = UploadButton()
        uploadbttn.connect_to_database()
        uploadbttn.upload_button(selected_table)
