import sys

def main(text):
    n = set(text.lower())
    base = 0
    for i in "aieou":
        if i in n:
            base += 1
    
    return(base)

print(main(sys.argv[1]))