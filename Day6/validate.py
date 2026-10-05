"""Day 6: minimal JSON-schema validation for tool arguments."""
import json

from tools_v2 import SCHEMAS


def validate_args(tool_name: str, raw_args):
    """
    Validate raw tool arguments against the tool's schema.

    Returns:
        (True, parsed_args, "")
        or
        (False, None, error_message)
    """

    # 1. Check whether the tool exists
    if tool_name not in SCHEMAS:
        return False, None, f"Unknown tool: {tool_name}"

    # 2. Parse JSON if arguments arrive as a string
    if isinstance(raw_args, str):
        try:
            args = json.loads(raw_args)
        except json.JSONDecodeError as error:
            return False, None, f"Malformed JSON arguments: {error}"
    elif isinstance(raw_args, dict):
        args = raw_args
    else:
        return False, None, "Arguments must be a JSON object"

    # 3. Arguments must be an object
    if not isinstance(args, dict):
        return False, None, "Arguments must be a JSON object"

    schema = SCHEMAS[tool_name]
    properties = schema.get("properties", {})
    required = schema.get("required", [])

    # 4. Check required arguments
    missing = [name for name in required if name not in args]
    if missing:
        return False, None, f"Missing required argument(s): {', '.join(missing)}"

    # 5. Reject unexpected arguments
    if schema.get("additionalProperties") is False:
        unexpected = [name for name in args if name not in properties]
        if unexpected:
            return False, None, f"Unexpected argument(s): {', '.join(unexpected)}"

    # 6. Check enum values
    for name, value in args.items():
        definition = properties.get(name, {})

        if "enum" in definition and value not in definition["enum"]:
            return (
                False,
                None,
                f"Invalid value for {name}: {value}. "
                f"Allowed values: {definition['enum']}",
            )

        # Basic type checks
        expected_type = definition.get("type")

        if expected_type == "string" and not isinstance(value, str):
            return False, None, f"Argument '{name}' must be a string"

    return True, args, ""