def single_root_words(root_word,*other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)

    print(same_words)

# single_root_words('apple', 'banana', 'applesauce', 'orange', 'appleseed')
single_root_words('Flower', 'flowering','Floral','Florist','Flourish','Floret','Floriculture')
single_root_words('Run', 'Runner', 'running', 'Runnable', 'Runarond', 'Runoff')
single_root_words('apple', 'banana', 'Applesauce', 'orange', 'appleseed')