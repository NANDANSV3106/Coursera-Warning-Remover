# 🧹 Coursera Question Cleaner — Web

A lightweight web application that cleans copied Coursera question and quiz text by removing repeated AI-assistant warning boilerplate — accessible from any browser via a shareable link, no installation required.

This is the web (Streamlit) edition of the original desktop app. It provides the same cleaning logic through a simple browser interface: paste text, remove unwanted warning blocks, review the cleaned result, and copy it with one click.

---

## 🌐 Live App

```text
https://coursera-cleaner-06.streamlit.app/
```

👉 Click the link above to open the app — no installation needed.

---

## ✨ Features

### 🧹 Remove Warning Boilerplate

Automatically detects and removes configured AI-assistant warning blocks from copied text.

The current cleaner recognizes warning content beginning with:

```text
You are a helpful AI assistant.
```

and ending with:

```text
Do you understand?
```

### 📋 One-Click Copy

The cleaned output is shown in a code block with a built-in copy icon — click it to copy the result to your clipboard.

### 🔢 Word & Character Counter

The app displays total word and character counts for both the pasted input and the cleaned output.

### 💬 Status Feedback

After cleaning, the app reports:

- Number of warning blocks removed
- No warning boilerplate found (text shown as-is)

### 📝 Simple Two-Panel Layout

Side-by-side input and output panels, with a placeholder shown in the input box until you paste something.

### 🔗 No Install for Users

Anyone with the link opens it straight in a browser — nothing to download, no Python setup on their end.

---

## 🖥️ How It Works

```text
┌──────────────────────────┐
│   Copy Coursera Text     │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Paste Into the Web App  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Remove Warnings       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│     Cleaned Text         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Copy via the Code Block │
└──────────────────────────┘
```

---

## 🚀 How to Use

### 1. Open the app

Visit the deployed link (see [Live App](#-live-app)) — or run it locally:

```bash
pip install streamlit
streamlit run app.py
```

### 2. Paste your text

Paste copied Coursera question or quiz text into:

**📥 PASTE COPIED TEXT**

### 3. Remove warnings

Click:

**🧹 Remove Warnings**

### 4. Review the result

The cleaned text appears in:

**✨ CLEANED TEXT**

### 5. Copy the result

Click the copy icon in the top-right corner of the cleaned text block.

---

## 🧠 Cleaning Engine

The app uses regular expressions to identify warning blocks.

Warning patterns are defined using a start phrase and an end phrase:

```python
WARNING_PATTERNS = [
    ("You are a helpful AI assistant.", "Do you understand?"),
]
```

The matching system is designed to handle variations in copied text, including:

- Different capitalization
- Multiple spaces
- Irregular whitespace
- Line breaks
- Optional whitespace before punctuation
- Small punctuation variations

This makes the cleaner more tolerant of formatting differences introduced when copying text.

---

## ➕ Adding More Warning Patterns

Additional warning patterns can be added to the `WARNING_PATTERNS` list in `app.py`:

```python
WARNING_PATTERNS = [
    ("You are a helpful AI assistant.", "Do you understand?"),
    ("Another starting phrase.", "Another ending phrase."),
]
```

Each pattern consists of:

```text
(start phrase, end phrase)
```

The app compiles these patterns on startup and applies them whenever **Remove Warnings** is clicked.

---

## ☁️ Deployment (Streamlit Community Cloud — Free)

1. Push `app.py` and `requirements.txt` to a **public** GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, select the repo and branch, and set the main file path to `app.py`.
4. Click **Deploy**. After a minute or two, you'll get a public URL like:

   ```text
   https://coursera-cleaner-yourname.streamlit.app
   ```

5. Share that link — anyone can open it in a browser and use the tool immediately.

---

## 📐 Project Structure

```text
coursera-cleaner-web/
├── app.py             # Streamlit app: cleaning logic + UI
└── requirements.txt   # Python dependencies (streamlit)
```

---

## 🎨 User Interface

The web app includes:

- Header with title and subtitle
- Two-column input / output layout
- Action buttons (Remove Warnings, Clear)
- Word/character counters
- Status messages
- Footer with credit and LinkedIn link

---

## 🔒 Privacy

Text cleaning happens entirely within the app's own logic — no external AI service, API key, or database is used to process your pasted text.

Note: unlike the desktop version, this app runs on a remote server (Streamlit Community Cloud), so pasted text is sent over the network to render the page, the same way any web app works. It is not stored or logged by the app itself.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **Streamlit** | Web interface and hosting |
| **Regular Expressions** | Warning detection and removal |

---

## 💻 Requirements

- Python 3.x
- `streamlit` (see `requirements.txt`)

No database, custom backend, or external API is required.

---

## 🖥️ Also Available: Desktop Version

A Tkinter-based desktop edition of this tool is also available, with dark/light theming, keyboard shortcuts, and offline use. See the desktop app's own README for details.

---

## 🎯 Purpose

Coursera content copied into notes or other applications can sometimes contain repeated AI-assistant warning text alongside the actual question.

**Coursera Question Cleaner** provides a quick way to remove that unwanted boilerplate and produce cleaner, more readable text — now accessible to anyone via a simple link.

### Simple. Fast. Shareable. 🧹

---

**Made by Nandan S V.**
🔗 [linkedin.com/in/nandansv05](https://www.linkedin.com/in/nandansv05/)
