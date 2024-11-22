from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Resume Skills Extraction API"
    LLM_API_KEY: str = "your-openai-api-key"  # OpenAI API key
    WEAVIATE_URL: str = "http://localhost:8080"  # Weaviate instance URL
    ENV: str = "development"

settings = Settings()
