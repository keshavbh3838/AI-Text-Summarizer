import streamlit as st
from transformers import pipeline

@st.cache_resource
def get_summarizer():

    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = get_summarizer()

st.title("AI-powered Text Summarizer")
st.markdown("### Paste any text below to get a 3-sentence summary.")

input_text = st.text_area("Enter your text here", height=250)

if st.button("Summarize"):
    if input_text:
        with st.spinner("Summarizing..."):
            try:
                # Summarize the text
                summary = summarizer(input_text, max_length=90, min_length=30, do_sample=False)
                st.success("Summary generated successfully!")
                st.write("---")
                st.markdown("### Summary:")
                st.info(summary[0]['summary_text'])

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to summarize.")
