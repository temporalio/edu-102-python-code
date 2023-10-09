import logging

from flask import Flask, jsonify, request

app = Flask(__name__)

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

# Define translations
translations = {
    "de": {"hello": "hallo", "goodbye": "auf wiedersehen", "thanks": "danke schön"},
    "es": {"hello": "hola", "goodbye": "adiós", "thanks": "gracias"},
    "fr": {"hello": "bonjour", "goodbye": "au revoir", "thanks": "merci"},
    "lv": {"hello": "sveiks", "goodbye": "ardievu", "thanks": "paldies"},
    "mi": {"hello": "kia ora", "goodbye": "poroporoaki", "thanks": "whakawhetai koe"},
    "sk": {"hello": "ahoj", "goodbye": "zbohom", "thanks": "ďakujem koe"},
    "tr": {"hello": "merhaba", "goodbye": "güle güle", "thanks": "teşekkür ederim"},
    "zu": {"hello": "hamba kahle", "goodbye": "sawubona", "thanks": "ngiyabonga"},
}


@app.route("/translate", methods=["GET"])
def translate():
    term = request.args.get("term")
    lang = request.args.get("lang")

    if not term:
        return jsonify({"error": "Missing required 'term' parameter"}), 500
    if not lang:
        return jsonify({"error": "Missing required 'lang' parameter"}), 500

    if lang not in translations:
        return jsonify({"error": f"Invalid language code '{lang}'"}), 500

    if term not in translations[lang]:
        return jsonify({"error": f"Invalid translation term '{term}'"}), 500

    translation = translations[lang][term]
    capitalized_translation = translation.capitalize()

    print(f"{term} translated to {lang} with result {translation}")

    return jsonify({"translation": capitalized_translation})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
