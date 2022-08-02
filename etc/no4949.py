import sys

R = []
S = ""
while S!=".":
    S = sys.stdin.readline().strip()
    R.append(S)

def valance(R):
    left = ['(','[']
    right = [')',']']
    for r in R:
        i = 0
        j = len(r)-1
        while i<j:
            while r[i] not in left:
                if i<j:
                    break
                i += 1
            while r[j] not in right:
                if i<j:
                    break
            r = r[i+1:j]

valance(R)