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
        print(f"\nPrompt: {prompt!r}\n")
        print(f"Generated text: {generated_text!r}\n")
        print("-" * 80 + "\n")


def process_docs(docs, docs_dict, questions):
    conversation = []
    for doc in docs:
        doc_name = doc.split('.')[0]
        conversation.append({
            "role": "user",
            "content": f"{doc_name}: {docs_dict[doc_name]}"
        })
        conversation.append({
            "role": "assistant",
            "content": "Saving the document..."
        })

    questions_str = ""
    for question in questions:
        questions_str += "[" + question + "]"

    conversation.append({
        "role": "user",
        "content": f"Answer the questions and only the questions \
related to the texts I gave you above : {questions_str}. \
The questions are contained between '[' and ']'. \
Answer is the language of the questions. Every answers must be contained\
between '[' and ']' like the questions."
    })
    outputs = call_llm(conversation)
    print_outputs(outputs)


def call_llm(conversation):
    model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
    sampling_params = SamplingParams(max_tokens=4096, temperature=0.95)
    llm = LLM(
        model=model_name,
        dtype="float16",
    )
    outputs = llm.chat(conversation, sampling_params, use_tqdm=False)
    del llm
    gc.collect()
    torch.cuda.empty_cache()
    return outputs
