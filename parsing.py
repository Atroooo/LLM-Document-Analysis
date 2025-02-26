from PyPDF2 import PdfReader


def parse_docs(docs: list):
    """Parse the different documents provided by the user.

    Args:
        docs (list): A list containing the names of the documents.
    """
    parsed_docs = dict()
    for doc in docs:
        if (doc.endswith(".csv")):
            try:
                text = open(doc, "r")
            except Exception as e:
                print("Error while reading :", e)
                pass
            content = ' '.join([i for i in text])
            parsed_docs[doc.split('.')[0]] = content
        elif (doc.endswith(".txt")):
            try:
                text = open(doc, "r")
            except Exception as e:
                print("Error while reading :", e)
                pass
            parsed_docs[doc.split('.')[0]] = text.read()
        elif (doc.endswith(".pdf")):
            text = extract_from_pdf(doc)
            if (text == "None"):
                pass
            parsed_docs[doc.split('.')[0]] = text
        else:
            print(doc, ": Format not supported")
    return parsed_docs


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
