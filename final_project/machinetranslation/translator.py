'''Translates languages using Watson!'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def load_translator():
    '''Loads the translator'''
    load_dotenv()
    apikey = os.environ['apikey']
    url = os.environ['url']
    authenticator = IAMAuthenticator(f'{apikey}')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(f'{url}')
    return language_translator

def translate(service, message='Hello world, how are you today?',
    model='en-fr'):
    '''Takes a message and translates it from english to french by default'''
    translation = service.translate(text=message,
    model_id=model).get_result()
    # print(json.dumps(translation, indent=2, ensure_ascii=False))
    # print(translation)
    return translation['translations'][0]['translation']

def english_to_french(english_text):
    '''Convenience method converting english to french'''
    if english_text is None:
        return None
    return translate(translator, english_text)

def french_to_english(french_text):
    '''Convenience method converting french to english'''
    if french_text is None:
        return None
    return translate(translator, message= french_text, model= 'fr-en')


translator = load_translator()
# translate(translator)
# words = english_to_french("Where are my freaking pants?")
# print(french_to_english(words))
