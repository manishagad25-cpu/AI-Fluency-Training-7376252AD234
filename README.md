# AI Fluency Training - Day 1

## Agentic AI: Foundations and Open-Source Practice

This repository contains my Day 1 practical work for the AI Fluency Training.

The Day 1 lab focuses on understanding:
- Chatbot
- Rule-based workflow
- AI agent
- Tool usage
- Agent behavior on an unseen question

## Programs

### 1. Chatbot
A simple chatbot that takes a question from the user and generates a response using an LLM.

### 2. Rule-Based Workflow
A fixed workflow for answering predefined course-fee questions.

Course fees:

- CS101 - ₹12,000
- AI202 - ₹18,000
- DS303 - ₹15,000

### 3. AI Agent
An AI agent that can use tools when required.

Tools used:

- `get_course_fee` - retrieves the fee of a course
- `calculator` - performs arithmetic calculations

### 4. Challenge
An unseen question was used to compare the rule-based workflow and the AI agent.

## Technologies Used

- Python
- VS Code
- Groq API
- GPT-OSS-20B
- OpenAI Python SDK
- python-dotenv

## Project Structure

```text
Day1/
├── agent.py
├── challenge.py
├── chatbot.py
├── check_setup.py
├── config.py
├── requirements.txt
├── tools.py
├── workflow.py
├── .gitignore
└── outputs/
    ├── agent.png
    ├── challenge.png
    ├── chatbot.png
    ├── check_setup.png
    └── workflow.png

    Observation

The rule-based workflow works only for the fixed questions defined in the program.

The AI agent can use tools dynamically. In the challenge, it retrieved the course fees and calculated the possible combinations, but it reached the maximum step limit before giving a final response.

Output Screenshots

The Day1/outputs folder contains screenshots of the actual program executions.