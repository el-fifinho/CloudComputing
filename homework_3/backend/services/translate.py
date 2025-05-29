from google.cloud import translate_v2 as translate

def translate_text(text, target_lang):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_lang)
    return result["translatedText"]