import re

# -------------------------------------
# INTENT PATTERNS
# -------------------------------------

INTENTS = {

    "translation": [
        "translate",
        "translation",
        "in twi",
        "in akan",
        "translate to twi",
        "translate into twi",
        "translate into akan"
    ],

    "definition": [
        "what is",
        "define",
        "definition of",
        "meaning of"
    ],

    "explanation": [
        "explain",
        "describe",
        "tell me about",
        "how does"
    ],

    "quiz": [
        "quiz",
        "test me",
        "ask me",
        "question about"
    ],

    "example": [
        "example",
        "examples",
        "sample sentence"
    ],

    "comparison": [
        "difference",
        "compare",
        "versus",
        "vs"
    ],

    "greeting": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon"
    ]
}


# -------------------------------------
# DETECT USER INTENT
# -------------------------------------

def detect_intent(question):

    q = question.lower().strip()

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            if pattern in q:
                return intent

    return "unknown"

def extract_topic(question):

    q = question.lower()

    fillers = [
        "what is",
        "define",
        "meaning of",
        "translate",
        "translate to twi",
        "translate into twi",
        "tell me about",
        "explain",
        "describe",
        "difference between",
        "compare"
    ]

    for f in fillers:
        q = q.replace(f, "")

    return q.strip()

if __name__ == "__main__":

    while True:

        q = input("> ")

        print("Intent :", detect_intent(q))
        print("Topic  :", extract_topic(q))