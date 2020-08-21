from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
import json

app = Flask(__name__)

# 라우팅
@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods=('GET','POST'))
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 
        print(f.filename)
        f.save(secure_filename(f.filename))
        return '파일 업로드 성공'

@app.route('/receiveJson',methods=['POST'])
def receive_json():
    print(request.data)
    print(request.get_json())
    response = {'a':3}
    return json.dumps(response)

@app.route('/draw_test')
def draw_test():
    return render_template('naver_draw_sample.html')

@app.route('/request', methods =['POST'])
def query():
    value = request.form['SensorID']
    
    data= {"a":3}            
    jsondata=json.dumps(data)  
    
    return jsondata

if __name__ == "__main__":
    app.run(debug=True)