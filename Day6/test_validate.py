from validate import validate_args

print(validate_args(
    "get_course_fee",
    {"course_code": "AI202"}
))

print(validate_args(
    "get_course_fee",
    {"semester": "odd"}
))

print(validate_args(
    "get_course_fee",
    {"course_code": "AI202", "bad": "x"}
))