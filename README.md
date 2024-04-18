# split-audio-for-whisper
[Whisper](https://platform.openai.com/docs/guides/speech-to-text)が許容できるファイルサイズが25MBなので、これを超えるような場合にファイルを分割して何とかするためのスクリプト

# use
## get OpenAI API Key
Obtain the API_KEY and update `whisper.py` to use the new API_KEY.

## Execute
execute the command below

```
python -m venv env
pip install -r requirements.txt

python main.py
````

