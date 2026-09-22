# AI Fluency Training – Day 1

## 1. Observations

### Comparison of the Three Systems

| Criterion | Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Q1 correct? | General chatbot responded, but it has no access to the private fee data | Yes – ₹18,000 | Yes – ₹18,000 |
| Q2 correct? | It does not have the course-fee data available in its prompt | Yes – ₹27,000 | Yes – ₹27,000 |
| Q3 correct? | It does not have the course-fee data available in its prompt | Yes – ₹3,000 more | Yes – ₹3,000 more |
| Q4 handled well? | Yes – it can generate a welcome message | No – only fixed fee rules were included | Yes – it answered directly without using a tool |
| Challenge question handled? | No fee data/rules available | No – returned the fixed-rule message | Partly – it found the correct combinations but stopped at the maximum step limit |
| Same output on repeat run? | Response wording can change | Yes, because the rules are fixed | Tool steps/writing can change between runs |
| Approximate response time | A few seconds | Almost instant | A few seconds per question |
| LLM calls per question | 1 | 0 | Depends on the number of tool/reasoning steps |
| One strength | Simple and natural conversation | Reliable for predefined questions | Can choose and use tools for multi-step tasks |
| One weakness | Can lack private data and may give an uncertain answer confidently | Rigid and cannot handle new questions automatically | Can use unnecessary steps or stop at the step limit |
| Suitable use case | General student questions | Fixed college fee/office queries | Questions involving lookup and calculation |

### Actual Results from My Run

#### Rule-Based Workflow

For the fixed questions, the workflow gave:

- AI202 fee = ₹18,000
- CS101 + AI202 after 10% scholarship = ₹27,000
- DS303 is ₹3,000 more expensive than CS101
- For the welcome message question, it returned: `I can answer only the fixed course questions.`

#### AI Agent

The agent used the tools correctly for the fixed questions.

For Question 2 it used:

| Step | Tool | Arguments | Result |
|---|---|---|---|
| 1 | `get_course_fee` | `course_code = AI202` / course lookup as required | Course fee lookup |
| 2 | `get_course_fee` | `course_code = CS101` | ₹12,000 |
| 3 | `calculator` | `(12000+18000)*0.9` | ₹27,000 |

In the actual Question 2 run, the printed steps were:

```text
step 1: get_course_fee({'course_code': 'CS101'}) -> 12000
step 2: get_course_fee({'course_code': 'AI202'}) -> 18000
step 3: calculator({'expression': '(12000+18000)*0.9'}) -> 27000.0
```

For Question 3, it looked up both fees and calculated the difference:

```text
step 1: get_course_fee({'course_code': 'DS303'}) -> 15000
step 2: get_course_fee({'course_code': 'CS101'}) -> 12000
step 3: calculator({'expression': '15000-12000'}) -> 3000
```

For Question 4, the agent answered directly and did not call a tool.

#### Challenge Question

Question:

> I can pay Rs. 30,000. Which two courses can I take together within this budget?

My actual output was:

```text
Workflow : I can answer only the fixed course questions.

step 1: get_course_fee({'course_code': 'CS101'}) -> 12000
step 2: get_course_fee({'course_code': 'AI202'}) -> 18000
step 3: get_course_fee({'course_code': 'DS303'}) -> 15000
step 4: calculator({'expression': '12000+18000'}) -> 30000
step 5: calculator({'expression': '12000+15000'}) -> 27000
step 6: calculator({'expression': '18000+15000'}) -> 33000

Agent : Stopped: maximum steps reached without a final answer.
```

So the agent found:

- CS101 + AI202 = ₹30,000
- CS101 + DS303 = ₹27,000
- AI202 + DS303 = ₹33,000

It did the calculations, but it did not finish with a final answer because the `max_steps` limit was reached.

---

## 2. Discussion Questions

### 1. The chatbot gave a confident but wrong fee. Why is that more dangerous than replying "I don't know"?

A confident wrong answer can look correct to the user. In a fee-related case, the user may trust it and make a wrong financial decision. Saying "I don't know" makes the lack of information clear.

### 2. The workflow was always correct for questions 1 and 2. Why might a finance office still prefer it over the agent?

A workflow follows fixed rules, so the output is predictable for the questions covered by those rules. A finance office may prefer this for fixed fee calculations because the logic is directly controlled by the programmer.

### 3. The agent's steps can change between runs. What problems would that cause in a real product?

Different steps can make the system harder to test and debug. It can also increase response time and sometimes lead to unnecessary tool calls or incomplete answers.

### 4. Design a system that uses a workflow for common questions and an agent for the rest. Where would you draw the line?

I would use the workflow first for common and clearly defined questions such as course fees, application status, and fixed rules. Questions that do not match those rules or need multiple steps can be sent to the agent.

### 5. Which parts of `agent.py` are the LLM, the tools, and the loop?

- **LLM:** `client.chat.completions.create(...)`
- **Tools:** `get_course_fee` and `calculator`
- **Loop:** `for step in range(1, max_steps + 1):`

The LLM decides the next action, Python executes the selected tool, and the result is sent back to the LLM until it gives a final answer or reaches the step limit.

## 3. Conclusion

This experiment showed the difference between a plain chatbot, a fixed rule-based workflow, and a tool-using AI agent.

The chatbot is useful for normal conversation but does not automatically know the private course-fee data. The workflow gives fixed and predictable answers for the rules that were programmed. The agent can use tools and handle multi-step questions, but the challenge run also showed that an agent may not always finish successfully within its step limit.
