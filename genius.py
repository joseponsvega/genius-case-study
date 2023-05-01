import functools
import sys

from langchain import OpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter

llm = OpenAI(temperature=0)

text_splitter = CharacterTextSplitter()


def read_file(filename):
    with open(filename) as f:
        contents = f.read()
    texts = text_splitter.split_text(contents)

    return [Document(page_content=t, metadata={"source": filename}) for t in texts[:]]

files = ["./project_csv_file_1.csv", "./project_csv_file_2.csv", "./project_text_file_1.txt", "./project_text_file_2.txt"]

docs = functools.reduce(lambda a, b: a + b, [read_file(file) for file in files])

chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="refine")

query = sys.argv[1]
resp = chain({"input_documents": docs, "question": query}, return_only_outputs=True)

output_text = resp["output_text"]
print(output_text)