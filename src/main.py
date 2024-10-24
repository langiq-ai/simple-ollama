import ollama
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Starting chat with ollama model")

try:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": "Why is the sky blue?",
            },
        ],
    )
    logging.debug(f"Response received: {response}")
    print(response["message"]["content"])
except Exception as e:
    logging.error(f"An error occurred: {e}")
