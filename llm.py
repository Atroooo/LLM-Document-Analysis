import os
from dotenv import load_dotenv
from huggingface_hub import HfFolder
from vllm import LLM, SamplingParams
import torch

load_dotenv()
HfFolder.save_token(os.getenv("HF_TOKEN"))


def print_outputs(outputs):
    """Prints the outputs of the model.

    Args:
        outputs (list): List of outputs from the model.
    """
    # Need improvement to print the outputs
    print("-" * 80 + "\n")
    for output in outputs:
        # prompt = output.prompt
        generated_text = output.outputs[0].text
        # print(f"\nPrompt: {prompt!r}\n")
        print(f"Generated text: {generated_text!r}\n")
        print("-" * 80 + "\n")


def process_docs(docs, docs_dict, questions):
    """Process the documents and questions.
    Create the conversation and call the model.

    Args:
        docs (list): List of documents.
        docs_dict (dict): Dictionary of documents.
docs_dict[doc_name] = doc_text
        questions (list): List of questions.
    """
    conversation = []
    # Add the documents to the conversation
    for doc in docs:
        doc_name = doc.split('.')[0]
        conversation.append({
            "role": "user",
            "content": f"{doc}: {docs_dict[doc_name]}"
        })
        conversation.append({
            "role": "assistant",
            "content": "Saving the document..."
        })

    # Create a string of questions
    questions_str = ""
    for question in questions:
        questions_str += "[" + question + "]"

    # Add the questions to the conversation and give instructions to the model
    conversation.append({
        "role": "user",
        "content": f"Answer the questions and ONLY the questions \
asked by the user. Do not add anything else. Just answer once per question. \
Answer the questions in the given order.\
Each questions are contained between '[' and ']'. Do NOT add any questions \
that are not asked. \
The questions are related to the texts provided above. \
Do not answer if the question is not related to one of the text. \
Format of the text is given as follow : \
name_of_the_document: text_in_the_document.\
Output must be return as follow and only like this: \
[question you are answering: the question's answer]. \
Here is the list of question(s): {questions_str}."
    })
    outputs = call_llm(conversation)
    print_outputs(outputs)


def call_llm(conversation):
    """Call the model. In this case,
it is the Mistral-7B-Instruct-v0.2-GPTQ model.

    Args:
        conversation (list): List of conversation.

    Returns:
        list: outputs from the model.
    """
    model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
    # Set the sampling parameters, here we set the max tokens to 4096
    # and the temperature to 0.95 to make the model less creative
    sampling_params = SamplingParams(max_tokens=4096, temperature=0.95)
    llm = LLM(
        model=model_name,
        dtype="float16",  # convert the model to float16
    )
    # Call the model with the chat template
    outputs = llm.chat(conversation, sampling_params)
    del llm
    return outputs
