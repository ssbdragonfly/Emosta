# Emosta: Emotion-based Pasta Recommender

Emosta is a web application that recommends pasta shapes based on the user's current emotions. It uses image analysis and AI to detect emotions from uploaded or captured photos, and then generates personalized pasta recommendations. Made by Shaurya Bisht.

I got it deployed on onrender! Check it out here: https://emosta.onrender.com/

Note that the AI model is not perfect, and the recommendations may not always be accurate. Also note that this is purely for fun and not meant for serious use (unlesss you're a pasta lover). 

## Demo (Click!)

[![Watch the video](https://img.youtube.com/vi/lE1GF6BJjzM/0.jpg)](https://www.youtube.com/watch?v=lE1GF6BJjzM)

## Features

- Live camera capture
- Photo upload support
- Emotion detection using Hugging Face Transformers
- Environmental context analysis (lighting and warmth)
- AI-powered pasta recommendations via Google Gemini
- Visual pasta suggestions with Pexels API integration
- Analytics with Plausible Analytics

## Technologies Used

- Flask
- DeepFace
- TensorFlow
- OpenCV
- Google Generative AI
- Pexels API

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/emosta.git
    cd emosta
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory and add your API keys:
        ```env
        GEMINI_API_KEY=your_gemini_api_key
        PEXELS_API_KEY=your_pexels_api_key
        ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure

- `app.py`: Main Flask application.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JavaScript, images).
-  `script.js`: JavaScript for the frontend, backend, and intengration.
- `gemini_agent.py`: Python script for interacting with Google Generative AI.
- `emo_detect.py`: Python script for emotion detection using DeepFace.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
