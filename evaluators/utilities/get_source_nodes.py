from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index import load_index_from_storage, StorageContext
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from llama_index import Prompt

def get_source_nodes(question):

    answer_summarizer_prompt = f"""
System:
You act as a employee at Soliton Technologies.
Your name is Vina. You are based out of Coimbatore.
You are part of engineer welfare team at Soliton Technologies.
You help the company employees with their questions.

You must,
1. Try to answer the Original question and if it is not clear then use the formatted query to answer.
2. Your answer is a collection of facts from the given source information.
3. Answer ONLY with the source information listed below.
4. If there isn't enough information in the source information to answer, then say you don't know the answer. DO NOT generate answers that don't use the sources below.
5. If you do not know the answer, then ask a clarifying question that can help you to answer the question next time.
6. Your answer should be a very clear summary and should be understandable by a English speaking person.
7. Your answer will be rendered to the user in a markdown renderer.
8. Avoid unwanted to empty lines in the answers.

The source information is listed below:
{"{context_str}"}


Using the above source, please answer the below question.

Original question:
{question}

Formatted query based on Original question:
{"{query_str}"}

Answer:
"""

    prompt = Prompt(answer_summarizer_prompt)
    
    vector_store = FaissVectorStore.from_persist_dir(".\\storage\\HR")
    storage = StorageContext.from_defaults(
        vector_store=vector_store, persist_dir=".\\storage\\HR"
    )
    search_index = load_index_from_storage(storage_context=storage)

    index_query_engine = search_index.as_query_engine(
        similarity_top_k=5,
        text_qa_template=prompt,
        engine=os.getenv("OPENAI_CHAT_MODEL"), # gpt-3.5-turbo
        similarity_threshold=0.7,
    )

    response = ""
    # Handled the error that may be raised during an LLM Call
    try:
        response = index_query_engine.query(question)

    except Exception as exc:
        raise f"Error occured while searching & summarizing the answer: {exc}"
    
    sourcenodes = []
    for node in response.source_nodes:
        metadata = node.node.metadata
        sourcenodes.append({"content": node.node.text})

    return sourcenodes
