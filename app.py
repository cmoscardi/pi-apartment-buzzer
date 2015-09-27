from flask import Flask, request

from buzz import buzz

def get_app():
    app = Flask(__name__)

    @app.route("/send_text", methods=["POST"])
    def send_text():
        buzz(request.get_json()['Body'].strip())
        return "OK"
    
    return app

if __name__ == "__main__":
    app = get_app()
    app.run(debug=True)
