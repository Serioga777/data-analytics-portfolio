"""
Ollama Diagnostics - Check your local LLM setup
"""
import requests
import json


def check_ollama_server():
    """Check if Ollama server is running"""
    print("=" * 80)
    print("Ollama Diagnostics")
    print("=" * 80)
    
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✓ Ollama server is running")
            data = response.json()
            models = data.get("models", [])
            
            if models:
                print(f"\n✓ Found {len(models)} model(s):")
                for model in models:
                    name = model.get("name", "unknown")
                    size = model.get("size", 0) / (1024**3)  # Convert to GB
                    print(f"  - {name} ({size:.1f} GB)")
                return True, models
            else:
                print("\n⚠️  No models found")
                print("Pull a model with: ollama pull qwen2.5:7b")
                return True, []
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return False, []
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama")
        print("\nTroubleshooting:")
        print("1. Make sure Ollama is running")
        print("2. Start it with: ollama serve")
        print("3. Or restart the Ollama service")
        return False, []
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, []


def test_simple_generation(model_name="qwen2.5:7b"):
    """Test a simple generation"""
    print(f"\n" + "=" * 80)
    print(f"Testing Generation with {model_name}")
    print("=" * 80)
    
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": model_name,
            "prompt": "Say 'Hello' and nothing else.",
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 50
            }
        }
        
        print(f"\nSending request to {model_name}...")
        print("(This may take a moment on first run)")
        
        response = requests.post(url, json=payload, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            output = result.get("response", "")
            print(f"\n✓ Success!")
            print(f"Response: {output}")
            return True
        else:
            print(f"\n❌ Error {response.status_code}")
            print(f"Message: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("\n⚠️  Request timed out")
        print("The model might be loading for the first time")
        print("Try again in a moment")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def test_chat_mode(model_name="qwen2.5:7b"):
    """Test chat mode"""
    print(f"\n" + "=" * 80)
    print(f"Testing Chat Mode with {model_name}")
    print("=" * 80)
    
    try:
        url = "http://localhost:11434/api/chat"
        payload = {
            "model": model_name,
            "messages": [
                {"role": "user", "content": "What is 2+2? Answer with just the number."}
            ],
            "stream": False
        }
        
        print(f"\nSending chat request...")
        
        response = requests.post(url, json=payload, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            message = result.get("message", {})
            content = message.get("content", "")
            print(f"\n✓ Chat mode works!")
            print(f"Response: {content}")
            return True
        else:
            print(f"\n❌ Error {response.status_code}")
            print(f"Message: {response.text}")
            return False
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def main():
    """Run diagnostics"""
    print("\n" + "=" * 80)
    print("OLLAMA LOCAL LLM DIAGNOSTICS")
    print("=" * 80 + "\n")
    
    # Check server
    server_ok, models = check_ollama_server()
    
    if not server_ok:
        print("\n" + "=" * 80)
        print("SETUP REQUIRED")
        print("=" * 80)
        print("\n1. Start Ollama:")
        print("   ollama serve")
        print("\n2. Or restart Ollama from system tray")
        print("\n3. Run this diagnostic again")
        return
    
    if not models:
        print("\n" + "=" * 80)
        print("NO MODELS FOUND")
        print("=" * 80)
        print("\nPull a model:")
        print("   ollama pull qwen2.5:7b")
        print("\nThen run this diagnostic again")
        return
    
    # Test with first available model
    model_name = models[0].get("name", "qwen2.5:7b")
    
    print(f"\n✓ Will test with: {model_name}")
    
    # Test generation
    gen_ok = test_simple_generation(model_name)
    
    if gen_ok:
        # Test chat
        chat_ok = test_chat_mode(model_name)
        
        if chat_ok:
            print("\n" + "=" * 80)
            print("✅ ALL TESTS PASSED!")
            print("=" * 80)
            print("\nYour Ollama setup is working perfectly!")
            print(f"You can use: {model_name}")
            print("\nRun the Qwen example:")
            print("   python examples\\qwen_example.py")
        else:
            print("\n⚠️  Chat mode failed, but generation works")
    else:
        print("\n" + "=" * 80)
        print("TROUBLESHOOTING")
        print("=" * 80)
        print("\nIf the model fails to load:")
        print("1. Restart Ollama: Close and reopen Ollama app")
        print("2. Re-pull the model: ollama pull " + model_name)
        print("3. Try a different model: ollama pull qwen2.5:3b")
        print("4. Check Ollama logs for errors")
    
    print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    main()
