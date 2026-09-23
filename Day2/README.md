# Day 2 - Agentic AI Lab

This folder contains my Day 2 lab work from the Agentic AI training.

## What I learned

Day 2 mainly focused on:

- ReAct: Thought, Action and Observation
- Chain-of-Thought (CoT) prompting
- Self-Consistency

The lab helped me understand when step-by-step reasoning is useful and when an AI agent needs tools to complete a task. :contentReference[oaicite:1]{index=1}

## Programs

### 1. react_trace.py

This program runs the Day 1 agent on a multi-step course-fee question and shows the agent's tool actions and observations.

The question compares:

- CS101 + AI202 with a 10% scholarship
- All three courses with a 25% scholarship

In my run:

```text
CS101 + AI202 with 10% scholarship = Rs. 27,000
All three courses with 25% scholarship = Rs. 33,750
Difference = Rs. 6,750
2. cot_compare.py

This program compares the same reasoning questions in two ways:

Without CoT - only the final answer is requested.
With CoT - the model is asked to solve step by step.

The three questions were about:

Course fees, scholarship and instalments
Student sittings in a computer lab
Finding the tallest and shortest person

In my run, both the Without-CoT and With-CoT answers were correct for all three questions.

The With-CoT replies were longer because they included the reasoning steps.
3. self_consistency.py

This program runs the same CoT question five times with:

RUNS = 5
TEMPERATURE = 0.8

The five answers had different wording, but all represented the same numerical answer:

Rs. 9,562.50 per instalment

The script then compares the extracted final answers and prints the most common result.

In my run, the printed majority result was:

Majority answer (1 of 5)

because the answers had different formatting even though the numerical result was the same.

The lab uses a non-zero temperature so that the runs can produce different reasoning paths.
ReAct

The ReAct process can be understood as:

Thought
   ↓
Action
   ↓
Observation
   ↓
Next Action
   ↓
Final Answer

An action is a tool call and the observation is the result returned by the tool. The Day 2 lab asks us to compare our expected trace with the real agent trace
Chain-of-Thought

Chain-of-Thought means asking the model to solve a problem step by step instead of directly giving only the final answer.

In my experiment, the With-CoT responses included the calculation or reasoning steps, while the Without-CoT responses were shorter.

Self-Consistency

Self-Consistency means generating multiple reasoning answers for the same question and comparing the final answers.

In this lab:

Runs = 5
Temperature = 0.8

The purpose was to allow some variation between runs and then compare the results.
Output Screenshots

The Output folder contains the screenshots of the Day 2 programs:

Output
├── cot_compare1.png
├── cot_compare2.png
├── react_trace.png
└── self_consistency.png
Technologies Used
Python
Groq
OpenAI-compatible API
python-dotenv

The same LLM option used in Day 1 was reused for Day 2, as required by the lab.