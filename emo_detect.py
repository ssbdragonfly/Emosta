from deepface import DeepFace

#input: image path, outputs emotion based on below model
def detect_emotion(img):
    result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
    emotion_map = {
        'happy': 'happy',
        'sad': 'sad',
        'angry': 'angry',
        'neutral': 'neutral',
        'surprise': 'surprised',
        'fear': 'neutral',
        'disgust': 'angry'
    }
    emotion = result[0]['dominant_emotion']
    return emotion_map.get(emotion, 'neutral')