from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from typing import Literal, TypedDict, Annotated, Optional
from pydantic import BaseModel, Field

load_dotenv()

# Initialize Gemini
model = init_chat_model("google_genai:gemini-2.0-flash")

# Define schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the key themes mentioned inside a list."
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "The sentiment of the review"
        },
        "pros": {
            "type": ["array","null"],
            "items": {
                "type": "string"
            },
            "description": "Write down all the pros mentioned inside a list."
        },
        "cons": {
            "type": ["array","null"],
            "items": {
                "type": "string"
            },
            "description": "Write down all the cons mentioned inside a list."
        },
        "name": {
            "type": ["string","null"],
            "description": "Name of the reviewer"
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}


# Use structured output wrapper with a function schema (keeps TypedDict above for docs/types)
structured_model = model.with_structured_output(json_schema)

# Now use the structured model
result = structured_model.invoke(
    """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say—it's an absolute powerhouse!

Performance:
Powered by the Snapdragon 8 Gen 3, the phone feels lightning fast—whether I'm gaming, multitasking, or editing photos.

Battery:
The 5000mAh battery easily lasts a full day, even with heavy use. On top of that, 45W fast charging is a lifesaver when I need a quick top-up.

S-Pen:
The S-Pen integration is a great addition for note-taking and quick sketches, though I don't use it very often.

Camera:
The 200MP camera blew me away. The night mode is stunning, capturing crisp and vibrant images even in low light. Zooming up to 10x looks excellent, while beyond 30x, quality starts to drop.

Design & Build:
While it looks premium, the weight and size make it a bit uncomfortable for one-handed use.

Software:
Samsung's One UI still comes with unnecessary bloatware (like multiple Samsung apps duplicating Google’s).

Price:
At $1,300, it's definitely expensive compared to competitors.

Pros:
- Insanely powerful processor (great for gaming & productivity)
- Stunning 200MP camera with incredible zoom & night mode
- Long-lasting 5000mAh battery + 45W fast charging
- Unique and useful S-Pen support

Cons:
- Bulky & heavy (not ideal for one-handed use)
- One UI still has bloatware
- Expensive compared to competitors

review by Rushikesh Raut
"""
)

print(result)

