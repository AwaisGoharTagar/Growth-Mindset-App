import streamlit as st
import random

# Custom CSS for styling
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            color: #FF4500;
            font-size: 16px;
            font-weight: bold;
            padding-top: 20px;
        }
        .highlight {
            font-size: 20px;
            font-weight: bold;
            color: #007ACC;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Motivational Messages
messages = [
    "Believe in yourself — every failure is a step closer to success.",
    "Growth happens outside of your comfort zone. Keep pushing!",
    "Success is not final, failure is not fatal: it’s the courage to continue that counts.",
    "Be patient with progress. Small steps lead to big changes.",
    "Learn from criticism — feedback is fuel for growth.",
    "Surround yourself with positivity and people who inspire you.",
    "Every day is a chance to become a better version of yourself.",
    "Embrace mistakes — they are proof that you’re learning."
]

# Streamlit UI
st.title("🌟 Growth Mindset App")
st.markdown("---")
st.image("https://www.w3schools.com/w3images/fjords.jpg", caption="Unlock Your Potential 🚀")

st.markdown("---")
st.write("Welcome to your personal growth mindset coach! Click the button to receive motivation and actionable growth tips.")

# Preserve message after button click
if "message" not in st.session_state:
    st.session_state.message = ""

if st.button("Get Inspired!"):
    st.session_state.message = random.choice(messages)

if st.session_state.message:
    st.success(f"💬 *{st.session_state.message}*")

    st.subheader("Action Steps for Growth")
    st.markdown("<div class='highlight'>Here are some steps to build a growth mindset:</div>", unsafe_allow_html=True)
    st.write("- Reflect on a recent challenge and write down what you learned.")
    st.write("- Set one small, achievable goal for today.")
    st.write("- Practice gratitude by listing three things you’re thankful for.")
    st.write("- Take a break and do something that sparks creativity (like journaling or drawing).")
 
import streamlit as st

# Growth Journal Feature (Manual Save with Individual Remove Option)
st.subheader("📖 Growth Journal")

if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

journal_entry = st.text_area("Write about a challenge you overcame today:")

if st.button("Save Entry"):
    if journal_entry:
        st.session_state.journal_entries.append(journal_entry)
        st.success("✅ Your entry has been saved. Keep growing!")

# Show previous journal entries with individual remove buttons
if st.session_state.journal_entries:
    st.subheader("📜 Your Journal Entries")
    updated_entries = []

    for index, entry in enumerate(st.session_state.journal_entries):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"📌 {entry}")
        with col2:
            if st.button("❌", key=f"remove_{index}"):
                st.session_state.journal_entries.pop(index)
                st.rerun()  # Refresh UI to update the list




st.markdown("---")
st.markdown("<div class='footer'>Developed by <strong>Awais Gohar Tagar</strong> | 🚀 Keep growing!</div>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; font-size: 18px; font-weight: bold;'>"
    "Remember: Growth is a continuous process, and every step counts. 🚀"
    "</div>",
    unsafe_allow_html=True
)




# import streamlit as st
# import random

# # Custom CSS
# st.markdown(
#     """
#     <style>
#         .footer {
#             text-align: center;
#             color: #FF4500;
#             font-size: 16px;
#             font-weight: bold;
#             padding-top: 20px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Motivational Messages
# messages = [
#     "Believe in yourself — every failure is a step closer to success.",
#     "Growth happens outside of your comfort zone. Keep pushing!",
#     "Success is not final, failure is not fatal: it’s the courage to continue that counts.",
#     "Be patient with progress. Small steps lead to big changes.",
#     "Learn from criticism — feedback is fuel for growth.",
#     "Surround yourself with positivity and people who inspire you.",
#     "Every day is a chance to become a better version of yourself.",
#     "Embrace mistakes — they are proof that you’re learning."
# ]

# # Streamlit UI
# st.title("🌟 Growth Mindset App")
# st.markdown("---")
# st.image("https://www.w3schools.com/w3images/lights.jpg", caption="Unlock Your Potential 🚀")

# st.markdown("---")
# st.write("Welcome to your personal growth mindset coach! Click the button to receive motivation and actionable growth tips.")

# # Preserve message after button click
# if "message" not in st.session_state:
#     st.session_state.message = ""

# if st.button("Get Inspired!"):
#     st.session_state.message = random.choice(messages)

# if st.session_state.message:
#     st.success(f"💬 *{st.session_state.message}*")

#     st.subheader("Action Steps for Growth")
#     st.write("- Reflect on a recent challenge and write down what you learned.")
#     st.write("- Set one small, achievable goal for today.")
#     st.write("- Practice gratitude by listing three things you’re thankful for.")
#     st.write("- Take a break and do something that sparks creativity (like journaling or drawing).")

# # Growth Journal Feature
# st.subheader("📖 Growth Journal")
# journal_entry = st.text_area("Write about a challenge you overcame today:")
# if st.button("Save Entry"):
#     st.success("✅ Your entry has been saved. Keep growing!")

# st.markdown("---")
# st.markdown("<div class='footer'>Developed by <strong>Awais Gohar Tagar</strong> | 🚀 Keep growing!</div>", unsafe_allow_html=True)
# st.write("Remember: Growth is a continuous process, and every step counts. 🚀" )
