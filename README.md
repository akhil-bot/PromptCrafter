# 🚀 PromptCrafter: AI-Powered Multi-Agent Prompt Engineering 🔥  

<div align="center">

![Prompt Engineer Assistant](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![OpenAI](https://img.shields.io/badge/OpenAI-Supported-brightgreen)](https://openai.com/)

</div>



**PromptCrafter** is an advanced **multi-agent tool** designed to generate high-quality prompts for any given task. Whether you're working with LLMs, automating workflows, or optimizing AI interactions, this tool ensures you get the perfect prompt—**every time!**  

### ⚙️ How It Works  
PromptCrafter operates with **two intelligent agents** working together:  
1️⃣ **Prompt Writer** – Crafts an initial prompt tailored to the given task.  
2️⃣ **Prompt Reviewer** – Analyzes and refines the prompt for clarity, completeness, and effectiveness.  

Together, they create optimized prompts that **maximize accuracy and efficiency** in AI-driven applications.  


Get started today and take your **prompt engineering** to the next level! 🚀

### Key Features
- 🎯 Smart prompt generation based on your task description
- 🔄 Automated prompt review and optimization
- 🎨 Intuitive web interface built with Streamlit
- 🌡️ Temperature control for creativity adjustment
- 📋 Easy copy-paste functionality
- 🔒 Reliable error handling and user feedback

## 🚀 Installation Instructions

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/akhil-bot/PromptCrafter.git
cd PromptCrafter
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```


## 💡 Usage Examples

### Starting the Application
```bash
streamlit run main.py
```

### Using the Interface

1. **Configure Model Settings**
   - Select any model provider(for now we support OpenAI)
   - Enter your API key
   - Choose your preferred model (e.g., GPT-3.5-turbo, GPT-4o)
   - Adjust the temperature slider for creativity control

2. **Generate a Prompt**
   ```plaintext
   Task: Create a prompt that helps generate creative story ideas
   
   Result: A well-structured prompt optimized for story generation
   ```

3. **Review and Copy**
   - Review the generated prompt
   - Use the copy button to copy the prompt to your clipboard
   - Use the prompt with your favorite AI model

## 🛠️ Project Structure
```
prompt-engineer/
├── agents/
│   └── Agents.py         # Agent implementations
├── graphs/
│   └── graph.py          # Workflow graph definition
├── models/
│   └── openai_models.py  # Model integrations
├── prompts/
│   └── prompts.py        # Prompt templates
├── states/
│   └── state.py          # State management
├── main.py               # Main application
└── README.md
```

## 🤝 Contribution Guidelines

We welcome contributions! Here's how you can help:

### Reporting Issues
- Use the GitHub issue tracker
- Include detailed descriptions and steps to reproduce
- Add relevant tags and labels

### Making Changes
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Include docstrings for new functions
- Add type hints where applicable
- Write unit tests for new features

## 🔮 Future Work

### Advanced Prompting Styles
- **Chain-of-Thought Integration**: Implement specialized prompting patterns for complex reasoning tasks
- **Zero/Few-Shot Templates**: Add pre-built templates optimized for different learning approaches
- **Task-Specific Patterns**: 
  - Code Generation prompts
  - Story Writing frameworks
  - Mathematical problem-solving structures
  - Data Analysis templates
  - Creative writing patterns
  - And many more...

### LLM-Specific Optimizations
- **Model-Aware Prompting**: Customize prompts based on specific LLM architectures
  - GPT-4 optimized patterns
  - Claude-specific formatting
  - Gemini-enhanced templates
  - Llama/Mistral adaptations
- **Context Window Optimization**: Smart prompt compression for different model context limits

### Enhanced Features
- **Prompt Library**: Build a collection of proven prompt patterns for common use cases
- **Performance Analytics**: Track and analyze prompt effectiveness across different models
- **Human-in-the-Loop**: Allow users to review and refine prompts
- **Interactive Prompt Builder**: Visual interface for constructing complex prompts
- **A/B Testing**: Compare different prompt versions for optimal results
- **Multi-Language Support**: Prompt templates optimized for different languages

### Community Integration
- **Template Sharing**: Platform for users to share and rate prompt templates
- **Collaborative Editing**: Real-time collaboration on prompt engineering
- **Version Control**: Track prompt evolution and improvements
- **Best Practices Database**: Crowdsourced knowledge base for prompt engineering

## 📫 Contact

For any inquiries or support, please contact Akhil Maddala at [akhil.maddala@gmail.com](mailto:akhil.maddala@gmail.com).

You can also find more interesting projects on [GitHub](https://github.com/akhil-bot/).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- The open-source community for their invaluable contributions

---

<div align="center">
Made with ❤️ by a passionate AI Engineer
</div> 