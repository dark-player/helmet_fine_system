from flask import Flask, render_template, Response, jsonify
import cv2
from detector import process_frame
from database import init_db
import sqlite3

app = Flask(__name__)

init_db()

camera = None
running = False


def gen_frames():
    global camera, running

    while running:
        success, frame = camera.read()
        if not success:
            break

        frame = process_frame(frame)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/start_camera')
def start_camera():
    global camera, running
    camera = cv2.VideoCapture(0)
    running = True
    return "started"


@app.route('/stop_camera')
def stop_camera():
    global running, camera
    running = False
    if camera:
        camera.release()
    return "stopped"


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_violations')
def get_violations():
    conn = sqlite3.connect("violations.db")
    c = conn.cursor()

    c.execute("SELECT plate, name, fine, reason, time FROM violations ORDER BY id DESC LIMIT 10")
    data = c.fetchall()

    conn.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)