
# Llama2 Model | Together ai
import together
import os
together.api_key = os.environ["TOGETHER_API_KEY"]
#together.api_key = "a966e2da8d4024d7aefb48eba1c4d45e59ebc3fd7b2e139f7ea869b7fe8e98db"

class TogetherAILLM:
    def __init__(self, model_id, temperature,  metadata = "",max_tokens=1000):
        self.model_id = model_id
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.metadata = metadata
        
    def _start_model(self):
        together.Models.start(self.model_id)

    def _stop_model(self):
        together.Models.stop(self.model_id)

    def _complete(self, prompt, stop=["</s>"]):
        self._start_model()
        output = together.Complete.create(
            prompt=prompt,
            model=self.model_id,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            top_k=90,
            top_p=0.8,
            repetition_penalty=1.1,
            stop=stop,
        )
        self._stop_model()
        return output
    
    def predict(self, prompt):
        output = self._complete(prompt)
        return output["output"]["choices"][0]["text"]
    
#     def _generate_chat_prompt(self, user_question, source_nodes):
# #         return f"""A dialog, where User interacts with AI. AI is helpful, kind, obedient, honest, and knows its own limits.
# # User: Hello, AI.
# # AI: Hello! How can I assist you today?
# # User: {user_question}
# # AI:"""

#         return """You are an expert in providing the summarized answer for the given user_question with the provided source nodes.
# Please find the user_question below:
# {user_question}

# Use these source_nodes below to summarize your answer for the user_question provided :
# {source_nodes}

# Answer:
# """
    
    def predict_messages(self, user_question, source, prompt):
        #output = self._complete(prompt=self._generate_chat_prompt(user_question, source_nodes), stop=["User:", "</s>"])
        formatted_prompt = prompt.format(user_question=user_question, source=source)
        #formatted_prompt = prompt
        #print(formatted_prompt)
        output = self._complete(prompt=formatted_prompt, stop=["User:", "</s>"])
        return output["output"]["choices"][0]["text"].rstrip(r"\nUser:").rstrip(r"</s>")  # Remove stop keywords at the end
    
    def metadata():
        print("metadata")


def Llama2LLM(question, source, prompt):
    llm = TogetherAILLM(model_id="togethercomputer/llama-2-70b-chat", temperature=0.1)
    response = llm.predict_messages(question, source, prompt)
    return response


def LLama2CodeLLM(question, source, prompt):
    llm = TogetherAILLM(model_id="togethercomputer/CodeLlama-34b-Instruct", temperature=0.1)
    response = llm.predict_messages(question, source, prompt)
    return response

def DefogSQLCoder(question, source, prompt):
    llm = TogetherAILLM(model_id="defog/sqlcoder", temperature=0.1)
    response = llm.predict_messages(question, source, prompt)
    return response

# ChatOpenAI LLMChain gpt-3.5-turbo model
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import os

MODEL_NAME = os.environ.get("OPENAI_CHAT_MODEL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def LangChainLLM(user_question, source, prompt):

    prompt_template = prompt

    llm_chain = LLMChain(
        llm=ChatOpenAI(
            temperature=0.1,
            verbose=True,
            model=MODEL_NAME,
            openai_api_key=OPENAI_API_KEY,
            max_retries=3
            ),
        prompt=PromptTemplate.from_template(prompt_template)
        #prompt= Prompt(prompt_template)
        #prompt=prompt_template
        )


    res = llm_chain(inputs={
        "user_question" : user_question,
        "source" : source
    })

    return res['text']