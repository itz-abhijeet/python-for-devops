from strands import Agent
from strands.models.ollama import OllamaModel
import psutil

# Collect system metrics
cpu = psutil.cpu_percent(interval=1)
disk = psutil.disk_usage('/').percent
memory = psutil.virtual_memory().percent

# Define agent behavior
SYSTEM_PROMPT = """
You are a System Health Analysis Agent.
You analyze system metrics and identify performance risks.
You provide root cause hypotheses and DevOps recommendations.
You never execute system commands.
"""

# Configure local LLM via Ollama
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2"
)

# Initialize AI agent
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=ollama_model
)

# Send metrics to agent for analysis
response = agent(
    f"""
    Metric: CPU | Value: {cpu}% | Threshold: 80%
    Metric: Disk | Value: {disk}% | Threshold: 80%
    Metric: Memory | Value: {memory}% | Threshold: 80%

    Analyze risk and suggest actions.
    """
)

# Write analysis report to file
with open("system_health_report.txt", "w") as f:
    f.write(str(response))

print("Report written to system_health_report.txt")
