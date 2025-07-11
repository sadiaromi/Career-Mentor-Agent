import openai
import os
import asyncio

class CareerAgent:
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        self.name = "Career Explorer"

    async def process(self, user_input, runner=None):
        system_prompt = """You are a Career Explorer Agent. Your role is to:
        1. Analyze user interests and suggest relevant career fields.
        2. Ask clarifying questions about their preferences.
        3. Recommend when to handoff to SkillAgent or JobAgent.
        4. Be encouraging and supportive.
        """

        try:
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model="deepseek/deepseek-r1:free",
                extra_headers={"X-OpenRouter-Model": "deepseek/deepseek-r1:free"},
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=700,
                temperature=0.7
            )

            result = response.choices[0].message.content

            if any(k in user_input.lower() for k in ['skills', 'learn', 'roadmap', 'requirements']):
                if runner:
                    handoff_result = await runner.handoff("skill", user_input)
                    return f"{result}\n\n🔄 Handing off to Skill Agent:\n{handoff_result}"
            elif any(k in user_input.lower() for k in ['job', 'salary', 'work', 'company', 'role']):
                if runner:
                    handoff_result = await runner.handoff("job", user_input)
                    return f"{result}\n\n🔄 Handing off to Job Agent:\n{handoff_result}"

            return result

        except Exception as e:
            return f"❌ CareerAgent Error: {e}"
