from playsound import *
import speech_recognition as speech
from googletrans import *
from gtts import *
import os
flag = 0
# dictionary of known languages of overseas bases and affiliates
language = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am',
            'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
            'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian',
            'bs', 'bulgarian', 'bg', 'catalan', 'ca',
            'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
            'zh-cn', 'chinese (traditional)', 'zh-tw',
            'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish',
            'da', 'dutch', 'nl', 'english', 'en', 'esperanto',
            'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi',
            'french', 'fr', 'frisian', 'fy', 'galician', 'gl',
            'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati',
            'gu', 'haitian creole', 'ht', 'hausa', 'ha',
            'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong',
            'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo',
            'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it',
            'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn',
            'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)',
            'ku', 'kyrgyz', 'ky', 'lao', 'lo',
            'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish',
            'lb', 'macedonian', 'mk', 'malagasy',
            'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori',
            'mi', 'marathi', 'mr', 'mongolian', 'mn',
            'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no',
            'odia', 'or', 'pashto', 'ps', 'persian',
            'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
            'romanian', 'ro', 'russian', 'ru', 'samoan',
            'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho',
            'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala',
            'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so',
            'spanish', 'es', 'sundanese', 'su',
            'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil',
            'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
            'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek',
            'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
            'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')


# function to take in speech from microphone
def takeLang():
    sp = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        sp.pause_threshold = 1
        audio = sp.listen(source)

    try:
        print("Recognizing language...")
        query = sp.recognize_google(audio, language='en-in')
        print(f"Person said {query}\n")

    except Exception as e:
        print("Could you say that again?")
        return "None"

    return query


# take voice input from user
query = takeLang()
while query == "None":
    query = takeLang()


def dest_lang():
    print("Enter language to convert to: ")
    print()

    transto = takeLang()
    while transto == "None":
        transto = takeLang()
    transto = transto.lower()
    return transto


to_lang = dest_lang()

# checks is language chosen is available
while to_lang not in language:
    print("The language you are trying to translate to is unavailable, try another language.")
    print()
    to_lang = dest_lang()

to_lang = language[language.index(to_lang) + 1]

# invokes Translator
translate = Translator()
text_to_translate = translate.translate(query, lang_tgt=to_lang)
text = text_to_translate.text

# Speak the translated text from the word or sentence received to store it as mp3 for playback
speak = gTTS(text=text, lang=to_lang, slow=False)

speak.save("captured_voice.mp3")

# plays the translated sentence and deletes when done
playsound("captured_voice.mp3")
os.remove("captured_voice.mp3")

print(text)
