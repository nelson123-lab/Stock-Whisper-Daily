from dotenv import load_dotenv
import os
import openai

def split_text(text):
    max_chunk_size = 2048
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def generate_summary(text):
    input_chunks = split_text(text)
    output_chunks = []
    for chunk in input_chunks:
        response = openai.Completion.create(
            engine="davinci",
            prompt=(f"Please provide a one line summary for the following text {chunk}"),
            temperature=0.5,
            max_tokens=1024,
            n = 1,
            stop=None
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
    return " ".join(output_chunks)