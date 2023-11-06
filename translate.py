from googletrans import Translator

"""This is a message"""

def translate_to_italian(text):
    translator = Translator()

    try:
        translated = translator.translate(text, src='en', dest='it')
        return translated.text
    except Exception as e:
        return str(e)



if __name__ == "__main__":
    text_to_translate = input("Enter the text in English to translate to Italian: ")
    translated_text = translate_to_italian(text_to_translate)
    print("Translated to Italian: ", translated_text)
