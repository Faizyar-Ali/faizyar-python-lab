from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)
def chat(user_input):
        if not api_key:
            return "Oops😵,Api_key enviroment not set"
        try:
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{user_input}(provide short answer if not forced)",
            )
            if not response.text:
                return f"Empty Responce from Chatgpt Please try again"
        except ConnectionError as e:
            return f"Connection Error : {e}"
        except Exception as e:
            return f"An Error Occured : {e}"
        return response.text

        