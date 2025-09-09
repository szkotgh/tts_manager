from tts_manager import TTSManager
from dotenv import load_dotenv
import time
load_dotenv()


tts = TTSManager()


# When you enter a string into play, playback will start automatically.
arvl_bus = ["5", "66", "66-4", "5002", "Y1302"]
tts_text = "번, ".join(arvl_bus) + "번, 버스가 잠시 후 도착할 예정입니다."
tts_text = tts_text.replace("-", "다시")
tts.play(tts_text)
print("Playing TTS...")
while tts.get_busy():
    time.sleep(0.1)


# If you call play while it's already playing, the previous audio will be canceled and it will start playing immediately.
tts_text = "과다한 스마트폰 사용으로 인한 정류소 내 미승차, 안전사고에 유의하시기 바랍니다."
tts.play(tts_text)
print("Playing TTS...")
while tts.get_busy():
    time.sleep(0.1)


# Running cleanup upon termination ensures safe shutdown.
tts.cleanup()
print("Done")