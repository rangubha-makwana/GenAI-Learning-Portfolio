import streamlit as st
import pandas as pd
import numpy as np



# Title of  the Application
st.title("Hello Worlds")

# Display the simple Text
st.write("This is the simple text")


## create a simple dataframe
df = pd.DataFrame({
    "first_column": [1,2,3,4,5,6],
    "second_column": [11,22,33,44,55,66]
    })

# Display here dataframe
st.write("Here is my dataframe")
st.write(df)


## create a line chart here
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=["A", "B", "C"]
)

st.line_chart(chart_data)

# https://www.cloudskillsboost.google/public_profiles/9a27d08f-1b9c-4491-8bff-a910df534053