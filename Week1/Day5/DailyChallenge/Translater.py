from deep_translator import GoogleTranslator

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translator = GoogleTranslator(source='fr', target='en')

translates = {
    word : translator.translate(word)
    for word in french_words
}

print(translates)