# Architecture 

# Text goes to 2 parallel models ChatOpenAi() and ChatAnthropic()
# 1st will generate notes and 2nd will generate quiz (parallely)
# Now pass quiz and notes into 3rd model which will combine them 
# And then show it to user 

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

# Generate Prompts 
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',   # Notes 
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}', # Quiz 
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}', # Merge (notes + quiz)
    input_variables=['notes', 'quiz']
)

# Create strOutputParser()
parser = StrOutputParser()

# Now Develop chains in two parts -> 1st Parallel chain (for parallel chain we need runnableParallel)
# Runnable Parallel -> Is a kind of runnable which helps to execute multiple chains parallely  -> from langchain.schema.runnable import RunnableParallel

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser, # 1st parallel chain -> prompt1 -> model -> parser 
    'quiz': prompt2 | model2 | parser   # 2nd Chain -> promp2 -> model -> parser 
})

# Now create merge chain here pass prompt to any model 1 or 2 
merge_chain = prompt3 | model1 | parser

# Now combine parallel chain and merge chain before invoking 
chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.
The advantages of support vector machines are:
Effective in high dimensional spaces.
Still effective in cases where number of dimensions is greater than the number of samples.
Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.
The disadvantages of support vector machines include:
If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.
SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).
The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()