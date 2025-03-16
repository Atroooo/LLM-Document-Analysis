import sys
import logging
from parsing import parse_docs
from llm import process_docs

if __name__ == "__main__":
    logging.disable(logging.CRITICAL)
    docs = sys.argv[1:]
    questions = []

    print("If you didn't provided any documents in the command line, please\
make sure that the files are in the documents folder (csv, pdf or txt)\
.")
    print("Please enter your questions. It could simply be to sum up a file or\
ask to find a relationship between the documents.\n\
Enter 'done' when finished.")
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
    docs, docs_dict = parse_docs(docs)
    process_docs(docs, docs_dict, questions)
    exit(1)
