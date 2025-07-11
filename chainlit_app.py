import chainlit as cl
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent
from runner.agent_runner import AgentRunner

# 🤖 Initialize agents
runner = AgentRunner({
    "career": CareerAgent(),
    "skill": SkillAgent(),
    "job": JobAgent()
})

# 🚀 Welcome message when chat starts
@cl.on_chat_start
async def start_chat():
    cl.user_session.set("runner", runner)
    cl.user_session.set("agent", "career")
    welcome = (
        "🎯 **Welcome to Career Mentor Agent!**\n\n"
        "I'm here to guide you through your career journey step-by-step.\n"
        "Ask me about career options, skill-building plans, or job market trends.\n\n"
        "✨ Example questions you can try:\n"
        "- *What career suits someone who likes coding and problem-solving?*\n"
        "- *What skills are required to become a UI/UX designer?*\n"
        "- *What's the average salary of a data analyst?*\n"
        "\nLet's get started — tell me what you're passionate about!"
    )
    await cl.Message(content=welcome).send()

# 💬 Handle user messages and route them to the right agent
@cl.on_message
async def on_message(message: cl.Message):
    runner: AgentRunner = cl.user_session.get("runner")
    agent_name: str = cl.user_session.get("agent")

    # 🔁 Process the message with the current agent
    response = await runner.run(agent_name, message.content)

    # 🔄 Update the current agent after processing
    cl.user_session.set("agent", runner.get_current_agent())

    # 📨 Send the response back to the user
    await cl.Message(content=response).send()
