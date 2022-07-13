""" Translate from English to French or French to English using IBM Watson """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from sqlalchemy import null

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(False)
language_translator.set_default_headers({'x-watson-learning-opt-out': "true"})

def english_to_french(english_text):
    """Translate English to French"""
    french_text = ""
    if english_text is null :
        return french_text
    try:
        translation = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
        french_text = ((translation['translations'])[0])['translation']
    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
    return french_text

def french_to_english(french_text):
    """Translate French to English"""
    english_text = ""
    if french_text is null :
        return english_text
    try:
        translation = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
        english_text = ((translation['translations'])[0])['translation']
    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)

    return english_text
