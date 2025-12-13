# Local Llama Integration Guide

## 🦙 Integrate Your Local Llama Model

This framework now supports local Llama models via **Ollama**!

## Quick Setup

### 1. Install Ollama (if not already installed)

**Windows:**
1. Download from: https://ollama.ai
2. Run the installer
3. Restart your terminal

**Already have Ollama?** Skip to step 2!

### 2. Start Ollama Server

```powershell
ollama serve
```

Leave this running in the background.

### 3. Pull a Llama Model

Open a **new terminal** and run:

```powershell
# Llama 2 (7B - recommended for most PCs)
ollama pull llama2

# Or try other models:
ollama pull llama3        # Llama 3
ollama pull mistral       # Mistral 7B
ollama pull codellama     # Code-specialized
```

### 4. Test the Integration

```powershell
python examples\llama_example.py
```

## Usage

### Basic Usage

```python
from agents.llama_agent import LlamaAgent

# Create a Llama-powered agent
agent = LlamaAgent(
    name="My Assistant",
    role="AI Helper",
    model_name="llama2"  # or llama3, mistral, etc.
)

# Execute a task
result = agent.execute("What are multi-agent systems?")
print(result['output'])
```

### Direct LLM Access

```python
from llm_integration import LocalLlamaLLM

# Create LLM instance
llm = LocalLlamaLLM(model_name="llama2")

# Generate text
response = llm.generate("Explain AI in simple terms")
print(response['content'])

# Chat mode
messages = [
    {"role": "user", "content": "Hello!"}
]
response = llm.chat(messages)
print(response['content'])
```

### Multi-Agent Workflow

```python
from agents.llama_agent import LlamaAgent

# Create specialized agents
researcher = LlamaAgent(
    name="Researcher",
    role="Research Analyst",
    model_name="llama2",
    temperature=0.5  # More focused
)

writer = LlamaAgent(
    name="Writer",
    role="Content Writer",
    model_name="llama2",
    temperature=0.8  # More creative
)

# Execute workflow
research = researcher.execute("Research AI trends")
article = writer.execute(
    "Write an article",
    context={'research': research['output']}
)
```

## Available Models

Check what models you have:
```powershell
ollama list
```

Popular models:
- **llama2** - Meta's Llama 2 (7B, 13B, 70B)
- **llama3** - Meta's Llama 3 (better performance)
- **mistral** - Mistral 7B (fast and capable)
- **codellama** - Code-specialized Llama
- **neural-chat** - Intel's conversational model
- **phi** - Microsoft's small but powerful model

Pull any model:
```powershell
ollama pull <model-name>
```

## Files Created

- **`llm_integration.py`** - Local Llama LLM interface
- **`agents/llama_agent.py`** - Llama-powered agent class
- **`examples/llama_example.py`** - Complete example with tests

## Commands

### Run the Llama integration example:
```powershell
python examples\llama_example.py
```

### Check if Ollama is running:
```powershell
ollama list
```

### Start Ollama (if not running):
```powershell
ollama serve
```

## Troubleshooting

### "Ollama not running" error
- Start Ollama: `ollama serve`
- Make sure port 11434 is not blocked

### "No models found" error
- Pull a model: `ollama pull llama2`
- Check models: `ollama list`

### Slow responses
- Try a smaller model (llama2:7b vs llama2:70b)
- Check CPU/RAM usage
- Consider using GPU acceleration (Ollama auto-detects)

## Advantages of Local LLM

✅ **Privacy** - Data stays on your PC
✅ **No API costs** - Free to use
✅ **Offline** - Works without internet
✅ **No rate limits** - Use as much as you want
✅ **Customizable** - Fine-tune models for your needs

## Next Steps

1. **Run the example**: `python examples\llama_example.py`
2. **Try different models**: `ollama pull llama3`
3. **Build custom agents** using `LlamaAgent`
4. **Combine** local Llama with cloud APIs for hybrid approach

---

**Your multi-agent framework now has local AI power! 🚀**
