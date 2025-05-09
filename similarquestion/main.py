# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta")
pipe(messages)