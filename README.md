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

Clears the pasted text, the cleaned text and the bot's answers.

### 🔢 Word and character counters

Shown for both the pasted input and the cleaned output.

### 💬 Continue in an AI chat

Opens the cleaned text in ChatGPT or Claude with the text pre-filled. Gemini doesn't support pre-filled links, so copy and paste manually there. Very long text may be cut off by the browser's URL length limit.

### 🤖 Study Bot

Get answers with explanations right inside the app.

- **Provider:** Gemini (Google), free tier available
- **Output per question:** the answer, a short reason, and a confidence rating (High / Medium / Low)
- **Automatic model fallback:** if a Gemini model is retired or out of quota, the app tries the next available one and shows which model answered
- **Double-check mode:** a second pass re-solves everything and corrects mistakes (marked "(corrected)")
- **Bring your own key:** paste an API key in **⚙️ Bot settings**; it is used only for your session and is not saved by the app

AI answers can be wrong. Verify anything marked Medium or Low, and anything that depends on course material the bot cannot see.

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
                              ├──►  💬 Open in ChatGPT / Claude
                              └──►  🤖 Study Bot (Gemini)
```

---

## 🚀 How to Use

1. Open the live app (or run it locally, see below).
2. Paste your copied text into **📥 PASTE COPIED TEXT**.
3. Click **🧹 Remove Warnings**.
4. Copy the result with the copy icon in the **✨ CLEANED TEXT** box.
5. Optional: use **💬 Continue with an AI chat** or the **🤖 Study Bot**.

### Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔑 Getting an API key for the Study Bot

The bot uses the **Gemini API** from Google, which has a free (rate-limited) tier and needs no billing details.

1. Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and sign in with Google.
2. Click **Create API key** and copy it (it starts with `AIza…`).
3. Paste it into **⚙️ Bot settings** in the app.

### Optional: provide a key for all visitors

If you host the app yourself, you can set a key on the server so visitors don't need their own. The app looks for an environment variable named `GEMINI_API_KEY`.

On **Render**: open your service → **Environment** → **Add Environment Variable** → set the name `GEMINI_API_KEY` and your key → save. Render redeploys automatically.

Notes:

- Never put keys in `app.py` or commit them to GitHub.
- Usage on a shared key is billed to the key owner. Set a spend limit with your provider. The app caps shared-key use at 10 runs per browser session, but refreshing the page resets that count.

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
├── app.py             # Streamlit app: cleaning logic + UI + study bot
├── requirements.txt   # streamlit, requests
└── README.md
```

---

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **Streamlit** | Web interface |
| **Regular expressions** | Warning detection and removal |
| **Gemini API** | Optional Study Bot |
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