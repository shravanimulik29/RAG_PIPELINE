from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Create FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server",
    docs_url=None,      # Disable /docs
    redoc_url=None,     # Disable /redoc  
    openapi_url=None    # Disable /openapi.json
)

# Initialize models
model = ChatOpenAI(model="gpt-3.5-turbo")  # Specify model explicitly
llm = ChatOllama(model="llama2")

# Create prompts
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} with 100 words"
)

# Add routes
add_routes(
    app,
    ChatOpenAI(model="gpt-3.5-turbo"),
    path="/openai"
)

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "LangServe API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)