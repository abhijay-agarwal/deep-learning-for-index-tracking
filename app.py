"""
Streamlit Cheat Sheet

App to summarise streamlit docs v1.8.0

There is also an accompanying png and pdf version

https://github.com/daniellewisDL/streamlit-cheat-sheet

v1.8.0 October 2021

Author:
    @daniellewisDL : https://github.com/daniellewisDL

Contributors:
    @arnaudmiribel : https://github.com/arnaudmiribel
    @akrolsmir : https://github.com/akrolsmir
    @nathancarter : https://github.com/nathancarter

"""

import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
    page_title="Streamlit cheat sheet",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    cs_sidebar()
    cs_body()

    return None


# Thanks to streamlitopedia for the following code snippet


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# sidebar


def cs_sidebar():
    st.sidebar.header("Streamlit cheat sheet")

    return None


##########################
# Main body of cheat sheet
##########################


def cs_body():
    # Magic commands

    col1, col2, col3 = st.columns(3)

    col1.subheader("Magic commands")

    col2.subheader("Control flow")

    col3.subheader("Mutate data")

    return None


# Run main()

if __name__ == "__main__":
    main()
