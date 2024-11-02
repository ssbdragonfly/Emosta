import os
import requests
import json
import google.generativeai as genai

#if you are using a different model, change the model name here, or if you want to use a different gen AI model, just change this setup
#if you just want to test the app locally, just search up gemini api dev and get a free api key, and put it in your .env file(dont forget to gitignore it)
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
PEXELS_API_KEY = os.environ.get('PEXELS_API_KEY')

def get_pasta_image(pasta_shape):
    headers = {'Authorization': PEXELS_API_KEY}
    url = f'https://api.pexels.com/v1/search?query={pasta_shape}+pasta&per_page=1'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            return data['photos'][0]['src']['medium']
    return None

#input: emotion, brightness, warmth, outputs pasta recommendation
def pasta_recommendation(emotion, brightness, warmth):
    prompt = f"""
    You are a passionate Italian chef who deeply understands the connection between emotions and pasta shapes.
    Someone is feeling {emotion}, in an environment with {brightness} brightness and {warmth} warmth.
    First, name a specific pasta shape.
    Then, explain why this shape perfectly matches their current state.
    Keep the explanation warm and engaging. 3-4 sentences.
    """
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    full_response = response.candidates[0].content.parts[0].text

    parser_prompt = f"""
    Extract only the pasta shape name from this response:
    {full_response}
    Return just the name, nothing else.
    """
    
    shape_response = model.generate_content(parser_prompt)
    shape_name = shape_response.candidates[0].content.parts[0].text.strip()
    pasta_image = get_pasta_image(shape_name)

    return {
        'shape': shape_name,
        'full_recommendation': full_response,
        'image_url': pasta_image
    }