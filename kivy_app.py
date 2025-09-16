# import streamlit as st

# st.title("Interactive Mental Health Self-Assessment")

# # Define questions
# questions = [
#     {
#         "question": "How is your overall mood today?",
#         "type": "slider",
#         "min": 0,
#         "max": 10,
#         "key": "mood",
#         "correct": "higher",  # higher score = better wellness
#         "points_map": lambda val: val
#     },
#     {
#         "question": "Do you have thoughts of self-harm or suicide?",
#         "type": "radio",
#         "options": ["Never", "Sometimes", "Often"],
#         "key": "suicide",
#         "correct": "Never",
#         "points_map": {"Never": 5, "Sometimes": 2, "Often": 0}
#     },
#     {
#         "question": "How do you usually respond to stress?",
#         "type": "radio",
#         "options": ["Calmly", "Irritably", "Avoidant", "Panic"],
#         "key": "stress",
#         "correct": "Calmly",
#         "points_map": {"Calmly": 5, "Irritably": 2, "Avoidant": 3, "Panic": 1}
#     },
#     {
#         "question": "Imagine you are driving a car and someone cuts you off. How do you react?",
#         "type": "textarea",
#         "key": "car_reaction",
#         "correct": "Calm",
#         "points_map": lambda text: 5 if "calm" in text.lower() else 2
#     },
# ]

# responses = {}
# points = {}
# current_step = st.session_state.get("step", 0)

# # Show current question
# q = questions[current_step]

# st.subheader(f"Question {current_step+1}/{len(questions)}")
# st.write(q["question"])

# if q["type"] == "slider":
#     answer = st.slider("", min_value=q["min"], max_value=q["max"], key=q["key"])
# elif q["type"] == "radio":
#     answer = st.radio("", q["options"], key=q["key"])
# elif q["type"] == "textarea":
#     answer = st.text_area("", key=q["key"])

# # Compute points
# if callable(q["points_map"]):
#     points[q["key"]] = q["points_map"](answer)
# elif isinstance(q["points_map"], dict):
#     points[q["key"]] = q["points_map"].get(answer, 0)
# else:
#     points[q["key"]] = 0

# # Next button
# if st.button("Next"):
#     responses[q["key"]] = answer
#     current_step += 1
#     st.session_state["step"] = current_step
#     st.rerun()

# # Show results if last step reached
# if current_step >= len(questions):
#     total_score = sum(points.values())
#     st.success(f"Assessment Complete! Your total score: {total_score}/{len(questions)*5}")

#     st.subheader("Detailed Feedback")
#     for q in questions:
#         st.write(f"**{q['question']}**")
#         st.write(f"Your answer: {responses.get(q['key'], '')}")
#         if "correct" in q:
#             st.write(f"Recommended answer: {q['correct']}")
#         st.write(f"Points: {points[q['key']]}")
#         st.write("---")

#     # Interpretation
#     if total_score >= 18:
#         st.success("Your mental wellness appears good. Keep practicing healthy habits!")
#     elif total_score >= 10:
#         st.warning("Some areas may need attention. Consider stress management strategies.")
#     else:
#         st.error("High risk detected. Please seek professional support immediately.")

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        /* ---------- Cards ---------- */
        .card {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            text-align: center;
            font-size: 18px;
            transition: transform 0.2s ease-in-out;
        }
        .card:hover {
            transform: translateY(-5px);
        }

        /* ---------- Tables ---------- */
        .responsive-table table {
            width: 100% !important;
            border-collapse: collapse;
            font-size: 16px;
        }
        .responsive-table th, .responsive-table td {
            padding: 10px;
            border: 1px solid #ddd;
        }
        .responsive-table th {
            background-color: #0d1b3d;
            color: white;
        }

        /* ---------- Responsive behavior ---------- */
        /* Tablets */
        @media (max-width: 992px) {
            .card {
                font-size: 16px;
                padding: 15px;
            }
            .responsive-table table {
                font-size: 14px;
            }
        }

        /* Phones */
        @media (max-width: 768px) {
            [data-testid="stHorizontalBlock"] {
                flex-direction: row !important; /* keep horizontal */
                gap: 8px !important;
            }
            .card {
                font-size: 14px;
                padding: 10px;
                min-width: 120px;
            }
            .responsive-table table {
                font-size: 13px;
            }
        }

        /* Very small phones */
        @media (max-width: 480px) {
            .card {
                font-size: 12px;
                padding: 8px;
                min-width: 100px;
            }
            .responsive-table table {
                font-size: 12px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---------- DEMO APP ----------

st.title("📱 Responsive Demo App")

# --- Cards Section ---
st.subheader("Cards Section (Responsive)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">📊 <br> Reports</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card">📈 <br> Analytics</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card">📂 <br> Archives</div>', unsafe_allow_html=True)

# --- Table Section ---
st.subheader("Responsive Table Example")
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [24, 30, 28, 35],
    "Department": ["HR", "IT", "Finance", "Marketing"]
}
df = pd.DataFrame(data)

# Render table inside responsive div
st.markdown('<div class="responsive-table">', unsafe_allow_html=True)
st.write(df)
st.markdown('</div>', unsafe_allow_html=True)

# --- Columns with content ---
st.subheader("Text in Columns")
colA, colB = st.columns(2)

with colA:
    st.markdown('<div class="card">This is column A content. On mobile, text resizes to fit properly.</div>', unsafe_allow_html=True)

with colB:
    st.markdown('<div class="card">This is column B content. No need for horizontal scrolling.</div>', unsafe_allow_html=True)

