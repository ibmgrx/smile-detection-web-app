from flask import Flask, jsonify, render_template, Response, request
from camera import Video

app=Flask(__name__)

bar = 0

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        # firstname = str(Video.bar)
        # lastname = str(Video.bar)
        output = str(float("{:.2f}".format(Video.bar)))
        # output = str(Video.bar)
        # if firstname and lastname:
        # return jsonify({'output': output, 'progressbar':Video.bar})
        # return jsonify({'output': output + 's of Happiness','bardata': float("{:.2f}".format(Video.bar))})
        return jsonify({'output': output + 's of Happiness','bardata': output+'%'})
        # return jsonify({'error' : 'Missing data!'})
    return render_template('index.html', bar = Video.bar)

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type:  image/jpeg\r\n\r\n' + frame +
        b'\r\n\r\n')
   
@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)