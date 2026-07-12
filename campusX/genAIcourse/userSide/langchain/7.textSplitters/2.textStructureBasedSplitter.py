from pprint import pprint

from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
The Yeti (/ˈjɛti/)[2] is an ape-like creature purported to inhabit the Himalayan mountain range in Asia. In Western popular culture, the creature is commonly referred to as the Abominable Snowman. Many dubious articles have been offered in an attempt to prove the existence of the Yeti, including anecdotal visual sightings, disputed video recordings, photographs, and plaster casts of large footprints. Some of these are speculated or known to be hoaxes.

Folklorists trace the origin of the Yeti to a combination of factors, including Sherpa folklore and misidentified fauna such as bear or yak.[3] The Yeti is commonly compared to Bigfoot of North America, as the two subjects often have similar physical descriptions.[4]
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0)

res = splitter.split_text(text)

pprint(res)
