# 🧹 Coursera Warning Remover — Web

A lightweight web app that cleans copied Coursera question and quiz text by removing the repeated AI-assistant warning boilerplate, plus question numbers, point labels and "Enter answer here" placeholders. Open it from any browser via a shareable link — no installation required.

This is the web (Streamlit) edition of the original desktop app.

---

## 🌐 Live App

```text
https://coursera-warning-remover.onrender.com/
```

👉 Click the link above to open the app.

> Hosted on Render's free tier, so the first visit after a quiet period can take about a minute to wake up.

---

## ✨ Features

### 🧹 Clean copied text

Removes, in one click:

- The AI-assistant warning block (from `You are a helpful AI assistant.` to `Do you understand?`)
- Bare question-number lines (`1.`, `2.`, `23.`)
- Point labels (`1 point`, `4 points.`)
- `Enter answer here` placeholders
- Extra blank lines

Question headings such as `Question 1` and all real question content are kept.

### 📋 One-click copy

The cleaned output is shown in a code block with a built-in copy icon.

### 🗑 Clear

Clears both the pasted text and the cleaned text.

### 🔢 Word and character counters

Shown for both the pasted input and the cleaned output.

### 💬 Continue in an AI chat

Opens the cleaned text in ChatGPT or Claude with the text pre-filled. Gemini doesn't support pre-filled links, so copy and paste manually there. Very long text may be cut off by the browser's URL length limit.

### 🔗 Footer

Credit line with GitHub and LinkedIn links.

---

## 🖥️ How It Works

```text
Copy Coursera text
        │
        ▼
Paste into the app
        │
        ▼
🧹 Remove Warnings  ──►  Cleaned text  ──►  📋 Copy
                              │
                              └──►  💬 Open in ChatGPT / Claude
```

---

## 🚀 How to Use

1. Open the live app (or run it locally, see below).
2. Paste your copied text into **📥 PASTE COPIED TEXT**.
3. Click **🧹 Remove Warnings**.
4. Copy the result with the copy icon in the **✨ CLEANED TEXT** box.
5. Optional: use **💬 Continue with an AI chat** to open it in ChatGPT or Claude.

### Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧠 Cleaning Engine

Warning patterns are defined as a start phrase and an end phrase:

```python
WARNING_PATTERNS = [
    ("You are a helpful AI assistant.", "Do you understand?"),
]
```

Matching tolerates differences in capitalization, spacing, line breaks and small punctuation variations, so formatting changes from copying don't break it.

### Adding more warning patterns

Add more pairs to `WARNING_PATTERNS` in `app.py`:

```python
WARNING_PATTERNS = [
    ("You are a helpful AI assistant.", "Do you understand?"),
    ("Another starting phrase.", "Another ending phrase."),
]
```

---

## ☁️ Deployment (Render)

1. Push `app.py` and `requirements.txt` to a GitHub repository.
2. On [render.com](https://render.com), create a **New → Web Service** and connect the repo.
3. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Deploy. Render gives you a public `onrender.com` URL.

---

## 📐 Project Structure

```text
Coursera-Warning-Remover/
├── .streamlit/
│   └── config.toml    # hides developer-only toolbar items from viewers
├── app.py             # Streamlit app: cleaning logic + UI
├── requirements.txt   # streamlit
└── README.md
```

---

## 🔒 Privacy

- Cleaning happens inside the app's own code on the server. No AI service or API key is used.
- The **💬 AI chat buttons** put the cleaned text in a link that opens ChatGPT or Claude in your browser. Nothing is sent until you click one.
- Like any hosted web app, pasted text travels from your browser to the server to render the page. The app doesn't store it.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **Streamlit** | Web interface |
| **Regular expressions** | Warning detection and removal |
| **Render** | Hosting |

---

## 🖥️ Also available: desktop version

A Tkinter desktop edition with dark/light themes and offline use also exists.

---

## 🎯 Purpose

Text copied from Coursera often arrives with repeated AI-assistant warning text, question numbers and point labels mixed in with the actual questions.

**Coursera Warning Remover** strips that clutter so you get clean, readable questions for your study notes.

### Simple. Fast. Shareable. 🧹

---

**Made by Nandan S V**
🔗 [LinkedIn](https://www.linkedin.com/in/nandansv05/) · 💻 [GitHub](https://github.com/NANDANSV3106)
