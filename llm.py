import os
from dotenv import load_dotenv
from huggingface_hub import HfFolder
from vllm import LLM, SamplingParams

load_dotenv()
HfFolder.save_token(os.getenv("HF_TOKEN"))

model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
sampling_params = SamplingParams(max_tokens=4096)
llm = LLM(
    model=model_name,
    dtype="float16",
)

# Define the messages for the conversation
messages = [
    {
        "role": "user",
        "content": "Qui est le meilleur peintre français ? Répondez avec des explications détaillées.",
    }
]

# Generate a response
res = llm.chat(messages=messages, sampling_params=sampling_params)

# Print the response
print(res[0].outputs[0].text)
