n = int(input())
score1, score2 = 0, 0
lead1, lead2 = 0, 0

for i in range (n):
    s1, s2 = map(int, input().split())
    score1 += s1
    score2 += s2
    lead = abs(score1 - score2)
    if score1 > score2:
        if lead > lead1:
            lead1 = lead
    else:
        if lead > lead2:
            lead2 = lead

if (lead1 > lead2):
    print(1, lead1)
else:
    print(2, lead2)