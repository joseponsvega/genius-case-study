import sys

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, CSVLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

txt_loader = DirectoryLoader('.', glob="*.txt")

loaders = [txt_loader]
documents = []
for loader in loaders:
    documents.extend(loader.load())

for filename in ["Grades.csv", "Professors.csv"]:
    loader = CSVLoader(file_path=filename)

    documents.extend(loader.load())

print(f"Total number of documents: {len(documents)}")
print(documents)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

qa = ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0), vectorstore.as_retriever())

response = qa({"question": sys.argv[1], "chat_history": ""})
print(response)