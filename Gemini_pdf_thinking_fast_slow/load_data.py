import os
import argparse
from tqdm import tqdm
import pdfquery
import chromadb
from chromadb.utils import embedding_functions
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")



def main(
    documents_directory: str = "documents",
    collection_name: str = "documents_collection",
    persist_directory: str = "./chroma_storage",
) -> None:
    documents = []
    metadatas = []
    files = os.listdir(documents_directory)
    pdfs = [file for file in files if file.endswith(".pdf")]
    if pdfs:
        for filename in files:
            pdf = pdfquery.PDFQuery(f"{documents_directory}/{filename}")
            pdf.load()
            num_pages = len(pdf.pq('LTPage'))
            for page_number in range(num_pages):
                text_elements = pdf.pq(f'LTPage[pageid="{page_number + 1}"] LTTextLineHorizontal')
                text = [t.text for t in text_elements]
                text = ' '.join(text)
                text = text.strip()
                if len(text) == 0:
                    continue
                documents.append(text)
                metadatas.append({"filename": filename, "page_number": page_number + 1})
    else:
        for filename in files:
            with open(f"{documents_directory}/{filename}", "r") as file:
                for line_number, line in enumerate(
                    tqdm((file.readlines()), desc=f"Reading {filename}"), 1
                ):
                    line = line.strip()
                    if len(line) == 0:
                        continue
                    documents.append(line)
                    metadatas.append({"filename": filename, "line_number": line_number})

    client = chromadb.PersistentClient(path=persist_directory)

    if "GOOGLE_API_KEY" not in os.environ:
        gapikey = input("Please enter your Google API Key: ")
        genai.configure(api_key=gapikey)
        GOOGLE_API_KEY = gapikey
    else:
        GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

    embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=GOOGLE_API_KEY)

    collection = client.get_or_create_collection(
        name=collection_name, embedding_function=embedding_function
    )

    count = collection.count()
    print(f"Collection already contains {count} documents")
    ids = [str(i) for i in range(count, count + len(documents))]

    for i in tqdm(
        range(0, len(documents), 100), desc="Adding documents", unit_scale=100
    ):
        collection.add(
            ids=ids[i : i + 100],
            documents=documents[i : i + 100],
            metadatas=metadatas[i : i + 100],
        )

    new_count = collection.count()
    print(f"Added {new_count - count} documents")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load documents from a directory into a Chroma collection"
    )

    parser.add_argument(
        "--data_directory",
        type=str,
        default="documents",
        help="The directory where your text files are stored",
    )
    parser.add_argument(
        "--collection_name",
        type=str,
        default="documents_collection",
        help="The name of the Chroma collection",
    )
    parser.add_argument(
        "--persist_directory",
        type=str,
        default="chroma_storage",
        help="The directory where you want to store the Chroma collection",
    )

    # Parse arguments
    args = parser.parse_args()

    main(
        documents_directory=args.data_directory,
        collection_name=args.collection_name,
        persist_directory=args.persist_directory,
    )
