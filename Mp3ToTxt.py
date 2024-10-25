import speech_recognition as sr
from pydub import AudioSegment

# Cắt tệp âm thanh thành các đoạn nhỏ hơn
def split_audio(file, chunk_length_ms=60000):  # 60 giây mỗi đoạn
    audio = AudioSegment.from_wav(file)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

# Xử lý từng đoạn âm thanh
def process_chunks(chunks):
    recognizer = sr.Recognizer()
    full_text = ""

    for i, chunk in enumerate(chunks):
        chunk_file = f"chunk_{i}.wav"
        chunk.export(chunk_file, format="wav")

        with sr.AudioFile(chunk_file) as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="vi-VN")
            full_text += text + " "
        except sr.UnknownValueError:
            print(f"Không thể nhận diện đoạn {i}")
        except sr.RequestError as e:
            print(f"Lỗi nhận diện ở đoạn {i}: {e}")

    return full_text

# Chia nhỏ và nhận diện tệp âm thanh
audio_file = "output_audio.wav"
chunks = split_audio(audio_file)
transcribed_text = process_chunks(chunks)
print("Toàn bộ văn bản: ", transcribed_text)

print("Bui Tien Duc \n")

my_data = transcribed_text
with open("output.txt", "w") as file:
    file.write(my_data)
