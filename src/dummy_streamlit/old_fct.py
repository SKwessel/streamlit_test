import streamlit as st
import pandas as pd

def dummy_button():
    st.write("## Button Example")
    if st.button("Click Me!"):
        st.write("Button clicked!")
    else:
        st.write("Button not clicked yet.")
    

def dummy_plot():

    st.write("""
    # My first app
    Hello *world!*
    """)
    data = {
        'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'Sales': [150, 200, 250, 300, 280]
    }
    df = pd.DataFrame(data)
    st.write("## Sales Data")
    st.line_chart(df, x='Day', y='Sales')