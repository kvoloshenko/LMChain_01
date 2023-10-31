from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


llm = OpenAI(
    openai_api_key = "anyValueYouLike",
    temperature = 0,
    openai_api_base = "http://localhost:1234/v1",
    max_tokens = -1,
)

# Prompt Template
blog_prompt_template = PromptTemplate(
    input_variables = ['product_description'],
    template = 'Write a blog post on {product_description} Give the result in Russian'
)

# Chain
blog_chain = LLMChain(llm=llm, prompt=blog_prompt_template,
                      verbose=True,
                      output_key='blog')


# Prompt 2
youtube_script_template = PromptTemplate(
    input_variables=['blog'],
    template = '''Write an engaging Youtube short video script
    for a new product based on this blog content: {blog} Give the result in Russian'''
)

# Chain 2
youtube_script_chain = LLMChain(llm=llm, prompt=youtube_script_template,
                                verbose=True,
                                output_key='yt_script')

# Prompt 3
youtube_visuals_template = PromptTemplate(
    input_variables=['yt_script','blog'],
    template='''You're an amazing director, generate the scene by scene
    Description for the Youtube video based on the following script: {yt_script}
    Here is additional blog content if additional context is needed: {blog} Give the result in Russian'''
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

product_description = 'инновационная экологически чистая кофейная чашка'
chain_run_result = marketing_automation_chain(product_description)
print(type(chain_run_result))

