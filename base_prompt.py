# flake8: noqa
# PREFIX = """User will send few-word input, you should understand it, classify it, and provide the following as best you can: Classifcation: "{class}", Prompt:

# ```
# AI:
# Classification: ""(result)""
# Prompt: a detailed prompt describing (result) in the form of: (I'm ...)
# ```
PREFIX = """
You role is to understand and classify "{input}" and reply strictly with the following format:
```
AI: classification: <class>, <prompt>

where prompt is a detailed prompt describing the input in the form of: (I'm ...)
```

You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""
SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""
