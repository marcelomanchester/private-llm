# Private LLM Agent

A Python-based private LLM agent built using OpenAI's API.

## Features
- Conversational agent capabilities.
- Task execution: text summarization, code generation, translations.
- Customizable configurations.
- Secure environment for private use.

## Repository Structure
The following structure organizes the project:

```plaintext
.
├── .github/
│   ├── workflows/
│   │   └── ci.yml                # CI pipeline (optional)
├── agent/
│   ├── __init__.py
│   ├── agent.py                  # Core logic for the agent
│   ├── utils.py                  # Utility functions (e.g., input processing)
│   ├── handlers.py               # Handlers for different functionalities
├── config/
│   ├── config.yaml               # Configurations (e.g., tasks, API settings)
│   ├── secrets.env               # Environment variables (use `.gitignore`!)
├── data/
│   ├── logs/
│   │   └── interactions.log      # Log user-agent interactions
│   └── samples/                  # Sample datasets for testing
├── tests/
│   ├── test_agent.py             # Unit tests for agent logic
│   ├── test_utils.py             # Unit tests for utility functions
├── .gitignore                    # Ignored files
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── main.py                       # Main entry point
├── LICENSE                       # License (optional)
└── CONTRIBUTING.md               # Contribution guidelines (optional)
```
## Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation
1. Clone the repository:
  ```bash
   git clone https://github.com/<your-username>/private-llm-agent.git
   cd private-llm-agent
  ```

2. Install dependencies:
  ```bash
    pip install -r requirements.txt
  ```

3. Set Up your environment:
  * Create a config/secrets.env file and add your OpenAI API key
  ``OPENAI_API_KEY=your_api_key``

### Usage
1. Run the main program:
  ```bash
    python main.py
  ```


