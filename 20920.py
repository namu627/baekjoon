import sys
input = sys.stdin.readline

n, m = map(int, input().split())

count={}
for _ in range(n):
    word=input().strip() 
    
    if len(word) >= m:
        if word in count:
            count[word] += 1
        else:
            count[word]=1

unique_words = list(count.keys())

unique_words.sort(key=lambda x: (-count[x], -len(x), x))
print('\n'.join(unique_words))