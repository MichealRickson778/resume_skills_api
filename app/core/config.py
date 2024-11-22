from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Resume Skills Extraction API"
    LLM_API_KEY: str = "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"  # OpenAI API key
    WEAVIATE_URL: str = "http://localhost:8080"  # Weaviate instance URL
    ENV: str = "development"

settings = Settings()
