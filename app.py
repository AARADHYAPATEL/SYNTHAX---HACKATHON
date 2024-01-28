from flask import Flask, render_template, request
from googletrans import Translator
from binary_converter import binary_addition
from binary_converter import binary_subtraction
from binary_converter import binary_multiplication
from binary_converter import binary_division

application = Flask(__name__, template_folder='templates')


@application.route('/binary-conversion', method=['POST'])
def Binary_operation():
    if request.method == 'POST':
        binary_input1 = request.form.get('binary_input1')
        binary_input2 = request.form.get('binary_input2')
        op = request.form.get('op')

        if op == 'addition':
            res = binary_addition(binary_input1, binary_input2)
        elif op == 'subtraction':
            res = binary_subtraction(binary_input1, binary_input2)
        elif op == 'Multiplication':
            res = binary_multiplication(binary_input1, binary_input2)
        elif op == 'Division':
            Quo, rem = binary_division(binary_input1, binary_input2)
            res = f"Quotient: {Quo}, Remainder: {rem}"
        else:
            res = "Invalid Operation"

        return render_template('binary_conversion.html', res=res)

    return render_template('binary_conversion.html')


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
