import glob
import os.path

from flask import Flask, render_template, send_file, request, jsonify

app = Flask(__name__)
video_folder_path = "D:/Projects/github/player.html/videos/"


@app.route("/")
def play():
    videos = [
        {"path": str(os.path.basename(x)), "name": str(os.path.basename(x))} for x in glob.glob(video_folder_path + "*")
    ]
    return render_template("index.html", videos=videos)


@app.route("/video/<path:filename>")
def serve_video(filename):
    video_path = os.path.join(video_folder_path, filename)  # Replace with the actual path to your video file
    return send_file(video_path, mimetype="video/mp4")


def prepare_video_url(video_path):
    # Assuming the videos are stored in the "videos" folder on the web server
    base_url = "http://localhost:5000/video/"
    video_url = base_url + video_path
    print(video_url)
    return video_url


@app.route("/play-video", methods=["POST"])
def play_video():
    video_path = request.json["videoPath"]
    video_url = prepare_video_url(video_path)  # Implement this function to generate the video URL

    return jsonify({"videoUrl": video_url})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
