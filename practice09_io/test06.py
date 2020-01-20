with open("171160.txt", 'r', encoding='utf8') as f:
    for item in f.readlines():
        if item != '\n':
            print(item.replace('\n', ''))
