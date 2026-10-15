import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import random
import streamlit as st

st.set_page_config(
    page_title="Scottish Fold Club",
    page_icon="🐱"
)

st.title("🎀 Scottish Fold Club 🎀")
st.write("A little corner of the internet for cat lovers.")

facts = [
    "Scottish Fold cats originated in Scotland! 🏴",
    "They can have short or long coats.",
    "Not every Scottish Fold has folded ears!",
    "Their folded-ear gene can cause joint problems."
]

st.header("🐾 Cat Facts")
if st.button("Give me a random fact!"):
    st.success(random.choice(facts))

st.header("💌 A message for you")
messages = [
    "You're pawsome! 🐾",
    "Sending you a little purr of happiness! 💗",
    "Have a meow-gical day! 🐱"
]

if st.button("Get a cute message"):
    st.info(random.choice(messages))

st.header("🐱 Cat Quiz")
answer = st.radio(
    "Where did Scottish Fold cats originate?",
    ["Japan", "Scotland", "France"],
    index=None
)

if st.button("Check answer"):
    if answer == "Scotland":
        st.success("Correct! You're a cat expert! 🎉")
    elif answer is None:
        st.warning("Choose an answer first!")
    else:
        st.error("Not quite! Try again. 💕")

st.caption("Made with love 🎀")
