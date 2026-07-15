from flask import Flask, request, jsonify, render_template

from model.qa_engine import get_answer


# ---------------------------------------
# FLASK APPLICATION
# ---------------------------------------

app = Flask(__name__)



# ---------------------------------------
# HOME PAGE
# ---------------------------------------

@app.route("/")
def home():

    return """
    <h1>Knowledge-Centered Intelligent Assistant</h1>

    <p>System is running successfully.</p>

    <p>Use the /ask endpoint to test questions.</p>
    """



# ---------------------------------------
# QUESTION ANSWERING API
# ---------------------------------------

@app.route("/ask", methods=["POST"])
def ask():

    try:

        data = request.get_json()


        question = data.get(
            "question",
            ""
        )


        if not question:

            return jsonify({

                "answer":
                "Please enter a question.",

                "source":
                "Input Error"

            })



        answer, source = get_answer(
            question
        )


        return jsonify({

            "answer": answer,

            "source": source

        })



    except Exception as e:


        print(
            "Server Error:",
            e
        )


        return jsonify({

            "answer":
            "An error occurred while processing your question.",

            "source":
            "System Error"

        })



# ---------------------------------------
# RUN SERVER
# ---------------------------------------

if __name__ == "__main__":


    print(
        "🚀 Intelligent Educational Assistant Running..."
    )


    app.run(
        debug=True
    )