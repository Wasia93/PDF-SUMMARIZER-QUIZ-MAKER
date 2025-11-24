### **Role: Senior Python AI Engineer**

---

## **1. Project Overview**

You need to build an AI Agent that:

* **Reads a PDF** (using PyPDF)
* **Generates a summary**
* **Creates a quiz** (MCQs or mixed quiz)
* **UI:** Streamlit (recommended) or HTML/CSS
* **Backend:** OpenAgents SDK
* **Model:** Gemini (via Gemini CLI)
* **Tools:** Context7 MCP server (Docs Reader Tool)

---

## **2. Strict Technical Rules**

These rules are extremely important — you must follow them exactly:

### **1) Zero-Bloat Rule**

* Do **not** add unnecessary code.
* Write only what is required for the task.
* No extra decorators, comments, or over-engineered error handling.

### **2) API Configuration (IMPORTANT)**

Use:

* **OpenAgents SDK**
* **Gemini base URL:**
  `https://generativelanguage.googleapis.com/v1beta/openai/`
* **Model:** `gemini-2.0-flash`
* **API key:** via environment variable `GEMINI_API_KEY`

### **3) SDK Syntax Rule**

* You **must NOT** use the standard `openai` library.
* Only use **openai-agents SDK**.
* Every function must match the tool documentation exactly.

### **4) Error Recovery**

If you encounter:

* `SyntaxError`
* `ImportError`
* `AttributeError`

→ **Stop immediately** — do NOT guess.
→ Re-run:

```
@get-library-docs openai-agents
```

And verify the correct syntax.

### **5) Dependencies**

Install packages using `uv`.

---

## **3. Project File Structure (Your Folder Layout)**

Your Task-4 folder structure inside Gemini CLI will be:

```
task4/
├── .gemini/
│   └── settings.json
├── gemini.md
├── main.py
├── pyproject.toml
├── README.md
├── .env
└── uv.lock
```

Everything must remain inside this root folder.
**Do NOT create any extra subfolders.**

---

## **4. Implementation Flow (Step-by-Step)**

Follow this exact sequence:

---

### **Step 1 — Load Docs & Verify Syntax**

1. Open Gemini CLI

2. Run:

   ```
   @get-library-docs openai-agents
   ```

3. Review and understand:

* How tool decorators work
* How to initialize an agent
* Model calling format
* How to register tools inside an agent

If anything is unclear → re-read the docs.

---

### **Step 2 — Tool Functions (Inside main.py)**

You will create two tools:

---

#### **1. extract_pdf_text(file_path)**

* Use PyPDF
* Read and extract text from the PDF
* Return raw plain text

---

#### **2. generate_quiz(text)**

* Pass the extracted text to the agent
* The agent will generate MCQs or a mixed quiz

🔴 **IMPORTANT:**
The tool definitions **must exactly match** the format shown in `openai-agents` documentation.

---

### **Step 3 — Agent Setup (main.py)**

You must:

* Set Gemini base URL
* Use model `gemini-2.0-flash`
* Bind both tools to the agent
* Add a static system prompt:

```
"You are a Study Notes Assistant. First produce a summary, then generate a quiz."
```

---

### **Step 4 — Streamlit UI**

UI workflow:

1. User uploads a PDF
2. You extract the text using PyPDF
3. Display the summary
4. Show a “Create Quiz” button
5. Display the generated quiz

You may use any UI components (cards, boxes, containers, etc.)

---

## **5. Testing Cases**

Ensure the following:

1. PDF upload → Summary appears
2. "Create Quiz" button → Quiz displays
3. Larger PDF → Better summary + more detailed quiz

---

## **6. Final Submission Rules**

You must commit to GitHub:

* Source code
* `README.md`
* **Screenshot of your prompt** used inside Gemini CLI
* Paste this final prompt inside `gemini.md`

---

If you want, I can also prepare a **clean one-page final prompt** specifically for your `gemini.md` file.

Just say:
**“Send the final prompt for gemini.md.”**