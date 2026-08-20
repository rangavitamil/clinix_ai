from flask import Flask, render_template, request, jsonify
from datetime import datetime, timezone

from chatbot_config import get_ai_response


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "Invalid request."
            }), 400

        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({
                "success": False,
                "error": "Message cannot be empty."
            }), 400

        # Get response from Gemini
        ai_response = get_ai_response(user_message)

        return jsonify({
            "success": True,
            "response": ai_response,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

    except Exception as e:

        print("ERROR:", repr(e))

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )