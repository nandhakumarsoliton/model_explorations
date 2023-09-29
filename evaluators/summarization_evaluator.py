from utilities.get_source_nodes import get_source_nodes
from utilities.AI_Lookups import Llama2LLM, LangChainLLM
from utilities.create_excel_report import write_into_excel
from utilities.prompts import get_summarization_prompt

# Currently only HR questions
questions = ["How to apply for sick leave?","How to book soliton guest house?",
             "Whom should I contect for my doubts regarding salary deposits?", "What is SOliton Recognition framework",
             "What is the cash prize for Start Soliton Award?", "How many sick leave that I can take for a year?",
             "How to get recognized as a Star Team in Soliton?", "What are few Exit formalitites that I need to follow in Soliton?",
             "I wish to take a company wide KSS. Whom should I contact for that?", "Should I say Yes for every request in Soliton?",
             "Is it mandatory for a female soliton to tur on video during teams connect?", "I wish to apply for TIDEL Parking pass. What should I do?"
             ]
nodes_collections = []
llama2_responses = []
langchain_responses = []
prompt = get_summarization_prompt()

excel_report_path = 'C:\\v2\\Model Exploration\\Reports\\SummarizationReport.xlsx'

for question in questions:
    print(question)

    nodes = get_source_nodes(question)
    nodes_collections.append(nodes)
    #print(nodes)

    llama2_response = Llama2LLM(question, nodes, prompt)
    llama2_responses.append(llama2_response)

    #print(llama2_response)
    print("llama2_response Generated")

    langchain_response = LangChainLLM(question, nodes, prompt)
    langchain_responses.append(langchain_response)
    
    #print(langchain_response)
    print("langchain_response Generated")

write_into_excel(nodes_collections,llama2_responses, langchain_responses, questions, excel_report_path)
print("Report Generated...")


