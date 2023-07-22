import streamlit as st
from pathlib import Path
import base64

# Path: app.py

st.set_page_config(
    page_title="ML for Index Replication",
    layout="wide",
)


def main():
    cs_body()

    return None


def cs_body():
    # Magic commands

    # col1, col2 = st.columns(1)

    # col1.subheader("Magic commands")
    # col1.code(
    #     """# Magic commands implicitly `st.write()`
    #     \'\'\' _This_ is some __Markdown__ \'\'\'
    #     a=3
    #     'dataframe:', data
    #     """
    # )

    st.text("This is some text")

    return None


if __name__ == "__main__":
    main()
