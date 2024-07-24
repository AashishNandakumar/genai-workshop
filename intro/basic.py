import os 
from dotenv import load_dotenv 
from langchain_cohere import ChatCohere

# from langchain_cohere.llms import Cohere
# from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

COHERE_API_KEY = os.getenv('COHERE_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

#! 1) LOAD THE MODEL
llm = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    max_tokens=1000,
    temperature=0.1
)

# llm = ChatGoogleGenerativeAI(
#     model="gemini-pro",
#     google_api_key=GOOGLE_API_KEY,
#     max_tokens=1000,
#     temperature=0.1
# )

#! 2) PROMPT THE MODEL
response = llm.invoke("say my name (here I am referring to the famous TV show Breaking bad)")

#! 3) PRINT THE RESPONSE 
print(response.content)
