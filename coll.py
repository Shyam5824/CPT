from collections import Counter
text=input()
counter=Counter(text)
print("Characters frequencies:",dict(counter))
