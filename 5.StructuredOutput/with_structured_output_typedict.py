# from langchain.chat_models import init_chat_model
# from dotenv import load_dotenv
# from typing import Literal, TypedDict, Any
# import json

# load_dotenv()

# model = init_chat_model("google_genai:gemini-2.0-flash")

# # Keep a TypedDict to describe the expected output shape


# class Review(TypedDict):
#     summary: str
#     sentiment: str

# # Provide a simple tool function with the same fields; this is used only as a schema for Gemini


# def review_tool(summary: str, sentiment: Literal["positive", "negative", "neutral"]) -> str:
#     """Return a structured review with 'summary' and 'sentiment'."""
#     return "ok"


# structured_output = model.with_structured_output(review_tool)

# text = (
#     "The hardware is great, but the software feels bloated. "
#     "There are too many pre-installed apps that I can't remove. "
#     "Also the UI looks outdated compared to other brands. "
#     "Hoping for a software update to fix this. "
#     "Return only 'summary' and 'sentiment'."
# )

# # Invoke on the structured_output wrapper (not the base model)
# response = structured_output.invoke(text)

# print("Raw response:", response)


# def _extract_review(obj: Any) -> dict | None:
#     # Try to coerce a single object to our Review shape
#     if hasattr(obj, "model_dump"):
#         d = obj.model_dump()
#     elif isinstance(obj, dict):
#         d = obj
#     elif isinstance(obj, str):
#         try:
#             parsed = json.loads(obj)
#             if isinstance(parsed, dict):
#                 d = parsed
#             else:
#                 d = {}
#         except Exception:
#             d = {}
#     else:
#         d = {
#             "summary": getattr(obj, "summary", None),
#             "sentiment": getattr(obj, "sentiment", None),
#         }
#     if not isinstance(d, dict):
#         return None
#     if "summary" in d or "sentiment" in d:
#         return {"summary": d.get("summary"), "sentiment": d.get("sentiment")}
#     return None


# # Normalize to dict for convenient indexing/printing, including list responses
# data: dict | None = _extract_review(response)
# if data is None and isinstance(response, list):
#     for item in response:
#         data = _extract_review(item)
#         if data is not None:
#             break
# if data is None:
#     data = {"summary": None, "sentiment": None}

# print(data)
# print(type(response))
# print(data.get('summary'))
# print(data.get('sentiment'))


# Annotated Output with TypedDict
# from langchain.chat_models import init_chat_model
# from dotenv import load_dotenv
# from typing import Literal, TypedDict, Any, Annotated, Optional
# import json

# load_dotenv()

# model = init_chat_model("google_genai:gemini-2.0-flash")

# # Keep a TypedDict to describe the expected output shape


# class Review(TypedDict):
#     key_themes: Annotated[list[str],
#                           "Write down all the key themes discussed in the review in a list."]
#     summary: Annotated[str, "A brief summary of the review"]
#     sentiment: Annotated[Literal["positive", "negative",
#                                  "neutral"], "The sentiment of the review"]
#     pros: Annotated[Optional[list[str]],
#                     "Write down all the pros mentioned inside a list."]
#     cons: Annotated[Optional[list[str]],
#                     "Write down all the cons mentioned inside a list."]

# # Provide a simple tool function with the same fields; this is used only as a schema for Gemini


# def review_tool(
#     key_themes: list[str],
#     summary: str,
#     sentiment: Literal["positive", "negative", "neutral"],
#     pros: Optional[list[str]] | None = None,
#     cons: Optional[list[str]] | None = None,
# ) -> str:
#     """Return a structured review with fields: key_themes, summary, sentiment, pros, cons."""
#     return "ok"


# structured_output = model.with_structured_output(review_tool)

# text = (
#     """
# I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say—it’s an absolute powerhouse!

# Performance:
# Powered by the Snapdragon 8 Gen 3, the phone feels lightning fast—whether I’m gaming, multitasking, or editing photos.

# Battery:
# The 5000mAh battery easily lasts a full day, even with heavy use. On top of that, 45W fast charging is a lifesaver when I need a quick top-up.

# S-Pen:
# The S-Pen integration is a great addition for note-taking and quick sketches, though I don’t use it very often.

# Camera:
# The 200MP camera blew me away. The night mode is stunning, capturing crisp and vibrant images even in low light. Zooming up to 10x looks excellent, while beyond 30x, quality starts to drop.

# Design & Build:
# While it looks premium, the weight and size make it a bit uncomfortable for one-handed use.

# Software:
# Samsung’s One UI still comes with unnecessary bloatware (like multiple Samsung apps duplicating Google’s).

# Price:
# At $1,300, it’s definitely expensive compared to competitors.

# Pros:
# - Insanely powerful processor (great for gaming & productivity)
# - Stunning 200MP camera with incredible zoom & night mode
# - Long-lasting 5000mAh battery + 45W fast charging
# - Unique and useful S-Pen support

# Cons:
# - Bulky & heavy (not ideal for one-handed use)
# - One UI still has bloatware
# - Expensive compared to competitors
# \n\nPlease extract and return only these fields: key_themes (list of short phrases), summary (2-3 sentences), sentiment (positive|negative|neutral), pros (list of short phrases), cons (list of short phrases).
# """
# )

# # Invoke on the structured_output wrapper (not the base model)
# response = structured_output.invoke(text)

# print("Raw response:", response)


# def _extract_review(obj: Any) -> dict | None:
#     """Attempt to extract all review fields from arbitrary responses (dict/list/objects/JSON-string)."""
#     if hasattr(obj, "model_dump"):
#         d: Any = obj.model_dump()
#     elif isinstance(obj, dict):
#         d = obj
#     elif isinstance(obj, str):
#         try:
#             parsed = json.loads(obj)
#             d = parsed
#         except Exception:
#             d = {}
#     else:
#         d = {
#             "key_themes": getattr(obj, "key_themes", None),
#             "summary": getattr(obj, "summary", None),
#             "sentiment": getattr(obj, "sentiment", None),
#             "pros": getattr(obj, "pros", None),
#             "cons": getattr(obj, "cons", None),
#         }

#     # If a dict, try direct keys; if missing, search nested
#     if isinstance(d, dict):
#         result = {
#             "key_themes": d.get("key_themes"),
#             "summary": d.get("summary"),
#             "sentiment": d.get("sentiment"),
#             "pros": d.get("pros"),
#             "cons": d.get("cons"),
#         }
#         if any(v is not None for v in result.values()):
#             return result
#         # Search nested values
#         for v in d.values():
#             nested = _extract_review(v)
#             if nested:
#                 return nested
#         return None

#     # If list/tuple, search each item
#     if isinstance(d, (list, tuple)):
#         for item in d:
#             nested = _extract_review(item)
#             if nested:
#                 return nested
#         return None

#     return None


# Normalize to dict for convenient indexing/printing, including list responses
# data: dict | None = _extract_review(response)
# if data is None and isinstance(response, list):
#     for item in response:
#         data = _extract_review(item)
#         if data is not None:
#             break
# if data is None:
#     data = {"key_themes": None, "summary": None,
#             "sentiment": None, "pros": None, "cons": None}

# print("\nParsed data:")
# print(json.dumps(data, indent=2, ensure_ascii=False))
# print("\nPython type of raw response:", type(response))


# def _print_list(name: str, value: Any) -> None:
#     if isinstance(value, list):
#         print(f"{name}:")
#         for i, item in enumerate(value, 1):
#             print(f"  {i}. {item}")
#     else:
#         print(f"{name}: {value}")


# _print_list("key_themes", data.get("key_themes"))
# print("summary:", data.get("summary"))
# print("sentiment:", data.get("sentiment"))
# _print_list("pros", data.get("pros"))
# _print_list("cons", data.get("cons"))




### With lecture code ###
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from typing import Literal, TypedDict, Annotated, Optional

load_dotenv()

# Initialize Gemini
model = init_chat_model("google_genai:gemini-2.0-flash")

# Define schema


class Review(TypedDict):
    key_themes: Annotated[list[str],
                          "Write down all the key themes discussed in the review in a list."]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"],
                         "The sentiment of the review"]
    pros: Annotated[Optional[list[str]],
                    "Write down all the pros mentioned inside a list."]
    cons: Annotated[Optional[list[str]],
                    "Write down all the cons mentioned inside a list."]
    name: Annotated[Optional[str], "Name of the reviewer"]


def review_tool(
    key_themes: list[str],
    summary: str,
    sentiment: Literal["positive", "negative", "neutral"],
    pros: Optional[list[str]] | None = None,
    cons: Optional[list[str]] | None = None,
    name: Optional[str] = None, 
) -> str:
    """Schema function for structured output: key_themes, summary, sentiment, pros, cons."""
    return "ok"


# Use structured output wrapper with a function schema (keeps TypedDict above for docs/types)
structured_model = model.with_structured_output(review_tool)

# Now use the structured model
result = structured_model.invoke(
    """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say—it’s an absolute powerhouse!

Performance:
Powered by the Snapdragon 8 Gen 3, the phone feels lightning fast—whether I’m gaming, multitasking, or editing photos.

Battery:
The 5000mAh battery easily lasts a full day, even with heavy use. On top of that, 45W fast charging is a lifesaver when I need a quick top-up.

S-Pen:
The S-Pen integration is a great addition for note-taking and quick sketches, though I don’t use it very often.

Camera:
The 200MP camera blew me away. The night mode is stunning, capturing crisp and vibrant images even in low light. Zooming up to 10x looks excellent, while beyond 30x, quality starts to drop.

Design & Build:
While it looks premium, the weight and size make it a bit uncomfortable for one-handed use.

Software:
Samsung’s One UI still comes with unnecessary bloatware (like multiple Samsung apps duplicating Google’s).

Price:
At $1,300, it’s definitely expensive compared to competitors.

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
print(type(result))
