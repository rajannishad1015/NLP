from transformers import pipeline

summarizer = pipeline("summarization")
text = """
The Transformers library by Hugging Face provides a simple and efficient way to perform 
various natural language processing 
 tasks, including text summarization. With just a few lines of code, you can leverage pre-trained 
models to generate concise summaries of long documents. This can be particularly useful for 
quickly understanding the main points of articles, research papers, or any lengthy text content. 
The library supports multiple languages and allows for customization of the summarization 
process to fit specific needs. 
In this example, we will demonstrate how to use the Transformers library to summarize a given 
text."""

summary = summarizer(text)
print("Original Text:")
print(text)
print("\nSummary:")
print(summary[0]['summary_text'])
