import streamlit as st

import pyshorteners

def main():

    # Set page title and configure layout

    st.set_page_config(page_title="Link Shortener", layout="centered")

    

    # Set custom CSS styles

    st.markdown("""

        <style>

        .stButton>button {

            background-color: #4CAF50;

            color: white;

            font-weight: bold;

            padding: 8px 16px;

            border: none;

            border-radius: 4px;

            cursor: pointer;

        }

        .stTextInput>div>div>input {

            border-radius: 4px;

            border: 1px solid #ccc;

            padding: 8px 12px;

            width: 100%;

        }

        </style>

    """, unsafe_allow_html=True)

    # Set page title and description

    st.title("Link Shortener")

    st.write("Enter a URL below to shorten it:")

    # User input

    url = st.text_input("URL", "")

    # Shorten the URL

    if st.button("Shorten"):

        if url:

            shortener = pyshorteners.Shortener()

            short_url = shortener.tinyurl.short(url)

            st.success(f"Shortened URL: {short_url}")

        else:

            st.warning("Please enter a valid URL.")

if __name__ == "__main__":

    main()

