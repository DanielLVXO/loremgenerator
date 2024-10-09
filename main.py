def print_lorem(): 
    file = open("lorem.txt", "r", encoding="utf-8")
    for line in file:
        print(line, end="")
    file.close()

def lorem_lines(lines):
    file = open("lorem.txt", "r", encoding="utf-8")
    lorem = file.readlines()
    file.close()
    return lorem[0:lines]

def get_lorem_words():
    file = open("lorem.txt", "r", encoding="utf-8")
    lorem = file.readlines()
    file.close()
    words = lorem[0].split(" ")
    return words


def main():
    print_lorem()

    print(lorem_lines(1))

    lorem_words = get_lorem_words()    
    for i in range(50): #skriv ut första 50
         print(lorem_words[i], end=" ")   




main()

