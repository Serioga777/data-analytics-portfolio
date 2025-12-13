# Getting Started with Multi-Agent AI Framework

## Quick Command Reference

### Verify Installation
```powershell
python setup_check.py
```

### Run Examples (No API Key Needed)
```powershell
# Basic agent interaction
python examples\basic_example.py

# Advanced orchestration
python examples\advanced_example.py
```

### Run AI-Powered Examples (API Key Required)
```powershell
# CrewAI framework
python examples\crewai_example.py

# AutoGen framework
python examples\autogen_example.py
```

### Configure API Keys
```powershell
# Copy template
copy .env.example .env

# Edit .env file and add your keys:
# OPENAI_API_KEY=sk-your-key-here
```

## Example Output

When you run `python examples\basic_example.py`, you should see:

```
================================================================================
Multi-Agent Framework - Basic Example
================================================================================

Initializing agents...
✓ AI Researcher: Senior Research Analyst
✓ Tech Writer: Senior Content Writer
✓ Data Analyst: Senior Data Analyst

--------------------------------------------------------------------------------
Task 1: Research Phase
--------------------------------------------------------------------------------
Research completed by AI Researcher
Status: completed

... (workflow continues)

✓ Multi-agent workflow completed successfully!
```

## Your First Custom Agent

Create a file `my_agent.py`:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from agents.base_agent import BaseAgent

class MyCustomAgent(BaseAgent):
    def __init__(self, name="My Agent"):
        super().__init__(
            name=name,
            role="Custom Specialist",
            goal="Your agent's goal",
            backstory="Your agent's background"
        )
    
    def execute(self, task, context=None):
        print(f"{self.name} is working on: {task}")
        
        result = {
            'agent': self.name,
            'task': task,
            'status': 'completed',
            'output': f'Completed: {task}'
        }
        
        self.add_to_memory({'type': 'result', 'result': result})
        return result

# Test it
if __name__ == "__main__":
    agent = MyCustomAgent()
    result = agent.execute("Test task")
    print(result)
```

Run it:
```powershell
python my_agent.py
```

## Common Tasks

### Install Additional Packages
```powershell
# Activate virtual environment (should be automatic)
.venv\Scripts\Activate.ps1

# Install package
pip install package-name

# Update requirements
pip freeze > requirements.txt
```

### Update Dependencies
```powershell
pip install --upgrade -r requirements.txt
```

### Run Tests
```powershell
pytest
```

### Format Code
```powershell
black .
```

## Troubleshooting

### Import Errors
If you get `ModuleNotFoundError`:
1. Make sure you're in the project directory
2. Check that virtual environment is activated
3. Verify dependencies are installed: `pip list`

### API Errors
If you get API errors:
1. Check `.env` file exists
2. Verify API keys are correct
3. Ensure you have credits/quota on your API account

### Permission Errors
If you get permission errors:
1. Run PowerShell as Administrator (if needed)
2. Check file permissions
3. Ensure antivirus isn't blocking files

## Project Files Explained

- **agents/** - Where agent classes live
- **tools/** - Reusable tools for agents
- **examples/** - Working examples to learn from
- **config.py** - Central configuration
- **.env** - Your API keys (create from .env.example)
- **requirements.txt** - All dependencies
- **setup_check.py** - Verify installation

## What's Next?

1. ✅ Run basic_example.py
2. ✅ Read the agent code in agents/
3. ⏭️ Create your custom agent
4. ⏭️ Add API keys and try AI examples
5. ⏭️ Build your first multi-agent workflow

---

**Need help?** Check README.md and INSTALLATION.md for detailed documentation.
