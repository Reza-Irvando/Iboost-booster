from flask import jsonify

def Make(Status, Message, Data):
    return jsonify({
        "status": int(Status),
        "message": str(Message),
        "data": Data
    })