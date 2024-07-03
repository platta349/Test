text1 = "Питон — мощный язык программирования. Он широко используется в науке о данных."
text2 = "Питон хорош для анализа данных. Он также используется в веб-разработке."
symbols = ".,!?:;'\"-—"
for symbol in symbols:
    text1 = text1.replace(symbol, '')
    text2 = text2.replace(symbol, '')
text1 = text1.lower()
text2 = text2.lower()

slova1 = text1.split()
slova2 = text2.split()

uniqaln_slova1 = []
uniqaln_slova2 = []

for word in slova1:
    if word not in slova2:
        uniqaln_slova1.append(word)

for word in slova2:
    if word not in slova1:
        uniqaln_slova2.append(word)
print("Уникальные слова в первом тексте:", uniqaln_slova1)
print("Уникальные слова во втором тексте:", uniqaln_slova2)

obschie_slova = []
for word in uniqaln_slova1:
    if word in uniqaln_slova2:
        obschie_slova.append(word)
for word in uniqaln_slova2:
    if word in uniqaln_slova1:
        obschie_slova.append((word))
print("Общие слова:", obschie_slova)

edenstv_slova1 = set()
edenstv_slova2 = set()

for word in slova1 :
    edenstv_slova1.add(word)
for word in slova2:
    edenstv_slova2.add(word)

print("Слова, повторяющиеся один раз за весь текст", edenstv_slova1)
print("Слова, повторяющиеся один раз за весь текст", edenstv_slova2)

unikalniye = []
for word in uniqaln_slova1:
    if word not in uniqaln_slova2 and word not in unikalniye:
        unikalniye.append(word)
for word in uniqaln_slova2:
    if word not in uniqaln_slova1 and word not in unikalniye:
        unikalniye.append(word)
print("Слова, которые присутствуют только в одном из текстов:", unikalniye)   