# Emosta: Emotion-based Pasta Recommender

Emosta is a web application that recommends pasta shapes based on the user's current emotions. It uses image analysis and AI to detect emotions from uploaded or captured photos, and then generates personalized pasta recommendations.

## Features

- Live camera capture
- Photo upload support
- Emotion detection using Hugging Face Transformers
- Environmental context analysis (lighting and warmth)
- AI-powered pasta recommendations via Google Gemini
- Visual pasta suggestions with Pexels API integration

## Technologies Used

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- AI Models:
- Emotion Detection: Hugging Face Transformers
- Recommendation Engine: Google Gemini AI
- Image Processing: OpenCV
- Image Search: Pexels API

## Setup

1. Clone the repository `git clone https://github.com/yourusername/emosta.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in your .env file:
`GEMINI_API_KEY: Your Google Gemini API key PEXELS_API_KEY=your_pexels_api_key`
4. Run the application: `python app.py`

## Usage

1. Open the application in your browser
2. Allow camera access or use the upload button
3. Take/select a photo
4. Receive your personalized pasta recommendation!

## Note

This application is for demonstration purposes and may require additional error handling and security measures for production use.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/emosta.git
   cd emosta
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the Gemini API key:
   - Obtain an API key from the Google AI Studio (https://makersuite.google.com/)
   - Set the API key as an environment variable:
     ```
     export GEMINI_API_KEY=your_api_key_here
     ```

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000` to use the application.

## Usage

1. Allow camera access when prompted, or click the "Upload Photo" button to select an image file.
2. If using the camera, click "Capture Photo" to take a picture.
3. Wait for the image to be processed and analyzed.
4. View your detected emotion, environmental context, and the recommended pasta shape.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).