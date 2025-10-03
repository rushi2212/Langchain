from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer.

The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. The text continues with more lines to ensure it exceeds the max_length for splitting.

Here is some additional text to make sure we have enough content to demonstrate the splitting functionality effectively."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)