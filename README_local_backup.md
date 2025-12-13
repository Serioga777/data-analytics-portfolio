# Multi-Agent AI Research Framework

A comprehensive Python framework for building and researching multi-agent AI systems. This framework provides a solid foundation for creating intelligent agents that can collaborate, use tools, and solve complex tasks.

## 🚀 Features

- **Multiple Agent Types**: Researcher, Writer, and Analyzer agents with specialized capabilities
- **Extensible Architecture**: Easy to create custom agents by extending the base agent class
- **Tool Integration**: Built-in tools for web search, file operations, and calculations
- **Memory System**: Agents maintain conversation history and context
- **Orchestration**: Coordinate multiple agents to work together on complex workflows
- **Modular Design**: Clean separation of concerns for easy maintenance and extension

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- API keys for AI services (OpenAI, Anthropic, or Google AI)

## 🛠️ Installation

1. **Clone or navigate to this directory**
   ```bash
   cd "c:\Users\deathy\Documents\multi agent test"
   ```

2. **Create and activate a virtual environment** (already done)
   The Python environment has been configured for you.

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   copy .env.example .env
   ```
   Then edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ANTHROPIC_API_KEY=your_actual_api_key_here
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## 🏗️ Project Structure

```
multi agent test/
├── agents/                 # Agent implementations
│   ├── __init__.py
│   ├── base_agent.py      # Base agent class
│   ├── researcher_agent.py # Research specialist
│   ├── writer_agent.py    # Content creation specialist
│   └── analyzer_agent.py  # Data analysis specialist
├── tools/                  # Agent tools
│   ├── __init__.py
│   ├── web_search_tool.py
│   ├── file_operations_tool.py
│   └── calculation_tool.py
├── examples/              # Usage examples
│   ├── basic_example.py   # Simple agent interaction
│   └── advanced_example.py # Complex workflows
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🎯 Quick Start

### Basic Example

Run the basic example to see agents in action:

```bash
python examples/basic_example.py
```

This demonstrates:
- Initializing multiple agents
- Sequential task execution
- Agent memory and context

### Advanced Example

Run the advanced example for complex workflows:

```bash
python examples/advanced_example.py
```

This demonstrates:
- Multi-agent orchestration
- Deep research workflows
- Tool integration
- Report generation

## 💡 Usage

### Creating a Custom Agent

```python
from agents.base_agent import BaseAgent

class MyCustomAgent(BaseAgent):
    def __init__(self, name="Custom Agent"):
        super().__init__(
            name=name,
            role="Custom Specialist",
            goal="Achieve specific goals",
            backstory="Your agent's background",
            model="gpt-4-turbo-preview",
            temperature=0.7
        )
    
    def execute(self, task, context=None):
        # Implement your agent's logic
        result = {
            'agent': self.name,
            'task': task,
            'status': 'completed',
            'output': 'Your output here'
        }
        self.add_to_memory({'type': 'result', 'result': result})
        return result
```

### Using Multiple Agents

```python
from agents import ResearcherAgent, WriterAgent

# Initialize agents
researcher = ResearcherAgent()
writer = WriterAgent()

# Execute workflow
research = researcher.execute("Research AI trends")
article = writer.execute(
    "Write an article", 
    context={'research': research['output']}
)
```

### Adding Custom Tools

```python
class MyCustomTool:
    def __init__(self):
        self.name = "my_tool"
        self.description = "What my tool does"
    
    def execute(self, *args, **kwargs):
        # Tool logic here
        return result
```

## 🔧 Configuration

Edit `config.py` or use environment variables to configure:

- **API Keys**: OpenAI, Anthropic, Google AI
- **Model Settings**: Default model, temperature, max tokens
- **Agent Behavior**: Verbosity, max iterations
- **Logging**: Log level and output

## 📊 Agent Types

### ResearcherAgent
- Specializes in information gathering and research
- Lower temperature (0.5) for factual accuracy
- Methods: `execute()`, `deep_research()`

### WriterAgent
- Specializes in content creation
- Higher temperature (0.8) for creativity
- Methods: `execute()`, `revise()`

### AnalyzerAgent
- Specializes in data analysis and insights
- Low temperature (0.3) for analytical precision
- Methods: `execute()`, `compare_results()`, `trend_analysis()`

## 🛠️ Available Tools

### WebSearchTool
Search the web for current information
```python
search_tool = WebSearchTool(api_key="your_key")
results = search_tool.search("AI agents", max_results=5)
```

### FileOperationsTool
Read, write, and manage files
```python
file_tool = FileOperationsTool()
content = file_tool.read_file("data.txt")
file_tool.write_file("output.txt", "content")
```

### CalculationTool
Perform mathematical calculations
```python
calc_tool = CalculationTool()
result = calc_tool.calculate("2 + 2 * 10")
stats = calc_tool.statistics([1, 2, 3, 4, 5])
```

## 🔌 Integrating Real LLMs

To connect agents to actual AI models:

1. **Ensure API keys are set** in `.env`

2. **Implement LLM calls** in agent `execute()` methods:
   ```python
   from openai import OpenAI
   
   client = OpenAI(api_key=settings.openai_api_key)
   response = client.chat.completions.create(
       model=self.model,
       messages=[{"role": "user", "content": task}],
       temperature=self.temperature
   )
   ```

3. **Use frameworks** like CrewAI, AutoGen, or LangGraph for advanced features

## 📚 Learning Resources

- **CrewAI**: Multi-agent orchestration framework
- **AutoGen**: Microsoft's multi-agent conversation framework
- **LangChain**: Building LLM applications
- **LangGraph**: State management for agent workflows

## 🤝 Contributing

This is a research framework designed for experimentation. Feel free to:
- Add new agent types
- Create custom tools
- Implement new workflows
- Integrate different LLM providers

## 📝 License

This framework is for personal research and development.

## 🆘 Troubleshooting

**Import errors**: Make sure all dependencies are installed
```bash
pip install -r requirements.txt
```

**API errors**: Verify your API keys in `.env` file

**Module not found**: Ensure you're running from the project root directory

## 🎓 Next Steps

1. ✅ Install dependencies
2. ✅ Configure API keys
3. 🔄 Run basic example
4. 🔄 Run advanced example
5. 🔄 Create your custom agent
6. 🔄 Build your first workflow
7. 🔄 Integrate with real LLM APIs

---

**Happy building! 🚀**

For questions or issues, review the examples and documentation in the code.
