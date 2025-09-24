import pyttsx3
from PyPDF2 import PdfReader

pdf = input("C:/")
reader = PdfReader(pdf)

text = "Office works"
for page in reader.pages:
    text += page.extract_text()

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
