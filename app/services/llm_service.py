from langchain.llms import OpenAI
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

class LLMService:
    def __init__(self, api_key: str):
        self.llm = OpenAI(api_key=api_key, model="gpt-4")

    def extract_skills(self, text: str) -> dict:
        prompt = f"""
        The following text is extracted from a resume and may contain noise.
        Extract and categorize the skills:
        {text}
        Categories: Technical Skills, Soft Skills, Programming Languages, Tools/Technologies.
        """
        logger.info("Sending request to LLM")
        response = self.llm(prompt)
        return response
