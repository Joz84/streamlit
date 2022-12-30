import streamlit as st
import numpy as np
import pandas as pd

#st.write(f'Welcome to my app with key: {st.secrets.key}')
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.sidebar.header("Mapping Demo")
st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

age = st.slider('How old are you?', 0, 10, 3)

# and used to select the displayed lines
head_df = df.head(age)

head_df

st.line_chart(df)