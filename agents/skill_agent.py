import openai
import os
import asyncio
from tools import get_career_roadmap

class SkillAgent:
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        self.name = "Skill Builder"

    async def process(self, user_input, runner=None):
        system_prompt = """You are a Skill Builder Agent. You:
        - Analyze career paths and identify skills
        - Suggest learning resources
        - Share roadmaps for progression
        """

        try:
            roadmap = get_career_roadmap(user_input)

            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model="deepseek/deepseek-r1:free",
                extra_headers={"X-OpenRouter-Model": "deepseek/deepseek-r1:free"},
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Create a skill roadmap for: {user_input}. Here is the data: {roadmap}"}
                ],
                max_tokens=600,
                temperature=0.6
            )

            result = response.choices[0].message.content

            if any(k in user_input.lower() for k in ['job', 'salary', 'work', 'company']):
                if runner:
                    handoff_result = await runner.handoff("job", user_input)
                    return f"{result}\n\n🔄 Handing off to Job Agent:\n{handoff_result}"

            return f"🛠️ Skill Development Plan:\n{result}"

        except Exception as e:
            return f"❌ SkillAgent Error: {e}"
