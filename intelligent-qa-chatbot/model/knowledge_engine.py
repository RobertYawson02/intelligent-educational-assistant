import json
import os

# ---------------------------------------------------
# KNOWLEDGE ENGINE
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(BASE_DIR, "data")


# ---------------------------------------------------
# LOAD ALL SUBJECTS
# ---------------------------------------------------

def load_subjects():

    knowledge = []

    for filename in os.listdir(DATA_FOLDER):

        # Skip the Akan dictionary
        if filename == "akan_lexical_knowledge_base.json":
            continue

        if filename.endswith(".json"):

            filepath = os.path.join(DATA_FOLDER, filename)

            try:

                with open(filepath, "r", encoding="utf-8") as file:

                    data = json.load(file)

                    if isinstance(data, list):
                        knowledge.extend(data)

                    elif isinstance(data, dict):
                        knowledge.append(data)

            except Exception as e:

                print(f"Cannot load {filename}: {e}")

    return knowledge


knowledge_base = load_subjects()


# ---------------------------------------------------
# SEARCH KNOWLEDGE
# ---------------------------------------------------

def search_knowledge(question):

    question = question.lower()

    for topic in knowledge_base:

        keywords = topic.get("keywords", [])

        keywords = [k.lower() for k in keywords]

        title = topic.get("topic", "").lower()

        if title in question:

            return topic

        for word in keywords:

            if word in question:
                return topic

    return None


# ---------------------------------------------------
# FORMAT EDUCATIONAL RESPONSE
# ---------------------------------------------------

def format_knowledge(topic):

    response = f"""
📚 Subject: {topic.get('subject','Unknown')}

📖 Topic:
{topic.get('topic','')}

🇬🇧 English Explanation

{topic.get('definition_en','No definition available.')}

🇬🇭 Akan Explanation

{topic.get('definition_twi','No Akan explanation available.')}

⭐ Importance

{topic.get('importance_en','')}

📝 Example

{topic.get('example_en','')}

{topic.get('example_twi','')}

❓ Quiz

{topic.get('quiz_question','')}

✅ Answer

{topic.get('quiz_answer','')}
"""

    return response