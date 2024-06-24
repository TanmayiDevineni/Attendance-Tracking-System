from flask import Flask, render_template, Response, send_file
import cv2
from src.face_rec import scan, make_attendance
from src.excel_generation import getLastFilePath

app = Flask(__name__)


def capture_by_frames():
    global video_capture
    video_capture = cv2.VideoCapture(0)
    while True:
        frame = scan(video_capture)
        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    return render_template("start.html")


@app.route("/stop", methods=["POST"])
def stop():
    if video_capture.isOpened():
        video_capture.release()
    make_attendance()
    return render_template("stop.html")


@app.route("/download", methods=["GET"])
def excel():
    print(getLastFilePath())
    return send_file(
        getLastFilePath(), download_name="attendance.csv", as_attachment=True
    )


@app.route("/video_capture")
def video_capture():
    return Response(
        capture_by_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=8000)
