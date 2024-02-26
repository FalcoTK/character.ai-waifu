from easygoogletranslate import EasyGoogleTranslate as esgt
import config


def translaout(testout):
    translator = esgt(
    source_language='en',
    target_language=config.target_lang,
    timeout=5)

    resoult = translator.translate(testout)
    
    # debug check
    if config.debug ==True:
        print("[dbg] Translate: " + resoult)

    return resoult



def translain(testin):
    translator = esgt(
    source_language='id',
    target_language='en',
    timeout=5)

    resoult = translator.translate(testin)

    # debug check
    if config.debug ==True:
        print("[dbg] Translate: " + resoult)

    return resoult
