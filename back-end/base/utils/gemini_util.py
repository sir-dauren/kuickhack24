import google.generativeai as genai
from django.conf import settings

from base.utils.process_recommendations import process_recommendations

genai.configure(api_key=settings.GOOGLE_TOKEN)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])


def generate_text(text):
    message = ("Напиши мне рекомендации на русском в 100 словах," +
               " как бы я мог снизить траты, покупая продукты: " + text +
               "после рекомендаций напиши мне текст в 50 словах, мотивацию," +
               "куда мог бы я полезно потратить деньги")
    convo.send_message(message)
    recommendations = convo.last.text
    processed_recommendations = process_recommendations(recommendations)
    return processed_recommendations