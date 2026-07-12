from pprint import pprint

from dotenv import load_dotenv
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

load_dotenv("../.env")

# Creating LangChain Documents for IPL Players

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"},
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"},
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"},
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"},
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
    persist_directory="IPL_chroma_db",
    collection_name="sample",
)

# Add documents -- It will generate a unique id like given below
vector_store.add_documents(documents=docs)

# [
#     'cdc5264e-d7d9-4469-88cf-90415e89d862',
#     '2923ac8a-cabd-4768-84d0-39899e8e6fba',
#     '45accfab-a80f-4f3c-8213-5e0d1db8e584',
#     '02752c21-270d-4332-b964-a19086140b96',
#     'abf3cf6a-0124-4aba-963b-8813cf4cf21a'
# ]


# view documents
res = vector_store.get(include=["embeddings", "metadatas", "documents"])

pprint(res)

# Search Query
query_res = vector_store.similarity_search(query="Who among these are a bowler", k=2)

# Search Query with score
query_res = vector_store.similarity_search_with_score(
    query="Who among these are a bowler", k=2
)

# metadata filter
query_res = vector_store.similarity_search_with_score(
    query="", filter={"team": "Chennai Super Kings"}
)

# Update Documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"},
)

vector_store.update_document(
    document_id="5351498f-3bef-45ea-b110-71353cc93522", document=updated_doc1
)

# Delete Documets
vector_store.delete(ids=["5351498f-3bef-45ea-b110-71353cc93522"])

# Get/ View Documents
query_res = vector_store.get(include=["documents", "metadatas"])
pprint(query_res)
