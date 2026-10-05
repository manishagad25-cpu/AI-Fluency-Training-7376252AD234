"""Day 6: robust function-calling agent."""

import json
import os
import time

from openai import OpenAI

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Day1"))

from config import MODEL, client
from tools_v2 import TOOL_FUNCTIONS, TOOLS
from validate import validate_args


MAX_TOOL_CALLS = 6
MAX_RETRIES = 2


def execute_tool(tool_name, raw_arguments):
    """Validate and execute one tool call."""
    valid, arguments, error = validate_args(tool_name, raw_arguments)

    if not valid:
        return {
            "ok": False,
            "error": error,
        }

    try:
        result = TOOL_FUNCTIONS[tool_name](**arguments)

        return {
            "ok": True,
            "result": result,
        }

    except Exception as error:
        return {
            "ok": False,
            "error": f"Tool execution failed: {error}",
        }


def run_agent(prompt):
    """Run the model and safely handle tool calls."""

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    tool_call_count = 0
    retry_count = 0

    while tool_call_count < MAX_TOOL_CALLS:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0,
        )

        choice = response.choices[0]

        # Retry if the model response was cut off.
        if choice.finish_reason == "length":
            if retry_count >= MAX_RETRIES:
                return "Stopped: model repeatedly exceeded the output limit."

            retry_count += 1

            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Your previous response was cut off. "
                        "Please provide a shorter response."
                    ),
                }
            )

            continue

        message = choice.message

        # Normal text response.
        if not message.tool_calls:
            return message.content or ""

        # Add the assistant tool-call message to the conversation.
        messages.append(message)

        for tool_call in message.tool_calls:

            tool_call_count += 1

            if tool_call_count > MAX_TOOL_CALLS:
                return "Stopped: too many tool calls."

            tool_name = tool_call.function.name
            raw_arguments = tool_call.function.arguments

            result = execute_tool(
                tool_name,
                raw_arguments,
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                }
            )

    return "Stopped: maximum tool-call limit reached."


if __name__ == "__main__":

    print("=" * 60)
    print("DAY 6 — ROBUST FUNCTION CALLING AGENT")
    print("=" * 60)

    prompt = input("\nEnter your question: ")

    start = time.time()

    answer = run_agent(prompt)

    elapsed = time.time() - start

    print("\nANSWER:")
    print(answer)

    print(f"\nTime: {elapsed:.2f} seconds")