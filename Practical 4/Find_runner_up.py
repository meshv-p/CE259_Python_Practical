'''
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''

Score_times = int(input())
scores = [int(i) for i in input().split()]
if len(scores) == Score_times:
    new_sc = list(set(scores))
    new_sc.sort(reverse=True)
    print(new_sc[1])
else:
    print(f'You entered {Score_times} Scores,but You entered {len(scores)}.')