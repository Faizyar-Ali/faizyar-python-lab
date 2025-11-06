from bytez import Bytez
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv("Bytez_API_KEY")
sdk = Bytez(api_key)
def fetch_url(prompt):
          if not api_key:
             print("Error ⚠️: API KEY Enviroment not set")
             return "Error ⚠️: Api key Missing"
          try:
                 model = sdk.model("stabilityai/stable-diffusion-xl-base-1.0")
                 url,error = model.run(prompt)
                 if error or not url:
                       return f"Error: {error or 'Image Generation Failed'} "
                 return url
          except Exception as e:
                return f"Error : {e}"

