import streamlit as st
import pandas as pd
from algorithms import fifo_page_replacement, lru_page_replacement, lfu_page_replacement, mfu_page_replacement

st.title("Page Replacement Algorithms")

# User Input
pages_input = st.text_input("Enter Page Reference String (comma-separated):", "7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2")
frames = st.number_input("Number of Frames:", min_value=1, max_value=10, value=3)
algorithm = st.selectbox("Select Algorithm:", ["FIFO", "LRU", "LFU", "MFU"])

# Convert input string to list of integers
pages = list(map(int, pages_input.split(',')))

# Initialize a dictionary to store the results of each algorithm
algorithm_results = {
    "FIFO": None,
    "LRU": None,
    "LFU": None,
    "MFU": None
}

# Run all algorithms when the button is clicked
if st.button("Run Algorithm"):
    # FIFO
    fifo_faults, fifo_steps = fifo_page_replacement(pages, frames)
    algorithm_results["FIFO"] = fifo_faults
    
    # LRU
    lru_faults, lru_steps = lru_page_replacement(pages, frames)
    algorithm_results["LRU"] = lru_faults
    
    # LFU
    lfu_faults, lfu_steps = lfu_page_replacement(pages, frames)
    algorithm_results["LFU"] = lfu_faults
    
    # MFU
    mfu_faults, mfu_steps = mfu_page_replacement(pages, frames)
    algorithm_results["MFU"] = mfu_faults

    # Show the detailed steps for the selected algorithm
    if algorithm == "FIFO":
        df = pd.DataFrame(fifo_steps, columns=[f"Frame {i+1}" for i in range(frames)])
        df.insert(0, "Page", pages)
        st.write("### Memory State (FIFO)")
        st.dataframe(df.transpose())
    
    elif algorithm == "LRU":
        df = pd.DataFrame(lru_steps, columns=[f"Frame {i+1}" for i in range(frames)])
        df.insert(0, "Page", pages)
        st.write("### Memory State (LRU)")
        st.dataframe(df.transpose())
    
    elif algorithm == "LFU":
        df = pd.DataFrame(lfu_steps, columns=[f"Frame {i+1}" for i in range(frames)])
        df.insert(0, "Page", pages)
        st.write("### Memory State (LFU)")
        st.dataframe(df.transpose())
    
    elif algorithm == "MFU":
        df = pd.DataFrame(mfu_steps, columns=[f"Frame {i+1}" for i in range(frames)])
        df.insert(0, "Page", pages)
        st.write("### Memory State (MFU)")
        st.dataframe(df.transpose())

    # Create the comparison table
    comparison_df = pd.DataFrame(list(algorithm_results.items()), columns=["Algorithm", "Page Faults"])
    st.write("### Comparison of Page Faults")
    st.dataframe(comparison_df)

