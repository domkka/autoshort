import moviepy.editor as mpe
import ffmpeg

def check_audio(input_file, fallback_audio):
    remove_audio = True
    try:
        hasaudio = ffmpeg.probe(input_file, select_streams="a")

        if hasaudio["streams"]:
            audio_clip = mpe.AudioFileClip(input_file)
            remove_audio = True
        else:
            audio_clip = mpe.AudioFileClip(fallback_audio)
            remove_audio = False

    except ffmpeg.Error as e:
        audio_clip = mpe.AudioFileClip(fallback_audio)
        remove_audio = False

    return audio_clip, remove_audio