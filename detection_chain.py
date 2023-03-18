from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms import OpenAIChat
from langchain.agents import load_tools, ZeroShotAgent

from langchain.agents import AgentExecutor, Agent, initialize_agent, Tool

from langchain.agents.react.base import ReActDocstoreAgent
from langchain.agents.self_ask_with_search.base import SelfAskWithSearchAgent

from earth_prompt import PREFIX, SUFFIX

import os
from litewiki import wiki_summary, wiki_summary_description

os.environ["SERPER_API_KEY"] = "key"

openai = OpenAIChat(
  temperature=0.1,
  openai_api_key="key",
  model="gpt-3.5-turbo",
  verbose=True)

# tools = load_tools([r for r in ["google-serper"]], llm=openai)

# tools += [
#   Tool(name="WikipediaSummary",
#        func=wiki_summary,
#        description=wiki_summary_description)
# ]

# llm_chain = LLMChain(llm=openai, verbose=True)

# react_agent = ReActDocstoreAgent(llm=openai, llm_chain=llm_chain)
# self_ask_agent = SelfAskWithSearchAgent(llm=openai, llm_chain=llm_chain)

tools = [
  Tool(name="WikipediaSummary",
       func=wiki_summary,
       description=wiki_summary_description),
  # Tool(
  #   name="ReAct",
  #   func=react_agent.run,
  #   description="useful for when you need to answer questions about documents"
  # ),
  # Tool(name="Self-Ask",
  #      func=self_ask_agent.run,
  #      description=
  #      "useful for when you need to answer questions that require reasoning")
]

#prefix="", suffix="", format_instructions=""
#agent_prompt = ZeroShotAgent.create_prompt(tools=tools )

# chain = LLMChain(prompt=agent_prompt, llm=opeai, verbose=True, memory=ConversationBufferWindowMemory(k=2))

# agent = ZeroShotAgent.from_llm_and_tools(
#   llm=openai,
#   tools=tools,
#   verbose=True,
#   prefix=PREFIX,
#   suffix=SUFFIX,
#   format_instructions=FORMAT_INSTRUCTIONS)

agent = ZeroShotAgent.from_llm_and_tools(llm=openai,
                                         tools=tools,
                                         verbose=True,
                                         prefix=PREFIX,
                                         suffix=SUFFIX)

#agent = initialize_agent(tools=tools, llm=opeai, agent="conversational-react-description", verbose=True)

executer = AgentExecutor(agent=agent,
                         tools=tools,
                         verbose=True,
                         max_iterations=4)

# output = executer({"input": "Lawyer", "chat_history": []})
# print(output)
