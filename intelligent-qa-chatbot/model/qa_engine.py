from model.intent_engine import detect_intent, extract_topic

from model.akan_engine import (
    search_akan,
    format_akan_response
)

from model.knowledge_engine import (
    search_knowledge,
    format_knowledge
)

from model.response_engine import create_response

from duckduckgo_search import DDGS



# ---------------------------------------
# LANGUAGE DETECTION
# ---------------------------------------

def detect_language(question):

    q = question.lower()

    akan_words = [
        "nsuo",
        "ɔdɔ",
        "meda ase",
        "maakye",
        "akwaaba",
        "twi",
        "akan"
    ]

    for word in akan_words:

        if word in q:
            return "akan"

    return "english"



# ---------------------------------------
# WEB SEARCH ENGINE
# ---------------------------------------

def web_search(question):

    try:

        print("🌍 Searching Web:", question)


        with DDGS() as ddgs:

            results = ddgs.text(
                question,
                max_results=3
            )


            for result in results:

                body = result.get("body")


                if body and len(body) > 100:

                    return body


    except Exception as e:

        print(
            "Web Error:",
            e
        )


    return None



# ---------------------------------------
# COMBINE ANSWERS
# ---------------------------------------

def combine_answers(
        akan_answer=None,
        knowledge_answer=None,
        web_answer=None
):

    response = ""


    if akan_answer:

        response += (
            "\n🇬🇭 Akan Language Information\n"
            + akan_answer
            + "\n"
        )


    if knowledge_answer:

        response += (
            "\n📚 Educational Explanation\n"
            + knowledge_answer
            + "\n"
        )


    if web_answer:

        response += (
            "\n🌍 Additional Information\n"
            + web_answer
        )


    return response



# ---------------------------------------
# MAIN INTELLIGENT ROUTER
# ---------------------------------------

def get_answer(question):


    print("\n====================")
    print("USER:", question)


    language = detect_language(question)


    intent = detect_intent(question)


    topic = extract_topic(question)



    print("Language:", language)
    print("Intent:", intent)
    print("Topic:", topic)



    akan_answer = None
    knowledge_answer = None
    web_answer = None



    # -----------------------------------
    # 1. AKAN ENGINE
    # -----------------------------------

    akan_result, mode = search_akan(topic)


    if akan_result:


        akan_answer = format_akan_response(
            akan_result
        )



    # -----------------------------------
    # 2. KNOWLEDGE ENGINE
    # -----------------------------------

    knowledge = search_knowledge(topic)


    if knowledge:


        knowledge_answer = format_knowledge(
            knowledge
        )



    # -----------------------------------
    # 3. WEB ENGINE
    # -----------------------------------

    if not knowledge_answer:


        web_answer = web_search(question)



    # -----------------------------------
    # FINAL RESPONSE
    # -----------------------------------

    final_answer = combine_answers(
        akan_answer,
        knowledge_answer,
        web_answer
    )



    if final_answer.strip():


        return create_response(
            final_answer,
            "🧠 Multi Knowledge Engine",
            intent,
            language
        ), "🧠 Intelligent Router"



    return create_response(
        "Sorry, I could not find enough information.",
        "⚠️ System",
        intent,
        language
    ), "⚠️ No Answer"