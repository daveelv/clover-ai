import sounddevice as sd
from scipy.io.wavfile import write
import whisper


model = whisper.load_model("base")


def listen():

    print("Listening...")

    sample_rate = 44100
    duration = 5

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    write(
        "voice_command.wav",
        sample_rate,
        recording
    )

    print("Processing...")

    result = model.transcribe(
        "voice_command.wav"
    )

    command = result["text"]

    print(f"You said: {command}")

    return command.lower().strip()