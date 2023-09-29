

from dotenv import load_dotenv
load_dotenv()

from utilities.AI_Lookups import Llama2LLM, LangChainLLM, LLama2CodeLLM
from utilities.create_excel_report import write_into_excel_3Models
from utilities.prompts import get_general_code_generation_prompt

questions = ["Generate a program to reverse a string.", "Generate a program to remove duplicates in an array", "Give a program to multiply 2 numbers"]

prompt = get_general_code_generation_prompt()
nodes_collections = []
llama2_responses = []
langchain_responses = []
llama2_code_responses = []
excel_report_path = 'C:\\v2\\Model Exploration\\Reports\\GeneralCodeGeneratorReport.xlsx'

for question in questions:
    print(question)
    
    llama2_response = Llama2LLM(question, [], prompt)
    llama2_responses.append(llama2_response)

    print(llama2_response)

    langchain_response = LangChainLLM(question, [], prompt)
    langchain_responses.append(langchain_response)
    
    print(langchain_response)

    llama2_code_response = LLama2CodeLLM(question, [], prompt)
    llama2_code_responses.append(llama2_response)

    print(llama2_response)

write_into_excel_3Models(nodes_collections,llama2_responses, langchain_responses, questions, excel_report_path, llama2_code_responses)
print("Report Generated...")