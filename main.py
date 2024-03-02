import streamlit as st
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter

    return end_text


def main():
    st.set_page_config(
        page_title="Caesar Cipher Encoder/Decoder",
        page_icon=":closed_lock_with_key:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Caesar Cipher Encoder/Decoder")
    st.sidebar.image("Caesar.jpeg", width=100)
    st.sidebar.markdown("**Welcome to Caesar Cipher!**")
    st.sidebar.write(logo)

    direction = st.radio("Choose an option:", ('Encode', 'Decode'))
    text = st.text_area("Enter your message:")
    shift = st.number_input("Enter the shift number:", value=0)

    if st.button("Apply Cipher"):
        shift = shift % 26
        result = caesar(start_text=text.lower(), shift_amount=shift, cipher_direction=direction.lower())
        st.success(f"The {direction.lower()}d text is: {result}")

        restart = st.radio("Would you like to encode/decode another message?", ('Yes', 'No'))
        if restart == 'No':
            st.write("Goodbye!")

    st.sidebar.markdown("---")
    st.sidebar.markdown("Created with :heart: by Your Name")

    st.sidebar.markdown(
        """
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YourGitHubProfile)
        """
    )


if __name__ == "__main__":
    main()
