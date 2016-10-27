def checkletter(letter, i):
    for j in range(i,len(secret),3):
        if not ((letter ^ secret[j]) in chars):
            return False
    return True


characters=[range(65,91)]
characters.append(range(97,123))
characters.append(range(48,58))
characters.append([40,41,58,59,44,46,63,33,39,45,32])
chars=[item for sublist in characters for item in sublist]
chars.sort()

N=int(raw_input().strip())
secret=map(int,raw_input().strip().split(" "))
keyrange=range(97,123)
key=[0]*3
for i in range(3):
    for letter in keyrange:
        if checkletter(letter, i):
            key[i]=letter
            break

solution=[chr(letter) for letter in key]
print ''.join(solution)
