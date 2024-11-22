from gtts import gTTS
import playsound
import os


text = "Đường 3 tháng 2 hôm nay kẹt xe" 
output = gTTS(text,lang="vi", slow=False)
output.save("output.mp3")
playsound.playsound('output.mp3', True)
os.remove("output.mp3")