"""
Coursera Question Cleaner — Web (Streamlit) version
-----------------------------------------------------
Removes repeated AI-assistant warning boilerplate that gets copied along
with quiz/question text from Coursera, so you can save clean notes.

Run locally:   streamlit run app.py
Deploy free:   push this folder to a GitHub repo, then deploy on
               https://share.streamlit.io (Streamlit Community Cloud).
"""

import re
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
        if line.strip() == "":
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

st.set_page_config(page_title="Coursera Question Cleaner", page_icon="🧹", layout="wide")

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

st.title("🧹 Coursera Question Cleaner")
st.caption("Strip repeated AI-warning boilerplate from copied questions.")

if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""
if "removed_count" not in st.session_state:
    st.session_state.removed_count = None

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("**📥 PASTE COPIED TEXT**")
    input_text = st.text_area(
        "input",
        height=380,
        placeholder="Paste your copied Coursera text here…",
        label_visibility="collapsed",
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

st.markdown(
    f"""
    <div class="footer">
        <span>Made by Nandan S V.</span>
        <a class="linkedin-badge" href="{LINKEDIN_URL}" target="_blank">
            <span class="linkedin-icon">in</span> in/nandansv05
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
