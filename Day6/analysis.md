\# Day 6 Analysis



\## 1. Robust Function Calling



The Day 6 agent validates tool calls before executing them.



It checks:

\- Unknown tools

\- Missing required arguments

\- Unexpected arguments

\- Invalid enum values

\- Wrong argument types



Invalid tool calls are rejected with an error message instead of causing the program to crash.



\## 2. Fault Injection Testing



Eight fault cases were tested:



1\. Unknown tool

2\. Missing required argument

3\. Unexpected argument

4\. Invalid enum value

5\. Wrong argument type

6\. Different tool-name capitalization

7\. JSON array instead of an object

8\. Valid tool call



The seven invalid cases were rejected correctly, and the valid call was accepted.



\## 3. Structured Outputs



Three response formats were tested:



1\. Free text

2\. JSON mode

3\. JSON schema mode



JSON mode and JSON schema mode provide a predictable JSON structure that can be parsed by the program.



The schema mode also ensures that the response follows the required fields:

\- course\_code

\- wants\_scholarship

\- needs\_tool



\## 4. Conclusion



The Day 6 implementation makes the agent more reliable by validating tool arguments, handling invalid calls safely, and using structured outputs that can be parsed by the program.

