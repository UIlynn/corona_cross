from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
import json, os
from datetime import datetime

# 현재 파일 절대 경로 저장
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 플라스크 앱 실행
app = Flask(__name__)



# 라우팅
@app.route('/receiveJson',methods=['POST'])
def receive_json():
    try:
        response = request.get_json()
        print(response)
        day = response.get('day')
        number = response.get('number')
        geojson = response.get('geojson')

        # k와 같은 폴더가 없으면 생성
        if not os.path.isdir(os.path.join(BASE_DIR,'static','data',day)):
            os.makedirs(os.path.join(BASE_DIR,'static','data',day))
        dir_name = os.path.join(BASE_DIR,'static','data',day)
        print(dir_name)

        # json 파일로 저장    
        filename = '{}.json'.format(number)
        with open(os.path.join(dir_name,filename), 'w', encoding='UTF-8') as fp:
                json.dump(geojson, fp, ensure_ascii=False, indent='\t')

        # list.json 생성
        file_list = os.listdir(dir_name)
        file_list.remove('list.json')
        with open(os.path.join(dir_name,'list.json'), 'w', encoding='UTF-8') as fp:
                json.dump(file_list, fp, ensure_ascii=False, indent='\t')
        return True
    except:
        return False

@app.route('/create_path')
def draw_test():
    return render_template('naver_draw_sample.html')

@app.route('/')
def cross_check():
    return render_template('cross_check.html')

if __name__ == "__main__":
    app.run(debug=True)