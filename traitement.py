from deep_translator import GoogleTranslator

def translate(text):
    return GoogleTranslator(source='en', target='fr').translate(text)

res = []
with open ("./static/words", 'r') as f:
    lines = f.readlines()
    s = len(lines)
    for i in range(s):
        res.append(translate(lines[i].strip()))
        print(str(i/s*100) + "%", end="\r")

with open ("./static/words_fr", 'w') as f:
    for line in res:
        f.write(line + "\n")

    