from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from src.tools import get_weather
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model="openrouter/auto",
    temperature=0,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",

)
memory = InMemorySaver()
agent = create_react_agent(
    model=llm,
    tools=[get_weather],
    prompt="""
    You are a helpful weather assistant.
    Rules:
    - Always use the get_weather tool.
    - Never guess weather information.
    - Return the tool output exactly as received.
    - Do not rephrase.
    - Do not change the city name.
    - Do not add extra explanations.
    """,
    checkpointer=memory
)




def ask_agent(question: str):
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        },
        config={
            "configurable": {
                "thread_id":"weather_chat_1"
        }
    }
)

    return response["messages"][-1].content