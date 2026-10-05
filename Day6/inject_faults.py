"""Day 6: test the validator with intentionally faulty tool calls."""

from validate import validate_args


TESTS = [
    (
        "Unknown tool",
        "unknown_tool",
        {"course_code": "AI202"},
    ),
    (
        "Missing required argument",
        "get_course_fee",
        {"semester": "odd"},
    ),
    (
        "Unexpected argument",
        "get_course_fee",
        {
            "course_code": "AI202",
            "wrong_argument": "test",
        },
    ),
    (
        "Invalid enum value",
        "get_course_fee",
        {
            "course_code": "AI202",
            "semester": "summer",
        },
    ),
    (
        "Wrong argument type",
        "get_course_fee",
        {
            "course_code": 202,
        },
    ),
    (
        "Different capitalization",
        "GET_COURSE_FEE",
        {"course_code": "AI202"},
    ),
    (
        "Arguments are JSON array",
        "get_course_fee",
        ["AI202"],
    ),
    (
        "Valid call",
        "get_course_fee",
        {
            "course_code": "AI202",
        },
    ),
]


if __name__ == "__main__":
    print("=" * 70)
    print("DAY 6 — FAULT INJECTION / VALIDATION TEST")
    print("=" * 70)

    for title, tool_name, arguments in TESTS:
        valid, parsed, error = validate_args(
            tool_name,
            arguments,
        )

        print(f"\n[{title}]")
        print(f"Tool: {tool_name}")
        print(f"Arguments: {arguments}")
        print(f"Valid: {valid}")

        if valid:
            print(f"Parsed: {parsed}")
        else:
            print(f"Rejected: {error}")