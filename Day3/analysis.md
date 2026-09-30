# Day 3 - ReAct Agent Analysis

## 1. Objective

The objective of this lab is to build a simple ReAct agent in Python using a calculator tool and a web-page reader tool.

The agent follows the Reason -> Act -> Observe cycle and uses tools only when required.

---

## 2. Tools Used

### Calculator
The calculator performs arithmetic expressions safely.

Example:

15% of AI202 fee:

18000 * 0.15 = 2700

### Web Page Reader
The web-page reader reads local HTML files or web pages and returns the text content.

Example:

notice.html contains the course fee details.

---

## 3. Normal Test Results

### Test 1 - Scholarship Calculation

Question:

Read notice.html and tell me the total fee for CS101 and AI202 after the merit scholarship.

CS101 = Rs. 12,000
AI202 = Rs. 18,000

Total = Rs. 30,000

10% scholarship = Rs. 3,000

Final fee = Rs. 27,000

Result: Correct

### Test 2 - AI202 Percentage

Question:

Read notice.html. What is 15% of the AI202 fee?

AI202 fee = Rs. 18,000

15% = 0.15 x 18,000

Answer = Rs. 2,700

Result: Correct

### Test 3 - Welcome Message

Question:

Give me a simple welcome message.

The agent answered directly without using any tool.

Result: Correct

---

## 4. Failure 1 - Repeating Tool Calls

Question:

Read fees.html and tell me the fee for CS101.

The file fees.html does not exist.

The unguarded agent repeatedly called the read_webpage tool.

Observed calls:

1. fees.html
2. fees.html
3. fees.html
4. fees.html
5. ./fees.html

Problem:

The agent continued trying the same unsuccessful tool call.

Fix:

Repeat detection was added to stop repeated calls when there is no progress.

---

## 5. Failure 2 - Hallucinated Tool

The agent was instructed to use a send_email tool even though the tool was not registered.

Problem:

The model may try to call a tool that does not exist.

Fix:

The tool registry uses safe lookup with .get(name) so an unknown tool can be handled safely instead of causing a program crash.

---

## 6. Failure 3 - Large Context

A large HTML page named big.html was generated with many student records.

Problem:

Reading a very large page can produce excessive tool output, increase context size and increase computation/cost.

Fix:

The fixed agent limits tool output and total context size.

---

## 7. Guards Added

The fixed agent includes:

- Repeat detection
- Maximum tool steps
- Maximum tool output characters
- Total character budget
- Safe handling of unknown tools

Chosen limits:

max_steps = 6

MAX_TOOL_CHARS = 1500

CHAR_BUDGET = 30000

Repeat threshold = 3

---

## 8. Fixed Agent Results

### Normal page

The fixed agent successfully read notice.html and calculated the total fee as Rs. 27,000.

### Missing page

The fixed agent detected repeated calls to fees.html and stopped instead of continuing indefinitely.

### Large page

The fixed agent detected repeated calls while processing big.html and stopped safely.

---

## 9. Observation

The unguarded ReAct agent can continue making unnecessary tool calls when a tool fails or when a large amount of information is returned.

Adding repeat detection, output limits and context budgets makes the agent safer and prevents unnecessary tool usage.

---

## 10. Conclusion

The ReAct agent was successfully implemented using Python with a calculator and web-page reader.

Three failure situations were studied:

1. Repeating tool-call loop
2. Hallucinated or unknown tool call
3. Large context / runaway tool usage

Guards were added to improve reliability, safety and resource usage.