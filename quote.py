import streamlit as st
import requests
import random

# Function to get a random quote from Quotable API
def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return {"quote": data['content'], "author": data['author']}
    else:
        return None

# Function to get a random quote by Donald Trump (from a hypothetical Trump Quotes API)
def get_trump_quote():
    # Hypothetical API for Trump quotes (replace this with a real API if available)
    response = requests.get("https://trump-quote-api.com/random")
    if response.status_code == 200:
        data = response.json()
        return {"quote": data['quote'], "author": "Donald Trump"}
    else:
        return None

# Function to randomly choose between fetching a Trump quote or a random quote
def get_random_or_trump_quote():
    if random.random() < 0.5:
        return get_trump_quote()
    else:
        return get_random_quote()

# Initial setup for state management
if "quote_data" not in st.session_state:
    st.session_state.quote_data = get_random_or_trump_quote()
    st.session_state.show_result = False

# Title of the app
st.title("Guess the Quote")

# Display the quote
if st.session_state.quote_data:
    st.write(f'Quote: "{st.session_state.quote_data["quote"]}"')
else:
    st.write("Failed to retrieve a quote.")

# Options to guess
guess = st.radio("Who said this?", ("Donald Trump", "Someone Else"))

# Button to check answer
if st.button("Submit Guess"):
    st.session_state.show_result = True
    # Check if the guess is correct by comparing the actual author, not the fake author
    if (guess == "Donald Trump" and st.session_state.quote_data["author"] == "Donald Trump") or \
       (guess == "Someone Else" and st.session_state.quote_data["author"] != "Donald Trump"):
        st.success("Correct!")
    else:
        st.error(f"Wrong! The quote was actually said by {st.session_state.quote_data['author']}")

# Option to get a new quote
if st.session_state.show_result:
    if st.button("New Quote"):
        st.session_state.quote_data = get_random_or_trump_quote()
        st.session_state.show_result = False

