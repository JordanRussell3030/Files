with open("textfiles2.txt", mode = "r", encoding = "utf-8") as text_file:
    for line in text_file:
        print(line, end = "")
