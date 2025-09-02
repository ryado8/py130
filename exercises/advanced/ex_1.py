import re

def longest_sentence(text):
    sentences = re.findall(r'[^ .!?]+[^.!?]*[.!?]', text)

    longest = max(sentences, key=lambda s: len(s.split()))

    print(longest + "\n")
    print(f"The longest sentence has {len(longest.split())} words.\n")