import json
import os
import re


# ---------------------------------------
# LOAD EDUCATIONAL KNOWLEDGE BASE
# ---------------------------------------

def load_knowledge():

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    file_path = os.path.join(
        base_dir,
        "data",
        "educational_knowledge.json"
    )


    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



knowledge_base = load_knowledge()



# ---------------------------------------
# TEXT CLEANER
# ---------------------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    return text



# ---------------------------------------
# KEYWORD MATCHING ENGINE
# ---------------------------------------

def calculate_score(question, item):


    question = clean_text(question)


    score = 0


    keywords = item.get(
        "keywords",
        []
    )


    topic = item.get(
        "topic",
        ""
    )


    # keyword matching

    for keyword in keywords:

        keyword = clean_text(keyword)


        if keyword in question:

            score += 3



    # topic matching

    if clean_text(topic) in question:

        score += 5



    return score




# ---------------------------------------
# KNOWLEDGE SEARCH ENGINE
# ---------------------------------------

def search_knowledge(question):


    best_match = None

    highest_score = 0



    for item in knowledge_base:


        score = calculate_score(
            question,
            item
        )


        if score > highest_score:

            highest_score = score

            best_match = item



    if highest_score > 0:

        return best_match



    return None




# ---------------------------------------
# FORMAT RESPONSE
# ---------------------------------------

def format_knowledge(result):


    return f"""

📚 Educational Knowledge Assistant


Topic:
{result.get('topic','Unknown')}


Definition:
{result.get('definition','No definition available')}


Explanation:
{result.get('explanation','No explanation available')}


Examples:
{', '.join(result.get('examples',[]))}


Category:
{result.get('category','General')}

"""