import os
from dotenv import load_dotenv
from huggingface_hub import HfFolder
from vllm import LLM, SamplingParams
import gc
import torch

load_dotenv()
HfFolder.save_token(os.getenv("HF_TOKEN"))


def print_outputs(outputs):
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}")
        print(f"Generated text: {generated_text!r}")
    print("-" * 80)


# def process_docs():
    

model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
sampling_params = SamplingParams(max_tokens=4096)
llm = LLM(
    model=model_name,
    dtype="float16",
)

conversation = [
        {
            "role": "user",
            "content": "Hello, how are you ?"
        },
        {
            "role": "assistant",
            "content": "==="
        },
        {
            "role": "user",
            "content":
            "This is a test.",
        },
        {
            "role": "assistant",
            "content":
            "No worries!",
        },
        {
            "role": "user",
            "content":
            "What did you tell me after my first message ?",
        },
    ]

outputs = llm.chat(conversation, sampling_params, use_tqdm=False)

# prompts = [
#     "Hello this is a test.",
#     "What did I say on the last message?",
#     "What is the meaning of life?",
# ]

# outputs = llm.generate(prompts, sampling_params, use_tqdm=False)

print_outputs(outputs)
del llm
gc.collect()
torch.cuda.empty_cache()
