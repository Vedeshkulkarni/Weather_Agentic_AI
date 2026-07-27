from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from src.tools import get_weather
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")

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
                "thread_id": "weather_chat"
            }
        }
    )

    return response["messages"][-1].content[0]["text"]