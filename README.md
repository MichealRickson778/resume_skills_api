Project Overview
Create a Resume Skills Extraction API that uses Large Language Models (LLMs) and
vector databases to automatically extract and categorize skills from resumes. The
application should be deployed locally using FastAPI.
Technical Requirements
Core Technologies
- Python 3.9+
- FastAPI
- LLM of your choice (OpenAI GPT, Anthropic Claude, Mistral, or Gemma)
- Vector Database (any open-source vector DB)
- PDF/Text processing libraries
Mandatory Features
1. Resume Processing
   - Parse PDF/TXT format resumes
   - Extract and categorize skills using LLM
   - Store processed data in vector database
   - Handle basic error cases
2. API Endpoints
   - POST /upload-resume: Upload and process resume
   - GET /skills/{resume_id}: Retrieve extracted skills
   - GET /health: Service health check
   - Swagger/OpenAPI documentation
3. Skills Categories to Extract
   - Technical skills
   - Soft skills
   - Programming languages

   - Tools and technologies
   - Certifications (optional)
