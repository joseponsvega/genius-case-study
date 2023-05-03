import functools
import sys

from langchain import OpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.document_loaders import CSVLoader
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter

llm = OpenAI(temperature=0)

text_splitter = CharacterTextSplitter()


def read_file(filename):
    with open(filename) as f:
        contents = f.read()
    texts = text_splitter.split_text(contents)

    if filename.endswith(".csv"):
        loader = CSVLoader(file_path=filename)

        return loader.load()

    return [Document(page_content=t, metadata={"source": filename}) for t in texts]

files = ["./Grades.csv", "./Professors.csv", "./Syllabus.txt", "./Weekly Schedule.txt"]

docs = functools.reduce(lambda a, b: a + b, [read_file(file) for file in files])

chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="stuff", verbose=True)

query = sys.argv[1]
resp = chain({"input_documents": docs, "question": query}, return_only_outputs=True)

output_text = resp["output_text"]
print(output_text)