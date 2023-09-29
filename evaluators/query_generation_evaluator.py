from dotenv import load_dotenv
load_dotenv()

from utilities.AI_Lookups import Llama2LLM, LangChainLLM, DefogSQLCoder, LLama2CodeLLM
from utilities.create_excel_report import write_into_excel
from utilities.prompts import get_spartans_query_generator_prompt

questions = ["Which mission has run more kilometers in Spartans Challenge?",]
                # "How many people signed up for Spartans Challenge?",
                # "How many kilometres were run by PES mission?",
                # "List the total kilometers run by each mission in Sparatans Challenge."]

prompt = get_spartans_query_generator_prompt()
nodes_collections = []
llama2_responses = []
langchain_responses = []
excel_report_path = 'C:\\v2\\Model Exploration\\Reports\\QueryGeneratorReport.xlsx'

for question in questions:
    print(question)

    res = Llama2LLM(question, [], prompt)    
    print(res)

#     llama2_response = Llama2LLM(question, [], prompt)
#     llama2_responses.append(llama2_response)

#     print(llama2_response)

#     langchain_response = LangChainLLM(question, [], prompt)
#     langchain_responses.append(langchain_response)
    
#     print(langchain_response)

# write_into_excel(nodes_collections,llama2_responses, langchain_responses, questions, excel_report_path)
# print("Report Generated...")