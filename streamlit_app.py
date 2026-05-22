import streamlit as st

st.title("🎈 project kelas A")
import pandas as pd
import streamlit as st

confusion_matrix = pd.DataFrame(
    {
        "Predicted naely": [2, 8, 6, 12],
        "Predicted pai": [9, 1, 8, 7],
        "Predicted dika": [8, 9, 7, 6],
        "Predicted falah": [5, 7, 9, 19],
    },
    index=["Actual naely", "Actual pai", "Actual dika", "Actual falah"],
)
st.table(confusion_matrix)
