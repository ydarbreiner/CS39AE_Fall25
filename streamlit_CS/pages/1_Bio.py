import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Brady Reiner"
PROGRAM = "Computer Science"
INTRO = (
    "Hi! I am finishing up my Bachelors of Science in Computer Science at MSU Denver."
    "I am very interested and involved in Data Science and Machine Learning. I am interested in Data Visualization because it will help me in undertsanding and working with the data I already collect outside of school."
)
FUN_FACTS = [
    "I love being outdoors usually rock climbing, hiking, or skiing.",
    "I’m learning how to use Computer Science to solve real world problems",
    "I want to use technology to help people and improve everyones quality of life.",
]
PHOTO_PATH = "assets/IMG_2929-2.jpg"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
