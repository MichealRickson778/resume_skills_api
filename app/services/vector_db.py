import weaviate
from app.core.config import settings
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

# Initialize Weaviate client
weaviate_client = weaviate.Client(url=settings.WEAVIATE_URL)

# Ensure schema exists
def ensure_schema():
    schema = {
        "class": "Resume",
        "properties": [
            {"name": "resume_id", "dataType": ["string"]},
            {"name": "skills", "dataType": ["string"]},
        ],
    }
    if not weaviate_client.schema.contains(schema):
        weaviate_client.schema.create_class(schema)
        logger.info("Weaviate schema created for Resume class")

# Store extracted skills in Weaviate
def store_skills(resume_id: str, skills: dict):
    try:
        weaviate_client.data_object.create(
            {
                "resume_id": resume_id,
                "skills": str(skills),
            },
            class_name="Resume",
        )
        logger.info(f"Stored skills for resume_id: {resume_id}")
    except Exception as e:
        logger.error(f"Error storing skills in Weaviate: {e}")
        raise

# Retrieve skills from Weaviate
def retrieve_skills(resume_id: str) -> dict:
    try:
        result = weaviate_client.query.get("Resume", ["skills"]).with_where(
            {"path": ["resume_id"], "operator": "Equal", "valueString": resume_id}
        ).do()
        if not result["data"]["Get"]["Resume"]:
            raise ValueError("Resume ID not found")
        return eval(result["data"]["Get"]["Resume"][0]["skills"])
    except Exception as e:
        logger.error(f"Error retrieving skills from Weaviate: {e}")
        raise ValueError("Resume ID not found")
