# You  ar e  gi ven  an i nt eger array  hei ght  of l engt h  n. Ther e  are  n  verti cal li nes dr a wn  such t hat t he t wo  endpoi nt s  of t he it h li ne  are  (i,  0)  and  (i,  hei ght[i]).Fi nd  t wo  li nes  t hat  t oget her  wit h  t he  x-axi s  f or m  a  cont ai ner,  such  t hat  t he  cont ai ner cont ai ns the  most  wat er.Ret ur n t he  maxi mu m  a mount  of  wat er  a  cont ai ner  can  st or e.Not i ce t hat  you  may  not sl ant t he  cont ai ner.I nput:  hei ght  =  [ 1, 8, 6, 2, 5, 4, 8, 3, 7]


# Name: Meshv U Patel
# Id: 20CE092
# Github Repository Link: https://github.com/meshv-p/CE259_Python_Practical

def maxArea(A, Len):
    area = 0
    for i in range(Len):
        for j in range(i + 1, Len):
            area = max(area, min(A[j], A[i]) * (j - i))
    return area


a = [int(n) for n in input("Enter an array: ").split()]

len1 = len(a)
print(maxArea(a, len1))
