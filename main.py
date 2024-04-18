from pydub import AudioSegment
from os import path
from whisper import transcribe_audio
import os

def split_audio(file_path, interval_ms):
    audio = AudioSegment.from_file(file_path)
    file_name, ext = path.splitext(path.basename(file_path))

    n_splits = len(audio) // interval_ms

    files = []

    for i in range(n_splits + 1):
        start = i * interval_ms
        end = (i + 1) * interval_ms
        chunk = audio[start:end]
        
        output = f"tmp_{file_name}_{i}{ext}"
        chunk.export(output, format="mp3")
        files.append(output)

    result = list(map(lambda x: transcribe_audio(x), files))
    return result

def main():
    file_path = "./test.mp3"
    interval_ms = 5_000

    file_size = os.path.getsize(file_path)

    MAX_FILE_SIZE = 25 * 1024 * 1024
    KB = 1024
    if file_size >= MAX_FILE_SIZE: 
        print(f"file size is over max size {file_size // KB}KB")
    else:
        print(f"file size is less than limit {file_size // KB}KB")

    result = split_audio(file_path, interval_ms)
    print(result)

    # 最終的にファイルは残しておきたくないので削除する
    removeTmpFiles()

def removeTmpFiles():
    for filename in os.listdir("./"):
        if filename.startswith('tmp'):
            file_path = os.path.join("./", filename)
            os.remove(file_path)

main()
