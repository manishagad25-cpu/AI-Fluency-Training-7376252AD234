# Day 2 - Analysis

## 1. Objective

In Day 2, I learned how a ReAct agent works with Thought, Action and Observation. I also compared answers from an LLM when I used a direct prompt and when I asked it to solve step by step. Finally, I used self-consistency by running the same question five times and checking the answers.

## 2. ReAct Trace Observation

The question used for the ReAct test was:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?

The correct answer is that CS101 + AI202 with 10% scholarship costs Rs. 27,000, while all three courses with 25% scholarship costs Rs. 33,750. The difference is Rs. 6,750.

In my actual agent run, the agent made 3 fee lookups and 3 calculator calls. The printed trace had one tool call in each step from step 1 to step 6, so no two tool calls were printed under the same step number. Therefore, no parallel tool call happened in this run.

The actual trace was:

- Step 1: get_course_fee(CS101) -> 12000
- Step 2: get_course_fee(AI202) -> 18000
- Step 3: get_course_fee(DS303) -> 15000
- Step 4: calculator(30000 * 0.9) -> 27000
- Step 5: calculator(45000 * 0.75) -> 33750
- Step 6: calculator(33750 - 27000) -> 6750

The agent then gave the final answer correctly.

For the agent code, each step makes an LLM call. So this run needed 6 LLM calls to make the tool calls and one more LLM call to give the final answer, which is about 7 LLM calls in total.

## 3. Chain-of-Thought Comparison

I tested three reasoning questions with and without Chain-of-Thought. The questions were about course instalments, lab sittings and height ordering.

| Question | Without CoT correct? | With CoT correct? | Which reply was longer? |
|---|---|---|---|
| Q1 - Instalments | Yes | Yes | With CoT |
| Q2 - Lab sittings | Yes | Yes | With CoT |
| Q3 - Tallest and shortest | Yes | Yes | With CoT |

### Q1

The direct answer was Rs. 9,562.50 per instalment. The CoT answer showed the total, scholarship, payable amount and division into four instalments. Both were correct.

### Q2

The direct answer was 90 student sittings. The CoT answer showed morning sittings, afternoon sittings and the final total. Both were correct.

### Q3

The direct answer was Ravi as the tallest and Priya as the shortest. The CoT answer showed the comparison chain before giving the final answer. Both were correct.

In all three questions, the CoT reply was longer because it included the intermediate steps. In this run, CoT did not change the final answer because the direct answers were already correct.

## 4. Self-Consistency Observation

For self-consistency, I used the first instalment question five times with temperature 0.8.

The five outputs were:

1. 9,562.5 rupees per instalment
2. 9,562.5 rupees
3. Rs. 9,562.50
4. Rs. 9,562.50 per instalment
5. 9562.5 rupees per instalment

All five answers have the same numerical value. The difference was only in formatting and wording.

One thing I noticed is that the program compares the complete answer string. Because the wording was different in all five runs, the program printed:

> Majority answer (1 of 5 runs)

So the printed majority was 1 of 5 even though all five answers were numerically the same. This shows that voting only on the exact text can be affected by formatting differences.

The correct numerical answer is Rs. 9,562.50, so the answers were correct.

The lab also asks for a comparison with temperature = 0. That extra run should be done separately because it was not part of the output above. With temperature 0, the purpose is to see that the five outputs become much more similar, so voting gives less extra benefit.

## 5. Discussion Questions

### 1. Does a different order of steps make one ReAct trace wrong?

Not necessarily. The order can be different as long as the required information is collected correctly and the final calculation is correct. For example, course fees can be looked up in a different order and still give the same final result.

### 2. Why did the model not automatically reason step by step?

The normal model prompt does not force it to show all intermediate steps. When I added the Chain-of-Thought instruction, I gave it a clear format for showing the steps, so it was more explicit in the solution.

### 3. What is missing when CoT cannot answer the fee question, and which pattern supplies it?

CoT only changes how the model reasons about the information it already has. It does not give the model the real course-fee data. The missing part is tool access. ReAct supplies this by connecting the LLM with tools that can retrieve the fee and do the calculation.

### 4. Why is temperature different for self-consistency and Day 1 tool calling?

For Day 1 tool calling, temperature 0 was used because consistent tool selection and factual answers are useful. For self-consistency, temperature 0.8 is used deliberately so that different runs can explore different reasoning paths. Then the answers can be compared.

### 5. How would Plan-and-Execute handle the Section 6 question?

Plan-and-Execute would first make a plan for the whole problem and then execute the planned steps. For this question, the plan could be to get the three fees, calculate the two discounted totals, and compare them. It may need fewer repeated planning decisions because the overall plan is made first, but the exact number of LLM calls depends on the implementation.

## 6. What I Learned

From this lab, I understood that Chain-of-Thought can make the model show more detailed reasoning, but it does not give access to missing facts. ReAct adds tools, so the agent can get real data and perform actions.

I also understood why self-consistency uses a non-zero temperature. It gives multiple reasoning attempts instead of repeating almost the same response every time.

The main difference I learned is:

```text
Chain-of-Thought
= step-by-step reasoning prompt

ReAct
= reasoning + actions/tools + observations

Self-Consistency
= multiple reasoning runs + majority checking
```

## 7. Result

The Day 2 experiments helped me understand how different prompting and agent patterns affect problem solving. In my run, the CoT answers were longer but all three final answers were already correct. The self-consistency runs gave the same numerical answer with different wording. The ReAct agent correctly used the course-fee and calculator tools and reached the final answer of Rs. 6,750.
