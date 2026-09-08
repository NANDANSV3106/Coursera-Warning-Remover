"""
Coursera Question Remover — Web (Streamlit) version
-----------------------------------------------------
Removes repeated AI-assistant warning boilerplate that gets copied along
with quiz/question text from Coursera, so you can save clean notes.

Run locally:   streamlit run app.py
Deploy free:   push this folder to a GitHub repo, then deploy on
               https://share.streamlit.io (Streamlit Community Cloud).
"""

import re
import urllib.parse
import streamlit as st

LINKEDIN_URL = "https://www.linkedin.com/in/nandansv05/"
LINKEDIN_BLUE = "#0A66C2"

# -----------------------------
# Cleaning logic (identical to the desktop version)
# -----------------------------

WARNING_PATTERNS = [
    ("You are a helpful AI assistant.", "Do you understand?"),
]


def _flexible(phrase: str) -> str:
    """Build a regex fragment that tolerates irregular whitespace and
    optional whitespace before trailing punctuation."""
    tokens = re.split(r"(\s+)", phrase)
    parts = []
    for token in tokens:
        if token == "":
            continue
        if token.isspace():
            parts.append(r"\s+")
            continue
        match = re.match(r"^(\w+)([?.!,]*)$", token)
        if match:
            word, punct = match.groups()
            parts.append(re.escape(word))
            if punct:
                parts.append(r"\s*" + re.escape(punct))
        else:
            parts.append(re.escape(token))
    return "".join(parts)


def _build_regex(start: str, end: str) -> re.Pattern:
    return re.compile(rf"{_flexible(start)}.*?{_flexible(end)}[.\s]*", re.IGNORECASE | re.DOTALL)


_COMPILED_PATTERNS = [_build_regex(s, e) for s, e in WARNING_PATTERNS]

# Standalone lines to strip: bare question numbering ("1.", "2.", "23.")
# and point-value labels ("1 point", "2 points", "10 points").
_QUESTION_NUMBER_RE = re.compile(r"^\d+\.$")
_POINTS_RE = re.compile(r"^\d+\s*points?$", re.IGNORECASE)


def remove_coursera_warnings(text: str):
    """Returns (cleaned_text, number_of_warnings_removed)."""
    removed_count = 0
    for pattern in _COMPILED_PATTERNS:
        text, n = pattern.subn("", text)
        removed_count += n

    lines = [line.rstrip() for line in text.splitlines()]
    cleaned_lines = []
    previous_blank = False
    for line in lines:
        stripped = line.strip()

        # Drop bare question-numbering lines and point-value labels entirely
        # (not treated as blank lines, so they don't leave extra gaps).
        if _QUESTION_NUMBER_RE.match(stripped) or _POINTS_RE.match(stripped):
            continue

        if stripped == "":
            if not previous_blank:
                cleaned_lines.append("")
            previous_blank = True
        else:
            cleaned_lines.append(line)
            previous_blank = False

    return "\n".join(cleaned_lines).strip(), removed_count


# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(page_title="Coursera Warning Remover", page_icon="🧹", layout="wide")

st.markdown(
    f"""
    <style>
    .stButton>button {{
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
    }}
    .footer {{
        margin-top: 2.5rem;
        padding-top: 0.9rem;
        border-top: 1px solid rgba(128,128,128,0.25);
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.8rem;
        opacity: 0.85;
    }}
    .linkedin-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        text-decoration: none;
        font-weight: 600;
        color: {LINKEDIN_BLUE};
    }}
    .linkedin-icon {{
        background: {LINKEDIN_BLUE};
        color: white;
        font-weight: 700;
        font-size: 0.7rem;
        padding: 2px 5px;
        border-radius: 3px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧹 Coursera Warning Remover")
st.caption("Strip repeated AI-warning boilerplate from copied text.")

if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""
if "removed_count" not in st.session_state:
    st.session_state.removed_count = None
if "clear_signal" not in st.session_state:
    st.session_state.clear_signal = False
if "input_box" not in st.session_state:
    st.session_state.input_box = ""

# Handle a pending clear request BEFORE the text_area widget is created below,
# since a widget's session_state value can't be changed after it's instantiated.
if st.session_state.clear_signal:
    st.session_state.input_box = ""
    st.session_state.clear_signal = False

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("**📥 PASTE COPIED TEXT**")
    input_text = st.text_area(
        "input",
        height=380,
        placeholder="Paste your copied Coursera text here…",
        label_visibility="collapsed",
        key="input_box",
    )
    st.caption(f"{len(input_text.split())} words · {len(input_text)} chars")

    b1, b2 = st.columns([1, 1])
    with b1:
        clean_clicked = st.button("🧹 Remove Warnings", use_container_width=True, type="primary")
    with b2:
        clear_clicked = st.button("🗑 Clear", use_container_width=True)

with col2:
    st.markdown("**✨ CLEANED TEXT**")

    if clean_clicked:
        if not input_text.strip():
            st.warning("Please paste your Coursera text first.")
        else:
            cleaned, removed = remove_coursera_warnings(input_text)
            st.session_state.cleaned_text = cleaned
            st.session_state.removed_count = removed

    if clear_clicked:
        st.session_state.cleaned_text = ""
        st.session_state.removed_count = None
        st.session_state.clear_signal = True
        st.rerun()

    if st.session_state.cleaned_text:
        st.code(st.session_state.cleaned_text, language=None)
        st.caption(
            f"{len(st.session_state.cleaned_text.split())} words · "
            f"{len(st.session_state.cleaned_text)} chars"
        )
    else:
        st.info("Cleaned text will appear here… (use the copy icon in the top-right of the box)")

    if st.session_state.removed_count is not None:
        if st.session_state.removed_count:
            st.success(f"✓ Removed {st.session_state.removed_count} warning block(s)")
        else:
            st.caption("No warning boilerplate found — text shown as-is")

    if st.session_state.cleaned_text:
        st.markdown("**🤖 Continue with an AI chat**")

        encoded = urllib.parse.quote(st.session_state.cleaned_text)
        chatgpt_url = f"https://chatgpt.com/?q={encoded}"
        claude_url = f"https://claude.ai/new?q={encoded}"
        gemini_url = "https://gemini.google.com/app"

        ac1, ac2, ac3 = st.columns(3)
        with ac1:
            st.link_button("Open in ChatGPT", chatgpt_url, use_container_width=True)
        with ac2:
            st.link_button("Open in Claude", claude_url, use_container_width=True)
        with ac3:
            st.link_button("Open in Gemini", gemini_url, use_container_width=True)

        if len(st.session_state.cleaned_text) > 1500:
            st.caption(
                "⚠️ Long text — ChatGPT/Claude links may truncate or fail to prefill. "
                "Gemini doesn't support prefilling at all yet — use the copy icon above and paste manually."
            )
        else:
            st.caption("Gemini doesn't support link prefilling yet — copy the text above and paste it in manually.")

st.markdown(
    f"""
    <div class="footer">
        <span>Made by Nandan S V</span>
        <a class="linkedin-badge" href="{LINKEDIN_URL}" target="_blank">
            <span class="linkedin-icon">in</span> in/nandansv05
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
