import pyttsx3
import PyPDF2

# Initialize text-to-speech
speaker = pyttsx3.init()

# Open PDF file
with open("your_ebook.pdf", "rb") as book:
    reader = PyPDF2.PdfReader(book)
    pages = len(reader.pages)
    print(f"Total pages: {pages}")

    for num in range(pages):
        text = reader.pages[num].extract_text()
        if text:
            print(f"Reading page {num+1}")
            speaker.say(text)
            speaker.runAndWait()

speaker.stop()
