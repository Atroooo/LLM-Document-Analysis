import os
from dotenv import load_dotenv
from huggingface_hub import HfFolder
from vllm import LLM, SamplingParams

load_dotenv()
HfFolder.save_token(os.getenv("HF_TOKEN"))


def print_outputs(outputs):
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}")
        print(f"Generated text: {generated_text!r}")
    print("-" * 80)


model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
sampling_params = SamplingParams(max_tokens=4096)
llm = LLM(
    model=model_name,
    dtype="float16",
)

# conversation = [
#         {
#             "role": "user",
#             "content": "Hello"
#         },
#         {
#             "role": "assistant",
#             "content": "Hello! How can I assist you today?"
#         },
#         {
#             "role": "user",
#             "content":
#             "Write an essay about the importance of higher education.",
#         },
#         {
#             "role": "assistant",
#             "content":
#             "No worries!",
#         },
#         {
#             "role": "user",
#             "content":
#             "What did I ask you to do on the last message ?",
#         },
#     ]

# outputs = llm.chat(conversation, sampling_params, use_tqdm=False)

prompts = [
    "Hello this is a test.",
    "What did I say on the last message?",
    "What is the meaning of life?",
]


outputs = llm.generate(prompts, sampling_params, use_tqdm=False)
print_outputs(outputs)
