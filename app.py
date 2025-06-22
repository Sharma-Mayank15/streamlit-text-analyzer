import streamlit as st
from collections import Counter
import string

st.set_page_config(page_title="Text Analyzer", layout="centered")

st.title("📄 Advanced Text Analyzer")
st.write("Upload a `.txt` file and get instant analysis below:")

uploaded_file = st.file_uploader("Choose a text file", type="txt")

def analyze_text(text):
    lines = text.split("\n")
    words = text.split()
    sentences = text.split('.')
    clean_words = [word.strip(string.punctuation).lower() for word in words]
    common = Counter(clean_words).most_common(5)

    return {
        "lines": len(lines),
        "words": len(words),
        "characters": len(text),
        "sentences": len([s for s in sentences if s.strip()]),
        "common_words": common
    }

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    result = analyze_text(content)

    st.subheader("📊 Analysis Report")
    st.write(f"**Total Lines:** {result['lines']}")
    st.write(f"**Total Words:** {result['words']}")
    st.write(f"**Total Characters:** {result['characters']}")
    st.write(f"**Total Sentences:** {result['sentences']}")

    st.subheader("🔝 Most Common Words")
    for word, freq in result["common_words"]:
        st.write(f"- **{word}**: {freq}")
else:
    st.info("👆 Upload a .txt file to get started.")
