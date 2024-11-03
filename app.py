from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from emo_detect import detect_emotion
from gemini_agent import pasta_recommendation
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png','jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#input filename, outputs if the file is allowed to be uploaded
def allow(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#input image path, outputs features of the image to make better inferences.
def img_analyze(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = cv2.mean(gray)[0]
    bgr = cv2.mean(img)[:3]
    warmth = (bgr[2] + bgr[1]) / (bgr[0] + 1)
    return {
        'brightness': brightness,
        'warmth': warmth
    }

#main page, renders index.html
@app.route('/')
def index():
    return render_template('index.html')

#upload page, tries to upload file and get reccomendation
@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'no file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'no selected file'}), 400
            
        if file and allow(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            print("File saved to:", path)
            emotion = detect_emotion(path)
            print("Detected emotion:", emotion)
            analysis = img_analyze(path)
            print("Image analysis:", analysis)
            pasta_result = pasta_recommendation(
                emotion=emotion,
                brightness=analysis['brightness'],
                warmth=analysis['warmth']
            )
            print("Pasta result:", pasta_result)
            os.remove(path)
            return jsonify({
                'emotion': emotion,
                'pasta_shape': pasta_result['shape'],
                'recommendation': pasta_result['full_recommendation'].replace("*",""),
                'image_url': pasta_result['image_url']
            })
            
    except Exception as e:
        print(f"Error details: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
