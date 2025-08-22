import streamlit as st

st.title("Mental Health Self-Assessment")
st.write("Answer the following questions honestly to assess your wellness.")

# Define questions
questions = [
    {
        "question": "How is your overall mood today?",
        "type": "slider",
        "min": 0,
        "max": 10,
        "key": "mood",
        "points_map": lambda val: val  # higher mood = higher score
    },
    {
        "question": "How do you usually respond to stress?",
        "type": "radio",
        "options": ["Calmly", "Irritably", "Avoidant", "Panic"],
        "key": "stress",
        "points_map": {"Calmly": 5, "Irritably": 2, "Avoidant": 3, "Panic": 1}
    },
    {
        "question": "Do you have thoughts of self-harm or suicide?",
        "type": "radio",
        "options": ["Never", "Sometimes", "Often"],
        "key": "suicide",
        "points_map": {"Never": 5, "Sometimes": 2, "Often": 0}
    },
    {
        "question": "Imagine you are driving a car and someone cuts you off. How do you react?",
        "type": "textarea",
        "key": "car_reaction",
        "points_map": lambda text: 5 if "calm" in text.lower() else 2
    },
    {
        "question": "How would you describe your anger levels in the past week?",
        "type": "slider",
        "min": 0,
        "max": 10,
        "key": "anger",
        "points_map": lambda val: 10 - val  # lower anger = higher points
    }
]

responses = {}
points = {}

# Render questions
for q in questions:
    if q["type"] == "slider":
        responses[q["key"]] = st.slider(q["question"], min_value=q["min"], max_value=q["max"])
    elif q["type"] == "radio":
        responses[q["key"]] = st.radio(q["question"], q["options"])
    elif q["type"] == "textarea":
        responses[q["key"]] = st.text_area(q["question"])
    
    # Calculate points
    if callable(q["points_map"]):
        points[q["key"]] = q["points_map"](responses[q["key"]])
    elif isinstance(q["points_map"], dict):
        points[q["key"]] = q["points_map"].get(responses[q["key"]], 0)
    else:
        points[q["key"]] = 0

# Submit button
if st.button("Submit Assessment"):
    total_score = sum(points.values())
    st.subheader("Your Assessment Results")
    st.write(f"Total Score: {total_score} / {len(questions)*5}")

    # Interpretation
    if total_score >= 20:
        st.success("Your mental wellness appears good. Keep practicing healthy habits!")
    elif total_score >= 10:
        st.warning("Some areas may need attention. Consider stress management strategies.")
    else:
        st.error("High risk detected. Please seek professional support immediately.")

    # Show detailed feedback per question
    st.subheader("Question-by-Question Feedback")
    for q in questions:
        st.write(f"**{q['question']}**")
        st.write(f"Your answer: {responses[q['key']]}")
        st.write(f"Points: {points[q['key']]}")
        st.write("---")
