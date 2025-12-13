"""
Quick Start Script for Multi-Agent Framework
Run this script to verify your installation and get started
"""
import sys
import os
from pathlib import Path


def print_banner():
    """Print welcome banner"""
    print("\n" + "=" * 80)
    print(" " * 20 + "MULTI-AGENT AI RESEARCH FRAMEWORK")
    print("=" * 80 + "\n")


def check_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} detected")
        print("   Required: Python 3.8 or higher")
        return False


def check_dependencies():
    """Check if key dependencies are installed"""
    print("\nChecking dependencies...")
    
    required_packages = [
        'crewai', 'langchain', 'openai', 'anthropic', 
        'pydantic', 'dotenv', 'pandas', 'numpy'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✓ {package}")
        except ImportError:
            print(f"❌ {package} - not found")
            missing.append(package)
    
    if missing:
        print("\n⚠️  Some packages are missing. Install them with:")
        print("   pip install -r requirements.txt")
        return False
    
    return True


def check_env_file():
    """Check if .env file exists"""
    print("\nChecking environment configuration...")
    
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if env_file.exists():
        print("✓ .env file found")
        
        # Check if API keys are configured
        with open(env_file, 'r') as f:
            content = f.read()
            
        has_openai = "OPENAI_API_KEY" in content and "your_" not in content
        has_anthropic = "ANTHROPIC_API_KEY" in content and "your_" not in content
        
        if has_openai or has_anthropic:
            print("✓ API keys appear to be configured")
            return True
        else:
            print("⚠️  .env file exists but API keys may not be configured")
            print("   Edit .env and add your API keys")
            return False
    else:
        print("⚠️  .env file not found")
        if env_example.exists():
            print("   Copy .env.example to .env and add your API keys:")
            print("   copy .env.example .env")
        return False


def show_examples():
    """Show available examples"""
    print("\n" + "-" * 80)
    print("Available Examples:")
    print("-" * 80)
    
    examples = [
        ("basic_example.py", "Basic multi-agent interaction (no API key needed)"),
        ("advanced_example.py", "Advanced orchestration workflow (no API key needed)"),
        ("crewai_example.py", "CrewAI framework integration (requires API key)"),
        ("autogen_example.py", "AutoGen framework integration (requires API key)")
    ]
    
    for filename, description in examples:
        filepath = Path("examples") / filename
        if filepath.exists():
            print(f"✓ {filename:25} - {description}")
        else:
            print(f"  {filename:25} - {description}")
    
    print()


def show_next_steps(has_deps, has_env):
    """Show next steps based on setup status"""
    print("-" * 80)
    print("Next Steps:")
    print("-" * 80)
    
    if not has_deps:
        print("1. Install dependencies:")
        print('   pip install -r requirements.txt')
        print()
    
    if not has_env:
        print("2. Configure environment:")
        print('   copy .env.example .env')
        print('   # Then edit .env and add your API keys')
        print()
    
    print("3. Run examples:")
    print('   python examples/basic_example.py         # Start here (no API needed)')
    print('   python examples/advanced_example.py      # More complex (no API needed)')
    print('   python examples/crewai_example.py        # Requires API key')
    print('   python examples/autogen_example.py       # Requires API key')
    print()
    
    print("4. Explore the framework:")
    print('   - Check agents/ folder for agent implementations')
    print('   - Check tools/ folder for available tools')
    print('   - Read README.md for detailed documentation')
    print()
    
    print("5. Create your own agents:")
    print('   - Extend BaseAgent class')
    print('   - Add custom tools')
    print('   - Build your workflows')
    print()


def main():
    """Main setup check"""
    print_banner()
    
    # Run checks
    python_ok = check_python_version()
    deps_ok = check_dependencies()
    env_ok = check_env_file()
    
    # Show examples
    show_examples()
    
    # Summary
    print("=" * 80)
    print("Setup Summary:")
    print("=" * 80)
    print(f"Python Version:  {'✓ OK' if python_ok else '❌ Update Required'}")
    print(f"Dependencies:    {'✓ OK' if deps_ok else '❌ Install Required'}")
    print(f"Configuration:   {'✓ OK' if env_ok else '⚠️  Setup Required'}")
    print()
    
    if python_ok and deps_ok:
        print("🎉 Your environment is ready!")
        if not env_ok:
            print("⚠️  Add API keys to .env to use advanced examples")
    else:
        print("⚠️  Some setup steps are still needed")
    
    print()
    
    # Show next steps
    show_next_steps(deps_ok, env_ok)
    
    print("=" * 80)
    print("For more information, see README.md")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
