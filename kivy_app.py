import streamlit as st

st.title("Interactive Mental Health Self-Assessment")

# Define questions
questions = [
    {
        "question": "How is your overall mood today?",
        "type": "slider",
        "min": 0,
        "max": 10,
        "key": "mood",
        "correct": "higher",  # higher score = better wellness
        "points_map": lambda val: val
    },
    {
        "question": "Do you have thoughts of self-harm or suicide?",
        "type": "radio",
        "options": ["Never", "Sometimes", "Often"],
        "key": "suicide",
        "correct": "Never",
        "points_map": {"Never": 5, "Sometimes": 2, "Often": 0}
    },
    {
        "question": "How do you usually respond to stress?",
        "type": "radio",
        "options": ["Calmly", "Irritably", "Avoidant", "Panic"],
        "key": "stress",
        "correct": "Calmly",
        "points_map": {"Calmly": 5, "Irritably": 2, "Avoidant": 3, "Panic": 1}
    },
    {
        "question": "Imagine you are driving a car and someone cuts you off. How do you react?",
        "type": "textarea",
        "key": "car_reaction",
        "correct": "Calm",
        "points_map": lambda text: 5 if "calm" in text.lower() else 2
    },
]

responses = {}
points = {}
current_step = st.session_state.get("step", 0)

# Show current question
q = questions[current_step]

st.subheader(f"Question {current_step+1}/{len(questions)}")
st.write(q["question"])

if q["type"] == "slider":
    answer = st.slider("", min_value=q["min"], max_value=q["max"], key=q["key"])
elif q["type"] == "radio":
    answer = st.radio("", q["options"], key=q["key"])
elif q["type"] == "textarea":
    answer = st.text_area("", key=q["key"])

# Compute points
if callable(q["points_map"]):
    points[q["key"]] = q["points_map"](answer)
elif isinstance(q["points_map"], dict):
    points[q["key"]] = q["points_map"].get(answer, 0)
else:
    points[q["key"]] = 0

# Next button
if st.button("Next"):
    responses[q["key"]] = answer
    current_step += 1
    st.session_state["step"] = current_step
    st.experimental_rerun()

# Show results if last step reached
if current_step >= len(questions):
    total_score = sum(points.values())
    st.success(f"Assessment Complete! Your total score: {total_score}/{len(questions)*5}")

    st.subheader("Detailed Feedback")
    for q in questions:
        st.write(f"**{q['question']}**")
        st.write(f"Your answer: {responses.get(q['key'], '')}")
        if "correct" in q:
            st.write(f"Recommended answer: {q['correct']}")
        st.write(f"Points: {points[q['key']]}")
        st.write("---")

    # Interpretation
    if total_score >= 18:
        st.success("Your mental wellness appears good. Keep practicing healthy habits!")
    elif total_score >= 10:
        st.warning("Some areas may need attention. Consider stress management strategies.")
    else:
        st.error("High risk detected. Please seek professional support immediately.")
