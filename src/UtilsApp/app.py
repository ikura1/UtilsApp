from pathlib import Path

import streamlit as st

dir_path = Path(__file__).parent


def run():
    page = st.navigation(
        [
            st.Page("pages/hello.py", title="Hello"),
        ]
    )
    page.run()


if __name__ == "__main__":
    run()
