from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path="/home/de-ninja/Desktop/ObsidianNotes/MyNotes/Courses/campusX/genAI/langchain/",
    glob="*.md",
    loader_cls=TextLoader,
)

# docs = loader.load()

docs = loader.lazy_load()

# print(len(docs)) # Generator has no len function

print(next(docs).metadata)
print(next(docs).metadata)
print(next(docs).metadata)
print(next(docs).metadata)
