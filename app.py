from flask import Flask, request

from buzz import buzz

RESP = """<?xml version="1.0" encoding="UTF-8" ?>  
<Response> 
</Response>"""

def get_app():
    app = Flask(__name__)

    @app.route("/send_text", methods=["POST"])
    def send_text():
        buzz(request.form['Body'].strip())
        return RESP
    

    @app.route("/")
    def index():
        return "HEY"

    return app

if __name__ == "__main__":
    app = get_app()
    app.run(debug=True, port=80, host='0.0.0.0')
