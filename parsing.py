from PyPDF2 import PdfReader
from pathlib import Path


def parse_docs():
    """Parse the different documents provided by the user."""
    path = "documents/"
    subdirectory_path = Path(path)
    docs_name = [f.name for f in subdirectory_path.iterdir() if f.is_file()]
    parsed_docs = dict()

    for doc in docs_name:
        doc = path + doc

        if (doc.endswith(".csv")):
            # Parse csv file and turn it into an str and add it to the dict.
            try:
                text = open(subdirectory_path + doc, "r")
            except Exception as e:
                print("Error while reading :", e)
                pass
            content = ' '.join([i for i in text])
            parsed_docs[doc.split('.')[0]] = content

        elif (doc.endswith(".txt")):
            # Parse txt file and turn it into an str and add it to the dict.
            try:
                text = open(doc, "r")
            except Exception as e:
                print("Error while reading :", e)
                pass
            content = text.read()
            parsed_docs[doc.split('.')[0]] = content

        elif (doc.endswith(".pdf")):
            # Parse pdf file, turn it into an str and add it to the dict.
            text = extract_from_pdf(subdirectory_path + doc)
            if (text == "None"):
                pass
            parsed_docs[doc.split('.')[0]] = text

        else:
            print(doc, ": Format not supported")
    return docs_name, parsed_docs


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
