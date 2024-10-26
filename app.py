from flask import Flask, request, render_template, send_from_directory
import os
import subprocess
from spleeter.separator import Separator

app = Flask(__name__)

# CPUを強制的に使用するための設定
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # これにより、CUDAが無効化される

@app.route('/')
def home():
    return render_template('index.html')  # index.htmlを表示する

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "ファイルが見つかりません。"

    file = request.files['file']
    if file.filename == '':
        return "ファイルが選択されていません。"

    input_file = "uploaded_video.mp4"  # アップロードされたファイルの保存名
    file.save(input_file)  # ファイルを保存する

    # 音声分離の処理
    output_directory = 'output/'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 音を2つ（声とゲーム音）に分ける
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_file, output_directory)

    # 分けた音声ファイルのパスを設定
    vocals_file = os.path.join(output_directory, "uploaded_video/vocals.wav")
    accompaniment_file = os.path.join(output_directory, "uploaded_video/accompaniment.wav")

    # 声だけの動画を作成
    global final_output_file  # グローバル変数としてfinal_output_fileを設定
    final_output_file = "final_video.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-i", input_file, "-i", vocals_file, "-c:v", "copy",
        "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", final_output_file
    ])

    return "声だけの動画が作成されました！<br><a href='/download'>ダウンロードする</a>"

@app.route('/download')
def download_file():
    return send_from_directory(directory='.', path=final_output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
