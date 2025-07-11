# 💼 Career Mentor Agent

An AI-powered multi-agent assistant that helps students explore career options, build skill roadmaps, and understand job market trends — all through natural conversations!

---

## 🚀 Features

- 🤖 **CareerAgent**: Suggests career paths based on user interests.
- 🛠️ **SkillAgent**: Recommends skill-building plans using a roadmap tool.
- 💼 **JobAgent**: Shares real-world job roles, salaries, and market demand.
- 🔄 **Multi-Agent Handoff**: Seamless switching between agents based on conversation context.
- 🌐 **Chainlit Interface**: Easy-to-use web interface.
- 🔐 **OpenRouter API Integration** using free model.

---

## 🧠 How It Works

1. Start with the **CareerAgent** to discuss your interests.
2. Based on your query, it may hand off to:
   - **SkillAgent**: If you're asking about skills, roadmaps, or learning paths.
   - **JobAgent**: If you're asking about salaries, roles, or job sectors.
3. Each agent is powered by its own prompt logic and backed by OpenRouter's AI models.

---

## 📁 Folder Structure

```
career_mentor_agent/
│
├── agents/
│ ├── career_agent.py # Career path recommendations
│ ├── skill_agent.py # Skill roadmap + tool usage
│ └── job_agent.py # Job market information
│
├── runner/
│ └── agent_runner.py # Agent manager and handoff logic
│
├── tools.py # Custom roadmap generator tool
│
├── chainlit_app.py # Main Chainlit UI app
├── .env # API key 

```


---

## 🔧 Installation & Setup

1. **Create and activate a virtual environment**
   ```bash
   uv venv
   venv\Scripts\activate  #on Windows

   ```

2. **Create .env file & Add OpenRouter API key**
  ```bash
OPENROUTER_API_KEY=your_api_key_here

```

3. **Run the app**
  ```bash
chainlit run chainlit_app.py

```
---

## ⚙️ Tech Stack

- 🧠 OpenAI-compatible API (via OpenRouter)

- 🗃️ Multi-agent architecture

- 🛠️ Custom skill roadmap tool

- 💬 Chainlit for interactive UI

- 🐍 Python 3.13

---

## 🧪 Sample Questions to Try

- What career suits someone who loves solving puzzles?

- What skills are required to become a UI/UX designer?

- What's the average salary for a data scientist?

- I want to switch to cybersecurity — what should I learn?


