class AgentRunner:
    def __init__(self, agents):
        self.agents = agents
        self.current_agent = None

    async def run(self, agent_name, user_input):
        if agent_name not in self.agents:
            return f"⚠️ Agent '{agent_name}' not found."

        self.current_agent = agent_name
        agent = self.agents[agent_name]

        return await agent.process(user_input, runner=self)

    async def handoff(self, target_agent, user_input):
        if target_agent not in self.agents:
            return f"⚠️ Cannot handoff to '{target_agent}' — agent not found."

        previous_agent = self.current_agent
        self.current_agent = target_agent
        agent = self.agents[target_agent]

        result = await agent.process(user_input, runner=self)

        return f"🔄 [Handoff from **{previous_agent}** to **{target_agent}**]\n{result}"

    def get_current_agent(self):
        return self.current_agent

    def list_agents(self):
        return list(self.agents.keys())
