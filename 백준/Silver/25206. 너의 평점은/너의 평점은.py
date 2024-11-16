grade_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total_credit = 0
total_score = 0 

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade != 'P':
        total_credit += credit
        total_score += credit * score_list[grade_list.index(grade)]

print('%.6f' % (total_score/total_credit))