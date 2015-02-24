text = None
texts = []
for count in range(5):
    text = input("Please input a line of text: ")
    texts.append(text)

with open("textlines.txt", mode = "w", encoding = "utf-8") as text_file:
    for text in texts:
        text_file.write(text)
        text_file.write("\n")
    
