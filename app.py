from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
import json, os
from datetime import datetime

# 현재 파일 절대 경로 저장
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 플라스크 앱 실행
app = Flask(__name__)

# 임시 카운트
count = 1

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
    response = request.get_json()

    # k와 같은 폴더가 없으면 생성
    if not os.path.isdir(os.path.join(BASE_DIR,'data')):
        os.makedirs(os.path.join(BASE_DIR,'data'))
    dir_name = os.path.join(BASE_DIR,'data')
    # print(dir_name)

    # json 파일로 저장    
    global count
    filename = '{}.json'.format(count)
    with open(os.path.join(dir_name,filename), 'w', encoding='UTF-8') as fp:
            json.dump(response, fp, ensure_ascii=False, indent='\t')
    count += 1
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