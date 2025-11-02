import requests
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")
def curr():
        if not api_key:
                return "Oops😵‍💫 API_key enviroment not set"
        print("------------------------------ Convert Currency -----------------------------")
        from_c=input("From  : ").upper().strip()
        to=input("To : ").upper().strip()
        if from_c.isalpha() and to.isalpha():
              pass
        else:
            return "Oops😵‍💫,Enter Valid Country Name"
        try:
            amount=float(input("Amount : "))
        except ValueError:
            return f"Oops😵‍💫,Please Enter Amount in Integer"
      
        try:
            url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_c}"
            responce=requests.get(url,timeout=10)
            responce.raise_for_status()
            data=responce.json()
            re=float(data["conversion_rates"][to])
            return f"{re*amount}"
        except requests.exceptions.ConnectionError as e:
            return f"No Internet , check your connection : {e}"
        except requests.exceptions.Timeout:
            return f"⏱️Error,The request timedout"
        except requests.exceptions.HTTPError as e:
            return f"Https Error Occurred : {e}"
        except requests.exceptions.RequestException as e:
            return f"an error occurred : {e}"
        except KeyError as e:
            return f"Key Error : {e}"
        
print(curr())

