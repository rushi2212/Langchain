def _extract_review(obj: Any) -> dict | None:
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


# # Normalize to dict for convenient indexing/printing, including list responses
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
