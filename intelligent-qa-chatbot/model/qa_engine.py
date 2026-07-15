from model.intent_engine import detect_intent, extract_topic
from model.akan_engine import search_akan, format_akan_response
from model.knowledge_engine import search_knowledge, format_knowledge
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

        print("🌍 Searching web:", question)

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

        print("Web Error:", e)


    return None



# ---------------------------------------
# MAIN INTELLIGENT ROUTER
# ---------------------------------------

def get_answer(question):


    print("\n====================")
    print("USER:", question)


    # 1. Detect language
    language = detect_language(question)

    print(
        "Language:",
        language
    )


    # 2. Detect intent
    intent = detect_intent(question)

    print(
        "Intent:",
        intent
    )


    # 3. Extract topic
    topic = extract_topic(question)

    print(
        "Topic:",
        topic
    )



    # -----------------------------------
    # A. AKAN LANGUAGE REQUEST
    # -----------------------------------

    if language == "akan":


        akan_result, mode = search_akan(topic)


        if akan_result:


            answer = format_akan_response(
                akan_result
            )


            return create_response(
                answer,
                "🇬🇭 Akan Knowledge Base",
                intent,
                language
            ), "🇬🇭 Akan Engine"



    # -----------------------------------
    # B. EDUCATIONAL KNOWLEDGE SEARCH
    # -----------------------------------

    knowledge = search_knowledge(topic)


    if knowledge:


        answer = format_knowledge(
            knowledge
        )


        return create_response(
            answer,
            "📚 Educational Knowledge Base",
            intent,
            language
        ), "📚 Knowledge Engine"



    # -----------------------------------
    # C. WEB FALLBACK
    # -----------------------------------

    web_answer = web_search(question)


    if web_answer:


        return create_response(
            web_answer,
            "🌍 Web Knowledge",
            intent,
            language
        ), "🌍 Web Engine"



    # -----------------------------------
    # D. NO RESULT
    # -----------------------------------

    return create_response(
        "Sorry, I could not find enough information about this topic.",
        "⚠️ System",
        intent,
        language
    ), "⚠️ No Answer"