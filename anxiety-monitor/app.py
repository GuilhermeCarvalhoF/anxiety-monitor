import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime

# In the future openai will be used to generate suggestions

#############
### STREAMLIT
#############

st.set_page_config(page_title="Anxiety Monitor", page_icon=":brain:", layout="centered")

st.title("Anxiety Monitor")

st.markdown("Welcome to the Anxiety Monitor! This app is designed to help you track your anxiety levels over time. ")

st.subheader("Over the last 2 weeks, how often have you been bothered by any of the following problems?")

st.markdown("""
    - **Not at all** = 0
    - **Several days** = 1
    - **More than half the days** = 2
    - **Nearly every day** = 3
""")

#############
### QUESTIONS
#############

questions = [
    "Feeling nervous, anxious, or on edge?",
    "Not being able to stop or control worrying?",
    "Worrying too much about different things?",
    "Trouble relaxing?",
    "Being so restless that it's hard to sit still?",
    "Becoming easily annoyed or irritable?",
    "Feeling afraid as if something awful might happen?"
]

responses = []
for question in questions:
    response = st.slider(question, 0, 3, 0, format="%d") # The escale is set from 1 to 3 where one is "not at all" and three is "nearly everyday"
    responses.append(response)

######################
### ANXIETY CALCULATOR
######################

def calculate_anxiety_score(responses):
    score = np.sum(responses)

    ### SCALING RESPONSES IN PERCENTAGE

    return score

anxiety_score = calculate_anxiety_score(responses)

##########################
### ANXIETY SCORE FEEDBACK
##########################

def get_anxiety_feedback(score):
    if score <= 4:
        return "🟢 Minimal Anxiety", "Your anxiety levels are minimal. Keep up the great work!"
    elif 5 <= score <= 9:
        return "🟡 Mild Anxiety", "Your anxiety levels are mild. Consider adopting some relaxation techniques to maintain balance."
    elif 10 <= score <= 14:
        return "🟠 Moderate Anxiety", "Your anxiety levels are moderate. You might benefit from exploring deeper relaxation or stress management techniques."
    elif 15 <= score <= 21:
        return "🔴 Severe Anxiety", "Your anxiety levels are quite high. It's important to consider speaking with a professional for guidance."


label, advice = get_anxiety_feedback(anxiety_score)


##################
### DISPLAY RESULT
##################

st.subheader("Your Anxiety Score:")
st.markdown(f"**{anxiety_score}%**")
st.markdown(f"**{label}**")

st.subheader("Personalized Advice:")
st.markdown(advice)

##########
#
# THIS SECTION FOR THE ADVICES WILL BE REPLACED BY OPENAI API
#
##########


###############
### SAVE ON PDF
###############

if st.button("Save my results"):
    result = {
        "Timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Anxiety Score" : anxiety_score,
        "Feedback" : label,
        "Advice" : advice
    }

    results_df = pd.DataFrame([result])
    results_df.to_csv("anxiety_results.csv", mode="a", header=False, index=False)
    st.success("Your results have been saved")
