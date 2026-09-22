from config import COURSE_FEES, QUESTIONS, banner


def workflow(question):
    q = question.lower()

    if "fee for ai202" in q:
        return f"AI202 fee is ₹{COURSE_FEES['AI202']}."

    if "total fee" in q and "scholarship" in q:
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        discounted = total * 0.90
        return f"Total after 10% scholarship is ₹{discounted:.0f}."

    if "ds303" in q and "cs101" in q:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]
        return f"DS303 is ₹{difference} more expensive than CS101."

    return "I can answer only the fixed course questions."


if __name__ == "__main__":
    banner("RULE-BASED WORKFLOW")

    for i, question in enumerate(QUESTIONS, start=1):
        print(f"Q{i}: {question}")
        print("A :", workflow(question))
        print()