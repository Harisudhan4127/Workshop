from gtts import gTTS 
import os
content = input("Enter the text to voice :")
language = "en"
tts = gTTS(text=content, lang=language, slow=False)
tts.save("output.mp3")
os.system("start output.mp3")