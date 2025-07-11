import openai
import os
import asyncio

class JobAgent:
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        self.name = "Job Market Expert"

    async def process(self, user_input, runner=None):
        system_prompt = """You are a Job Market Expert Agent. You:
        - Provide real-world job role information
        - Share salary ranges and demand
        - Suggest companies or sectors
        - Offer job search tips
        """

        try:
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model="deepseek/deepseek-r1:free",
                extra_headers={"X-OpenRouter-Model": "deepseek/deepseek-r1:free"},
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Give job market insights for: {user_input}"}
                ],
                max_tokens=600,
                temperature=0.6
            )

            result = response.choices[0].message.content

            if any(k in user_input.lower() for k in ['other careers', 'different field', 'explore more']):
                if runner:
                    handoff_result = await runner.handoff("career", user_input)
                    return f"{result}\n\n🔄 Handing off to Career Agent:\n{handoff_result}"

            return f"💼 Job Market Insights:\n{result}"

        except Exception as e:
            return f"❌ JobAgent Error: {e}"
