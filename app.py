from flask import Flask, render_template, request
from googletrans import Translator

application = Flask(__name__, template_folder='templates')


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.form.get('text_to_translate')
    target_language = request.form.get('target_language')

    translator = Translator()
    translation_res = translator.translate(text_to_translate, dest=target_language)

    return render_template('index.html', translation_res=translation_res.text)


if __name__ == '__main__':
    application.run(debug=True)
