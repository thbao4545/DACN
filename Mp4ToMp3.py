import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment

# Bước 1: Tách âm thanh từ video MP4 và lưu dưới dạng tệp WAV
def extract_audio_from_video(video_file, output_audio_file):
    video = mp.VideoFileClip(video_file)
    video.audio.write_audiofile(output_audio_file)

# Bước 2: Chuyển đổi từ âm thanh WAV sang văn bản
def speech_to_text(wav_file):
    recognizer = sr.Recognizer()

    # Đọc tệp âm thanh
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)

    # Nhận diện giọng nói từ âm thanh
    try:
        text = recognizer.recognize_google(audio, language="vi-VN")  # Chuyển đổi ngôn ngữ nếu cần
        print("Bản ghi âm đã chuyển đổi thành văn bản: ", text)
    except sr.UnknownValueError:
        print("Không thể nhận diện được âm thanh")
    except sr.RequestError as e:
        print(f"Lỗi khi gọi dịch vụ nhận diện: {e}")

# Ví dụ cách dùng
video_file = "Seminar 2 20240720_180314.mp4"
audio_file = "output_audio.wav"
print(f"Đã xuất {audio_file}  \n")

# Bước 1: Tách âm thanh từ video MP4
extract_audio_from_video(video_file, audio_file)

try:
    # Bước 2: Chuyển đổi tệp WAV sang văn bản <= 1 phút
    speech_to_text(audio_file)
except:
    print("Có lỗi xảy ra! Lớn hơn 1 phút")


