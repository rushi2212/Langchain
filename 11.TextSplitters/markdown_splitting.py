from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

markdown_text = """
# Project Documentation

Welcome to the **Project Documentation** for our sample project. This document demonstrates Markdown splitting.

## Introduction

Markdown is a lightweight markup language with plain-text formatting syntax. It is widely used for README files, documentation, and notes.

## Features

- Easy to read and write
- Supports headings, lists, links, and code blocks
- Converts easily to HTML or PDF

## Example Code Block
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.MARKDOWN, 
    chunk_size=300, 
    chunk_overlap=0
)

chunks = splitter.split_text(markdown_text)
print(chunks[0])
print(len(chunks))
