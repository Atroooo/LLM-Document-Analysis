import sys
import logging
import torch
from parsing import parse_docs
from llm import process_docs


def main():
    """Main function to process the documents and questions.
    The user can provide the documents in the command line or
    put them into the documents directory.
    The user provide the questions one by one.
    When the user is done, the documents and questions are processed
    by the model.
    """
    docs = sys.argv[1:]
    questions = []

    # Help
    if (len(docs) > 0 and docs[0] == "help"):
        print("Usage: python main.py 1[optional] document_list[optional]")
        print("1: Enable logging")
        print("document_list: List of documents to process [optional] \
(only csv, pdf and txt files)")
        exit(0)

    # Enable logging
    if (len(docs) > 0 and docs[0] == "1"):
        print("Logging enabled.")
        docs = sys.argv[2:]
    else:
        print("Logging disabled.")
        logging.disable(logging.CRITICAL)

    print("If you didn't provided any documents in the command line, please\
make sure that the files are in the documents folder (csv, pdf or txt)\
.")
    print("Please enter your questions. It could simply be to sum up a file or\
ask to find a relationship between the documents.\n\
Enter 'done' when finished.")
    # Get the questions
    while True:
        input_question = input()
        if (input_question == "Done" or input_question == "done"):
            break
        questions.append(input_question)
        print("Another one ?")

    if (len(questions) == 0):
        print("No question provided.")
        exit(0)

    print("Processing...")
    # Parse the documents
    docs, docs_dict = parse_docs(docs)
    # Process the documents and questions
    process_docs(docs, docs_dict, questions)


if __name__ == "__main__":
    main()
    # Clean up
    torch.cuda.empty_cache()
    torch.distributed.destroy_process_group()
    exit(1)
