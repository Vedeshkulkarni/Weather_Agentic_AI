# 🌦️ Weather Agentic AI

An AI-powered weather assistant built using **LangGraph, LangChain, Gemini LLM, OpenWeatherMap API, and Streamlit**.

This project uses an **Agentic AI architecture**, where the AI agent can understand user queries, decide when to use external tools, fetch real-time weather information, and provide a natural language response.

---

# 🚀 Features

* 🤖 AI Agent built with **LangGraph**
* 🧠 Gemini LLM integration using **LangChain**
* 🔧 Intelligent tool calling
* 🌍 Real-time weather information using OpenWeatherMap API
* 💬 Interactive web interface using Streamlit
* 🔐 Secure API key management using `.env`
* ⚡ Fast responses with AI-generated answers
* 🏗️ Modular project structure

---

# 🏗️ Architecture

```
                 User
                  |
                  |
            Weather Query
                  |
                  v
            Streamlit UI
                  |
                  v
          LangGraph AI Agent
                  |
                  v
             Gemini LLM
                  |
        Decides Tool Usage
                  |
                  v
          Weather API Tool
                  |
                  v
       OpenWeatherMap API
                  |
                  v
          Weather Information
                  |
                  v
        AI Generated Response
                  |
                  v
                 User
```

---

# 📂 Project Structure

```
Weather_Agentic_AI/
│
├── app.py                    # Streamlit web application
├── main.py                   # Terminal execution (optional)
├── requirements.txt          # Project dependencies
├── .env                      # API keys
├── .gitignore
│
├── src/
│   │
│   ├── agent.py              # LangGraph agent implementation
│   ├── tools.py              # Weather API tool
│   ├── config.py             # Configuration settings
│   └── prompts.py            # Agent prompts
│
└── README.md
```

---

# 🛠️ Technologies Used

| Technology         | Purpose                                |
| ------------------ | -------------------------------------- |
| Python             | Programming language                   |
| uv                 | Python package and environment manager |
| LangGraph          | Agent workflow creation                |
| LangChain          | LLM application framework              |
| Gemini             | Large Language Model                   |
| OpenWeatherMap API | Real-time weather data                 |
| Streamlit          | User interface                         |
| python-dotenv      | Environment variable management        |

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-github-repository-url>

cd Weather_Agentic_AI
```

---

## 2. Create Virtual Environment using uv

```bash
uv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 4. Install Dependencies

Using uv:

```bash
uv pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file in the project root directory.

Add your API keys:

```env
GOOGLE_API_KEY=your_gemini_api_key

OPENWEATHER_API_KEY=your_openweathermap_api_key
```

### Required APIs:

* Gemini API Key → Used for AI responses
* OpenWeatherMap API Key → Used for real-time weather information

---

# ▶️ Running the Application

## Start Streamlit Web App

Run:

```bash
uv run streamlit run app.py
```

The application will open in your browser.

---

## Run Terminal Version (Optional)

```bash
uv run python main.py
```

Example:

```
You: What is the weather in Delhi?

AI:
The current weather in Delhi is sunny with a temperature of 32°C.
```

---

# 💡 Example Queries

```
What is the weather in Bangalore?

Temperature in Mumbai?

How is the weather in Delhi today?

Tell me weather of Kalaburagi

Weather forecast in Chennai
```

---

# 🔄 Working Flow

1. User enters a weather query.
2. Streamlit sends the request to the AI agent.
3. LangGraph manages the agent workflow.
4. Gemini understands the user request.
5. Agent decides whether a tool is needed.
6. Weather tool calls OpenWeatherMap API.
7. Weather data is returned to the agent.
8. Gemini generates the final human-readable response.
9. User receives the answer.

---

# 🔒 Security

* API keys are stored in `.env`.
* `.env` should not be uploaded to GitHub.
* Sensitive files are ignored using `.gitignore`.

Example `.gitignore`:

```
.env
.venv/
__pycache__/
```

---

# 📦 Requirements

Main dependencies:

```
streamlit
langchain
langchain-core
langchain-google-genai
langgraph
python-dotenv
requests
pydantic
```

---

# 🚀 Future Improvements

* Add weather forecast prediction
* Add weather charts and visualization
* Add voice input support
* Add location auto-detection
* Add conversation memory
* Deploy using cloud platforms
* Add multiple weather data providers

---

Built with ❤️ using:

* Python
* LangGraph
* LangChain
* Gemini
* Streamlit
* OpenWeatherMap API
