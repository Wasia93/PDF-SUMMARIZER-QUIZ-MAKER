import os
import pypdf
import streamlit as st
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

API = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.0-flash"

# --- PDF text extraction ---
def extract_pdf_text(file) -> str:
    text = ""
    reader = pypdf.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


# --- Gemini Client ---
@st.cache_resource
def get_client():
    return AsyncOpenAI(
        api_key=API,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )


# --- Streamlit UI ---
def run_streamlit_app():
    st.title("📚 Study Notes & Quiz Generator")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.success(f"PDF uploaded: {uploaded_file.name}")

        extracted_text = extract_pdf_text(uploaded_file)
        st.subheader("📄 Extracted Text:")
        st.text_area("PDF Content", extracted_text, height=300)

        client = get_client()

        if st.button("Generate Summary & Quiz"):
            with st.spinner("Generating summary and quiz... Please wait..."):

                async def run_model():
                    prompt = (
                        "You are a Study Notes Assistant. "
                        "First produce a summary of the following PDF text. "
                        "Then generate a quiz with answers.\n\n"
                        f"{extracted_text}"
                    )

                    response = await client.chat.completions.create(
                        model=MODEL,
                        messages=[{"role": "user", "content": prompt}]
                    )

                    return response.choices[0].message["content"]

                result = asyncio.run(run_model())

                st.subheader("📝 Summary & Quiz:")
                st.write(result)


if __name__ == "__main__":
    run_streamlit_app()
