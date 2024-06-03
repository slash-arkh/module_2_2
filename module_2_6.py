def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        a = i.lower()
        if root_word.lower() in a or a in root_word.lower():
            same_words.append(i)
    return same_words
result1 = single_root_words('as' , 'ask','pasa', 'sdfs', 'gas', 'los')
result2 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result3 = single_root_words('able','Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
print(result3)