document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('capture');
    const uploadBtn = document.getElementById('upload');
    const resultDiv = document.getElementById('result');
    const fileInput = document.getElementById('file-input');
    
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
    });    
});
