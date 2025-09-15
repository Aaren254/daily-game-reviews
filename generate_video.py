from moviepy.editor import *
from gtts import gTTS
import random

# 1. Choose a game and write a review
games = ["Hades", "Elden Ring", "Stardew Valley", "Hollow Knight"]
game = random.choice(games)
review = f"Today’s review is about {game}. It's an incredible game with outstanding mechanics and visuals."

# 2. Convert review to speech
tts = gTTS(text=review, lang='en')
tts.save("voice.mp3")

# 3. Use a static image (add 'cover.jpg' to your repo)
clip = ImageClip("cover.jpg").set_duration(60)
audio = AudioFileClip("voice.mp3")
video = clip.set_audio(audio)

# 4. Export the video
video.write_videofile("output.mp4", fps=24)

