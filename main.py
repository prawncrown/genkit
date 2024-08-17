import streamlit as st
import time

class CounterState:
    def __init__(self):
        self.count = 0

@st.cache_resource
def get_counter_state():
    return CounterState()

def increment_count():
    counter_state = get_counter_state()
    counter_state.count += 1

def reset_count():
    counter_state = get_counter_state()
    counter_state.count = 0

@st.fragment(run_every="1s")
def auto_function():
	# This will update every 10 seconds!
    counter_state = get_counter_state()
    st.write(f"Button clicked: {counter_state.count} times")

def main():
    st.title("カウンターの遊び")
    auto_function()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Click me!"):
            increment_count()

    with col2:
        if st.button("Reset Counter"):
            reset_count()

if __name__ == "__main__":
    main()