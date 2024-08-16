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

# Possible "correct" authors, including Donald Trump and Crazy Guy
fake_authors = ["Donald Trump", "Crazy Guy"]

# Function to label authors randomly as either Donald Trump or Crazy Guy
def assign_fake_author(author_name):
    # 50% chance for Donald Trump, otherwise "Crazy Guy"
    if random.random() < 0.5:
        return "Donald Trump"
    else:
        return "Crazy Guy"

# Function to randomly choose between fetching a Trump quote or a random quote
def get_random_or_trump_quote():
    if random.random() < 0.5:
        return get_trump_quote()
    else:
        return get_random_quote()

# Initial setup for state management
if "quote_data" not in st.session_state:
    st.session_state.quote_data = get_random_or_trump_quote()
    st.session_state.fake_author = assign_fake_author(st.session_state.quote_data["author"])
    st.session_state.show_result = False

# Title of the app
st.title("Guess the Quote")

# Display the quote
if st.session_state.quote_data:
    st.write(f'Quote: "{st.session_state.quote_data["quote"]}"')
else:
    st.write("Failed to retrieve a quote.")

# Options to guess
guess = st.radio("Who said this?", ("Donald Trump", "Crazy Guy"))

# Button to check answer
if st.button("Submit Guess"):
    st.session_state.show_result = True
    if guess == st.session_state.fake_author:
        st.success("Correct!")
    else:
        st.error(f"Wrong! The quote was actually said by {st.session_state.quote_data['author']}")

# Option to get a new quote
if st.session_state.show_result:
    if st.button("New Quote"):
        st.session_state.quote_data = get_random_or_trump_quote()
        st.session_state.fake_author = assign_fake_author(st.session_state.quote_data["author"])
        st.session_state.show_result = False
