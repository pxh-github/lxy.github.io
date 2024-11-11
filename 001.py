M = list(input().split())
N = list(input().split())
not_dup = []
for each in M:
    if each not in N and each not in not_dup:
        not_dup.append(each)
for each in N:
    if each not in M and each not in not_dup:
        not_dup.append(each)
print(' '.join(not_dup))