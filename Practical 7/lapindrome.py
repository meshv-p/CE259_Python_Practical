'''
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Python_Practical
    Aim: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 
'''
tc = int(input())
for i in range(tc):
    s = input()
    if len(s)%2 == 0:
        if s[:int(len(s)/2)] == s[int(len(s)/2):] or s[:int(len(s)/2)] == s[int(len(s)/2)+1:][::-1]: 
            print('YES')
        else:
            print('NO')
    else:
        if s[:int(len(s)/2)] == s[int(len(s)/2)+1:] or s[:int(len(s)/2)] == s[int(len(s)/2)+1:][::-1]:
            print('YES')
        else:
            print('NO')
    



