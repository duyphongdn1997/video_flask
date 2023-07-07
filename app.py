from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/")
def player():
    return render_template("player.html")


@app.route('/video/<path:filename>')
def serve_video(filename):
    video_path = f'D:/Projects/github/player.html/videos/{filename}'  # Replace with the actual path to your video file
    return send_file(video_path, mimetype='video/mp4')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
