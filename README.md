# Study Notes & Quiz Generator

This is a Streamlit application that uses a Gemini-powered agent to generate study notes and a quiz from a PDF file.

## How to Run

1.  Install the required packages:
    ```bash
    uv pip install -r requirements.txt
    ```

2.  Set the `GEMINI_API_KEY` environment variable. You can do this by creating a `.env` file in the root of the project and adding the following line:
    ```
    GEMINI_API_KEY="YOUR_API_KEY"
    ```

3.  Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

## How it Works

1.  The application uses the `pypdf` library to extract text from the uploaded PDF file.
2.  The extracted text is then passed to a Gemini-powered agent.
3.  The agent summarizes the text and generates a quiz based on the content.
4.  The summary and quiz are then displayed in the Streamlit UI.