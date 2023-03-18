from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
# from langchain.llms import ChatOpenAI
from langchain.llms import OpenAIChat, OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain import OpenAI, SerpAPIWrapper, LLMChain

search = SerpAPIWrapper(
  serpapi_api_key=
  "key")
tools = [
  Tool(
    name="Character Search",
    func=search.run,
    description=
    "useful for when you need to search for the role-play personality characteristics for the or answer questions about current events or the current state of the world. the input to this should be a single search term."
  ),
]

openai = OpenAI(
  temperature=0.1,
  openai_api_key="key",
  model="gpt-3.5-turbo",
  verbose=True)

memory = ConversationBufferMemory(memory_key="chat_history",
                                  return_messages=True)

# You role is to create a detailed and thoroughly built prompt for chatGPT to roleplay the character specified by the user. Provide the AI with knowledge limitation, speech style, and example sentences so it can build a good understanding of the character

prefix = """Your rols is to simulate (roleplay): '{character}'. Answer user questions and engage in helpful conversation but speaking as a {character} might speak. You have access to the following tools:"""

suffix = """Begin! Remember to speak as a {character} when giving your final answer.

Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
  tools,
  prefix=prefix,
  suffix=suffix,
  input_variables=["input", "agent_scratchpad", "character"])

llm_chain = LLMChain(prompt=prompt, llm=openai, verbose=True)

# agent_chain = initialize_agent(tools,
#                                openai,
#                                agent="chat-conversational-react-description",
#                                verbose=True,
#                                memory=memory)

tool_names = [tool.name for tool in tools]
agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)

agent_executor = AgentExecutor.from_agent_and_tools(agent=agent,
                                                    tools=tools,
                                                    verbose=True)


def message(s) -> str:
  result = agent_executor.run(input=s, character='Programmer')
  return result
