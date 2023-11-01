# https://github.com/wayne923/langchain-marketing-assistant/blob/main/app.py
# https://youtu.be/cYvNX3zxQ6c?si=t09nxU2ubhywfIT9

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
import pprint

load_dotenv()
API_KEY = os.environ.get("API_KEY")
os.environ["OPENAI_API_KEY"] = API_KEY
OpenAI.api_key = API_KEY

LL_MODEL = os.environ.get("LL_MODEL") # модель
print (f'LL_MODEL = {LL_MODEL}')

TEMPERATURE = float(os.environ.get("TEMPERATURE")) # Температура модели
print(f'TEMPERATURE={TEMPERATURE}')

# Models
# llm = OpenAI(model_name=LL_MODEL, temperature=TEMPERATURE)
llm = ChatOpenAI(model_name=LL_MODEL, temperature=TEMPERATURE)

# Prompt Template
blog_prompt_template = PromptTemplate(
    input_variables = ['product_description'],
    template = '''Write a Telegram post on {product_description}. Add line breaks. 
    Give the result in Russian'''
)

# Chain
blog_chain = LLMChain(llm=llm, prompt=blog_prompt_template,
                      verbose=True,
                      output_key='blog')

# Run
# product_description = 'best eco-friendly coffee'
# product_description = 'лучший экологически чистый кофе'
# print(blog_chain.run(product_description))

# Prompt 2
youtube_script_template = PromptTemplate(
    input_variables=['blog'],
    template = '''Write an engaging Youtube short video script
    for a new product based on this blog content: {blog}. Add line breaks. 
    Give the result in Russian'''
)

# Chain 2
youtube_script_chain = LLMChain(llm=llm, prompt=youtube_script_template,
                                verbose=True,
                                output_key='yt_script')

# Sequential Chain
simple_chain = SimpleSequentialChain(chains=[blog_chain,youtube_script_chain],
                                     verbose=True)
# Run
# product_description = 'best eco-friendly coffee'
# print(simple_chain.run(product_description))

# Prompt 3
youtube_visuals_template = PromptTemplate(
    input_variables=['yt_script','blog'],
    template='''You're an amazing director, generate the scene by scene
    Description for the Youtube video based on the following script: {yt_script}
    Here is additional blog content if additional context is needed: {blog}. Add line breaks. 
    Give the result in Russian'''
)

# Chain 3
youtube_visuals_chain = LLMChain(llm=llm, prompt=youtube_visuals_template,
                                 verbose=True,
                                 output_key='yt_visuals')

# Sequential Chain
marketing_automation_chain = SequentialChain(
    chains=[blog_chain, youtube_script_chain, youtube_visuals_chain],
    input_variables=['product_description'],
    output_variables=['blog','yt_script','yt_visuals'],
    verbose=True
)


def marketing_text(user_input):
    app_data = marketing_automation_chain(user_input)
    return app_data

if __name__ == '__main__':
    topic ="инновационная экологически чистая кофейная чашка"
    ans = marketing_text(topic)
    pprint.pprint(ans)
