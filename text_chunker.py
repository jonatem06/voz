import textwrap
import re

def clean_text(text):
    """
    Basic text cleaning to remove extra spaces and newlines.
    """
    text = text.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_text(text, chunk_size=250):
    """
    Splits long text into smaller chunks based on chunk_size.
    Tries to split by sentences to maintain context.
    """
    text = clean_text(text)

    # Simple sentence splitting regex (handles . ! ?)
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            if current_chunk:
                current_chunk += " " + sentence
            else:
                current_chunk = sentence
        else:
            if current_chunk:
                chunks.append(current_chunk)

            # If a single sentence is longer than chunk_size, use textwrap
            if len(sentence) > chunk_size:
                wrapped = textwrap.wrap(sentence, width=chunk_size, break_long_words=False, replace_whitespace=False)
                chunks.extend(wrapped[:-1])
                current_chunk = wrapped[-1]
            else:
                current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk)

    return chunks
