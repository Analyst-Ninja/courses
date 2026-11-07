from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm
from pydantic import BaseModel, Field


# ------- Define Output Schema -------
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and clear"
    )
    body: str = Field(description="""
        The main content of the email. 
        It should be well formated with proper greeting, paragraphs & signatures
        """)


# ------- Create Email generator agent -------
root_agent = LlmAgent(
    name="email_agent",
    model=LiteLlm(model="ollama_chat/qwen3.5:0.8b", api_base="http://localhost:11434"),
    description="",
    instruction="""
    You are an Email generator assistant.
    Your task is not generate professional email based on user's email request.

    GUIDELINES:
    - Create an appropriate subject line (concise and relevant)
    - Write a well-structured email body with:
        * Professional greeting
        * Clear and concise main content
        * Appropriate closing
        * Your name as signature
    - Suggest relevant attachments if applicable (empty list if none needed)
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON matching this structure:
    {
        "subject": "Subject line here", 
        "body": "Email body here with proper paragraphs and formatting"
    }

    DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_schema=EmailContent,
    output_key="email",
)
