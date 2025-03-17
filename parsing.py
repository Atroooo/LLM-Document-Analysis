from PyPDF2 import PdfReader
from pathlib import Path


def parse_docs(docs):
    """Parse the different documents provided by the user and convert them
    into strings to put them in a dict."""
    parsed_docs = dict()
    doc_list = []
    path = ""

    if (len(docs) == 0):
        # If no arguments are provided we get the documents from the directory
        path = "documents/"
        path_object = Path(path)
        docs = [f.name for f in path_object.iterdir()
                if f.is_file()]

    for doc in docs:
        doc_name = doc.split('.')[0]

        if (doc.endswith(".txt")):
            # Parse txt file and turn it into an str and add it to the dict.
            try:
                text = open(path + doc, "r")
            except Exception as e:
                print("Error while reading :", e)
                pass
            content = text.read()
            parsed_docs[doc_name] = content
            doc_list.append(doc_name)

        elif (doc.endswith(".pdf")):
            # Parse pdf file, turn it into an str and add it to the dict.
            text = extract_from_pdf(path + doc)
            if (text == "None"):
                pass
            parsed_docs[doc_name] = text
            doc_list.append(doc_name)

        else:
            print(doc, ": Format not supported")
    return doc_list, parsed_docs


def extract_from_pdf(doc: str):
    """Extract the text from a pdf file

    Args:
        doc (str): PDF file name.

    Returns:
        text: text extracted from the pdf.
    """
    try:
        pdf = PdfReader(doc)
    except Exception as e:
        print("Error while reading :", e)
        return "None"
    text = ""
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        text += page.extract_text()
    return text
