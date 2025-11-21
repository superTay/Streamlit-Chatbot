# services/stream_utils.py
import time
from typing import Generator


def stream_text(text: str, delay: float = 0.02) -> Generator[str, None, None]:
    """
    Generator that yields one character at a time to create a
    typewriter-style streaming effect for the assistant response.
    
    Used with:
        st.write_stream(stream_text("Hello world"))
    """
    for char in text:
        yield char
        time.sleep(delay)
