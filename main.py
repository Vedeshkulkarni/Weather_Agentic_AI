from src.agent import ask_agent


if __name__ == "__main__":

    print("🌦️ Weather Agent AI")
    print("Type 'exit' to quit\n")

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        response = ask_agent(question)

        print("\nAI:", response)