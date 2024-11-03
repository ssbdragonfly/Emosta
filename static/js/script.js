function initFloatingEmojis() {
    const emojis = document.querySelectorAll('.emoji');
    emojis.forEach(emoji => {
        const startX = Math.random() * 100;
        const startY = 100 + Math.random() * 20; 
        const rotationSpeed = Math.random() * 360;
        
        emoji.style.left = `${startX}vw`;
        emoji.style.bottom = `${startY}vh`;
        emoji.style.transform = `rotate(${rotationSpeed}deg)`;
        emoji.style.animationDuration = `${8 + Math.random() * 7}s`;
        emoji.style.animationDelay = `${Math.random() * 0.5}s`;
    });
}

window.speakRecommendation = function(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'it-IT';
    utterance.rate = 0.9;
    utterance.pitch = 1.1;
    speechSynthesis.speak(utterance);
}

document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('capture');
    const uploadBtn = document.getElementById('upload');
    const resultDiv = document.getElementById('result');
    const fileInput = document.getElementById('file-input');
    
    initFloatingEmojis();
    
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
            });
    }

    captureBtn.addEventListener('click', function() {
        canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
        canvas.toBlob(function(blob) {
            const formData = new FormData();
            formData.append('file', blob, 'capture.jpg');
            uploadImage(formData);
        }, 'image/jpeg');
    });

    uploadBtn.addEventListener('click', function() {
        fileInput.click();
    });

    fileInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            const formData = new FormData();
            formData.append('file', this.files[0]);
            uploadImage(formData);
        }
    });

    function uploadImage(formData) {
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('result');
            const popup = document.getElementById('result-popup');
            
            resultDiv.innerHTML = `
                <h3>Your Pasta Match!</h3>
                <div class="pasta-result">
                    ${data.image_url ? `<img src="${data.image_url}" alt="${data.pasta_shape}" class="pasta-image">` : ''}
                    <div class="pasta-info">
                        <p class="pasta-shape">Recommended Pasta: ${data.pasta_shape}</p>
                        <p class="emotion">Detected Emotion: ${data.emotion}</p>
                        <p class="recommendation">${data.recommendation}</p>
                        <button class="speak-btn" onclick="speakRecommendation(\`${data.recommendation}\`)">🗣️ Listen to Recommendation</button>
                    </div>
                </div>
            `;
            
            popup.classList.remove('hidden');
        })
        .catch(error => {
            resultDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
        });
    }    
    document.querySelector('.close-btn').addEventListener('click', () => {
        document.getElementById('result-popup').classList.add('hidden');
        speechSynthesis.cancel();
    });    
});
