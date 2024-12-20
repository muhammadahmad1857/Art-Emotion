from langchain_google_genai import GoogleGenerativeAI
from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()


app =  FastAPI()
 
llm =  GoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("API_KEY"))
 
@app.get("/generate")
def get_emotion(emotion:str,art_form:str,style:str,context:str,language:str="English"):
    
    prompt = f"""
You are an advanced Emotion-to-Art Generator. Your purpose is to translate human emotions and descriptive inputs into artistic outputs.

### Instructions:
1. I will provide you with specific parameters about the desired art, including emotional themes, medium, style, context, and language.
2. Your response must always be in valid JSON format, structured as follows:


  "emotion": "<user's input emotion>",
  "description": "<expanded emotional narrative>",
  "art_form": "<artistic form like poetry, painting, music>",
  "style": "<specified or inferred style>",
  "output": "<detailed artistic response>"


### Required Parameters:
- **Emotion**: A description of the primary emotion or mood to convey.
- **Art Form**: The desired output type (e.g., poem, short story, painting description).
- **Style**: Optional. A specific artistic style or tone (e.g., romantic, abstract, surreal).
- **Context**: Optional. Any additional details about the subject or scenario.
- **Language**: The desired language for the output, description also write context in that language and also desc and context (e.g., English, Spanish, French).

Data:

  "emotion": {emotion},
  "art_form": {art_form},
  "style": {style},
  "language": {language},
  "context": {context}


### Now, provide your input, and I will generate the artistic output in JSON format.
"""
    try:
        response = llm.invoke([prompt])
   
        return response
    except:
        return {"error": "Something went wrong. Make sure you have connected to the internet..."}
    

 
 
resp=get_emotion("melancholy","sing","jolly","a rainy evening in autumn","urdu")
print(resp)