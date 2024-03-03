#!/home/theorizchy/SmartCCTV-Camera/venv/bin/python
from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera
import time
import os

app = Flask(__name__)

#background process happening without any refreshing
@app.route('/left')
def left():
    print ("Left")
    # os.system("python servo.py 1 2 0.1 1")       
    return ("nothing")

@app.route('/center')
def center():
    print ("Center")
    # os.system("python servo.py 89 90 0.3 1")       
    return ("nothing")

@app.route('/right')
def right():
    print ("Right")
    # os.system("python servo.py 179 180 0.1 1")       
    return ("nothing")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        return render_template('index.html', res_str=result)
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # context = ('/etc/ssl/localcerts/server.crt', '/etc/ssl/localcerts/server.key')
    app.run(host='0.0.0.0', port=1919, debug=False, threaded=True)
    # app.run(host='0.0.0.0', port=1919, debug=False, threaded=True, ssl_context=context)
