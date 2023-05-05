from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


loader = PyPDFLoader("/Users/jessiewilkins/Documents/Wilkins Edited_Resume_2019v4_Software_Engineer.pdf")

documents = loader.load()

# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# documents = text_splitter.split_documents(documents)

print(documents)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.6), vectorstore.as_retriever(search_kwargs={"k": 1}), memory=memory)

query = "Use the information to make up a story about Jessie working on a challenging project that shows how he succeeded and overcame obstacles. Use a fake company and a fake project with fake obstacles not from the PDF."
result = qa({"question": query})
print(result)