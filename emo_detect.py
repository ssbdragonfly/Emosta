from transformers import pipeline
import torch


classifier = pipeline(
    "image-classification",
    model="dima806/facial_emotions_image_detection",
    framework="pt",
    device=-1,
    torch_dtype=torch.float32
)

#input: image path, outputs emotion based on above model
def detect_emotion(img):
    result = classifier(img)
    emotion_map = {
        'happy': 'happy',
        'sad': 'sad',
        'angry': 'angry',
        'neutral': 'neutral',
        'surprise': 'surprised',
        'fear': 'neutral',
        'disgust': 'angry'
    }
    emotion = result[0]['label'].lower()
    return emotion_map.get(emotion, 'neutral')
