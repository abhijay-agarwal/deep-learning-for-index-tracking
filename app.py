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


# sidebar


def cs_sidebar():
    st.sidebar.header("Streamlit cheat sheet")
    st.sidebar.code("$ pip install streamlit")

    return None


##########################
# Main body of app
##########################


def cs_body():
    # Magic commands

    col1, col2, col3 = st.columns(3)

    col1.subheader("Magic commands")
    col1.code("""hello""")

    col2.subheader("Control flow")
    col2.code("""hello""")

    col3.subheader("Mutate data")
    col3.code("""hello""")

    return None


# Run main()

if __name__ == "__main__":
    main()
