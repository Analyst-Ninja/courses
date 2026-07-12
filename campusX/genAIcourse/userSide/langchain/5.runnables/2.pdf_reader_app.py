from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings

load_dotenv()

# Harry Potter 1 book path
BOOK_PATH = "/media/de-ninja/codebase/Courses/campusX/genAIcourse/userSide/langchain/5.runnables/hp1.txt"

# Load the document
loader = TextLoader(BOOK_PATH)
documents = loader.load()

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents=documents)

# Convert the text into embeddings and store into FAISS
vector_store = FAISS.from_documents(
    documents=docs,
    embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
)

# Create a retriver (fetched a relevant documents)
retiever = vector_store.as_retriever()

# Manually retriver relevant docs
query = "Who was hermione?"
retieved_docs = retiever.get_relevant_documents(query=query)

# Combined the relevant docs
retrieved_text = "\n".join([doc.page_content for doc in retieved_docs])

# Initialized the LLM
llm = GoogleGenerativeAI(model="gemini-2.0-flash")

# Manullay pass the retrived text to LLM
prompt = f"Based on the following text, answer the question: {query}\n{retrieved_text}"

# Getting the response from LLM
res = llm.invoke(prompt)
print(res)
