name1,weight_1,score1_1,score1_2,name2,weight_2,score2_1,score2_2 = input().split(" ")
score1_1 = float(score1_1)
score1_2 = float(score1_2)
score2_1 = float(score2_1)
score2_2 = float(score2_2)
a_score = score1_1 + score1_2
b_score = score2_1 + score2_2
if a_score == b_score and float(weight_1) < float(weight_2):
    print(name1)
elif a_score == b_score and float(weight_2) < float(weight_1):
    print(name2)
elif a_score > b_score:
    print(name1)
elif a_score < b_score:
    print(name2)
