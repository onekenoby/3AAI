import pocketsphinx


def recognize_italian_speech(audio_file_path):
    config = pocketsphinx.Config()
    # Update with the correct path
    config.set_string('-hmm', 'path/to/italian/acoustic/model')
    # Update with the correct path
    config.set_string('-lm', 'path/to/italian/language/model/language_model.lm')
    # Update with the correct path
    config.set_string('-dict', 'path/to/italian/language/model/language_model.dic')

    decoder = pocketsphinx.Decoder(config)

    with AudioFile(audio_file_path) as audio_file:
        audio_file_info = audio_file.info
        decoder.start_utt()

        while True:
            buf = audio_file.read(1024)
            if buf:
                decoder.process_raw(buf, False, False)
            else:
                break

        decoder.end_utt()

    hypothesis = decoder.hyp()
    if hypothesis:
        return hypothesis.hypstr
    else:
        return None


if __name__ == "__main__":
    # Replace with the path to your audio file
    audio_file_path = 'path/to/your/audio/file.wav'
    result = recognize_italian_speech(audio_file_path)

    if result:
        print("Recognized Italian Speech:", result)
    else:
        print("Speech recognition failed.")
