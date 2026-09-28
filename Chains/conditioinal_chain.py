# Here user will give some feedback on our product and our model will add sentiments to it -> currently we will only show sentiments back (pos or neg)
# Model will extract whether it is positive or negatice 
# Now based on sentiment -> we will again send feedback to model and now ask it to generate response accordingly 

# for response two models one for pos sentiment and othewr for neg sentiment -> imp thing is only one of them will run based on sentiment 

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

# We had no gurantee that for ("This is phone is terrible") what kind of output will model generate can be either "Positive or negative or Phone is positive or Negative sentiment"
# So we had no control on stucture of output -> therefore to structure the output we need pydanticOutputParser which is second parser here 

class Feedback(BaseModel):  # class is needed for pydantic
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)    

# Create Prompts 
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke('feedback': 'This is a terrible Phone').sentiment
# Now result will be either "positive" or "negative"


prompt2 = PromptTemplate(   # For +ve feedback
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(   # For -ve feedback
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Now branching part where we will create branches and either of them would work -> for this we require runnableBranch, which helps to execute if-else containing chains or conditional chains 

branch_chain = RunnableBranch(
    # (condition, chain)
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),      # function getting input x (which is response +ve or -ve) and if x is +ve chain -> prompt2->model->parser
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),      # function getting input x (which is response +ve or -ve) and if x is -ve chain -> prompt3->model->parser
    RunnableLambda(lambda x: "could not find sentiment")   # Default chain but we have to create runnableLambda here becoz (lambda x: "could not find sentiment") is not chain but we have to execute a chain
)
# RunnableLambda -> converts lambda function to runnable and if converted into runnable then we can use it as a chain 

chain = classifier_chain | branch_chain         # Merge both chains and create a final chain then invoke this final chain 
print(chain.invoke({'feedback': 'This is a beautiful phone'}))
chain.get_graph().print_ascii()
