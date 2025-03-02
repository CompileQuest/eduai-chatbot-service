from flask import Blueprint, request, jsonify
from app.services.intent_detection.intent_detection import detect_intent
from app.services.sentiment_analysis.sentiment_analysis import analyze_sentiment, save_feedback
from app.services.intent_detection.schemes import Message
chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/intent_detect", methods=["POST"])
def handle_intentDetection():
    data = request.get_json()
    user_message = Message(**data) # Ensure we're parsing JSON
    if not user_message:
        return jsonify({"error": "Invalid JSON body"}), 400
    return detect_intent(user_message)

@chatbot_bp.route("/analyze_sentiment",methods = ["POST"])
def handle_sentimentAnalysis():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"error:" "Invalid JSON body"}),400
    return analyze_sentiment(data)

