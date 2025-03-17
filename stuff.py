def phoeneticGenerator(base_str):
    nato_alphabet = {"a":"alpha","b":"bravo","c":"charlie","d":"delta","e":"echo","f":"foxtrot","g":"golf","h":"hotel","i":"india","j":"juliet","k":"kilo","l":"lima","m":"mike",
                 "n":"november","o":"oscar","p":"papa","q":"quebec","r":"romeo","s":"sierra","t":"tango","u":"uniform","v":"victor","w":"whiskey","x":"x-ray","y":"yankee","z":"zulu"}

    lowered = base_str.lower()
    phonetic = ""
    for char in lowered:
        if nato_alphabet.get(char):
            phonetic += nato_alphabet.get(char)
        else:
            phonetic += char
        
        phonetic += ","

    return phonetic
