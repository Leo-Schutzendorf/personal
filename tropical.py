import re
import numpy as np
def insert_char_slicing(string, char, position):
    # s[:n] gets characters from start to index n (exclusive)
    # s[n:] gets characters from index n (inclusive) to the end
    return string[:position] + char + string[position:]

def main():
    expression = input("Type expression: ").strip()
    for char in expression:
        if char == "-":
            expression = insert_char_slicing(expression, "+", expression.index(char))
    firstGetMin = re.split(r"\+", expression)

    print(firstGetMin)

    getMin=[]
    for term in firstGetMin:
        getMin.append(term.split("*"))

    print(getMin)

if __name__== "__main__":
    main()