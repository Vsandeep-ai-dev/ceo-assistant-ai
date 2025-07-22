import os
import openai
import tempfile
import whisper

# Load environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# ----------------------
# LOAD WHISPER MODEL
# ----------------------
model = whisper.load_model("base")  # or "medium", "large" for more accuracy

# ----------------------
# TRANSCRIBE AUDIO FILE
# ----------------------
def transcribe_audio(file_path):
    print("[🔊] Transcribing audio...")
    result = model.transcribe(file_path)
    return result["text"]

# ----------------------
# SUMMARIZE TRANSCRIPT WITH GPT
# ----------------------
def summarize_transcript(transcript):
    prompt = f"""
You are an executive assistant AI.

Read this meeting transcript and summarize:
- Key points
- Tasks decided
- Questions raised
- Any follow-ups

Transcript:
\"\"\"{transcript}\"\"\"
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You summarize business meetings."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=400
    )

    return response.choices[0].message.content.strip()

# ----------------------
# MAIN FLOW (FOR TESTING)
# ----------------------
if __name__ == "__main__":
    test_file = "assets/test_meeting.mp3"  # Make sure you have a sample in assets
    transcript = transcribe_audio(test_file)
    summary = summarize_transcript(transcript)

    print("TRANSCRIPT:\n", transcript)
    print("\n\nSUMMARY:\n", summary)
