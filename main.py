from parsing import parse_docs

if __name__ == "__main__":
    docs = []
    questions = []

    print("Please enter the name of the files. (csv, pdf or txt)\n\
Enter 'done' when finished.")
    while True:
        input_doc = input()
        if (input_doc == "done" or input_doc == "Done"):
            break
        docs.append(input_doc)
        print("Another one ?")

    if (len(docs) == 0):
        print("No document provided.")
        exit(0)

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

    dict_docs = parse_docs(docs)
    print(dict_docs)
