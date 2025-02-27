import sys
from parsing import parse_docs

if __name__ == "__main__":
    docs = sys.argv[1:]
    questions = []

    print("Please make sure that the files are in the documents folder\
(csv, pdf or txt).")
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

    docs, dict_docs = parse_docs(docs)
    print(docs)
    # print(dict_docs)
