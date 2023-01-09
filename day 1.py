def isIso(x,y):
  if len(x)!=len(y):
    return False
  for i in range(len(x)):
    count=0
    if x.count(x[i])!=y.count(y[i]):
      return False
  return True
print(isIso('fool','poor'))
print(isIso('fool','poor'))
print(isIso('too','bar'))
print(isIso('toto','yaya'))







l=[8,7,6,9,13,23,42,77,23]
def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even = even + i**2
        else:
            odd = odd + i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))






def sumDigitsquare(n):
    sq = 0;
    while (n !=0):
        digit = n%10
        sq += digit * digit
        n = n// 10
    return sq;
def isHappy(n):
    s=set()
    s.add(n)
    while (True):
        if (n==1):
            n=sumDigitSquare(n)
        if n in s:
            return False
        s.add(n)
    return False;
n=19
if(isHappy(n)):
    print('Yes')
else:
    print("No")







def oneDigit(num):
    return ((num >=0) and
            (num < 10))
def isPalUtil(num, dupNum):
    if oneDigit(num):
        return (num == (dupNum[0])% 10)
    if not isPalUtil(num // 10, dupNum):
        return False
    dupNum[0] = dupNum[0] // 10
    return (num % 10 == (dupNum[0])% 10)
def isPal(num):
    # if num is negative,
    # make it positive
    if (num < 0):
        num = (-num)
    dupNum = [num] # *dupNum = num
    return isPalUtil(num, dupNum)
n= 12321
if isPal(n):
    print("Yes")
else:
    print("No")




fresh=int(input('enter the number of fresh loves purchased'))
old=int(input('enter the number of the day old loves purchased'))
print('regular price: Rs.185.00')
fresh_amount = 185.00*float(fresh)
old_amount = (185*0.4)*float(old)
Total=fresh_amount+old_amount
print('amount of new loaves:Rs',fresh_amount)
print('amount of day old loaves:Rs:',old_amount)
print('total amount: Rs:',Total)





class Solution:
    def maxArea(self, A):
        maxarea =0
        l= 0
        r= len(A) - 1
        while l < r:
            base = r-1
            height = min(A[l], A[r])
            area = base * height
            maxarea = max(area, maxarea)
            if A[l] < A[r]:
                l+=1
            else:
                r -=1
        return maxarea
ob=Solution()
print(ob.maxArea([1,5,4,3]))
print(ob.maxArea([3,1,2,4,5]))




def countstrings(n, start):
    if n == 0:
        return 1
    count = 0
    for i in range(start, 5):
        count += countstrings(n - 1, i)
    return count
def countVowelStrings(n):
    # char arr[5]={'a','e','i','o','u'};
    # starting from index 0 add the vowels to strings
    return countstrings(n, 0)
n = 1
print(countVowelStrings(n))



def isNumeric(s):
    s = s.strip
    try:
        s= float(s)
        return True
    except:
        return False
print(isNumeric('0.2'))
print(isNumeric('xyz'))
print(isNumeric('hello'))
print(isNumeric('10'))




      
time=int(input())
entry=list(map(int, input().split()))
exit=list(map(int, input().split()))
present=0
Total_guests=0
for i in range(time):
    present += entry[i]-exit[i]
    if Total_guests < present:
        Total_guests = present
print(Total_guests,end = " ")



def addFrequencyToCharacter(s):
    frequency = [0] * 26
    n = len(s)
    for i in range(n):
        frequency[ord(s[i]) - ord('a')] += 1
    for i in range(n):
        add = frequency[ord(s[i]) - ord('a')] % 26
        if (ord(s[i]) + add <= ord('z')):
            s[i] = chr(ord(s[i])+ add)
        else:
            add = (ord(s[i]) + add) - (ord('z'))
            s[i] = chr(ord('a') + add - 1)
    print(''.join(s))
if __name__ == '__main__':
    str = 'ghee'

    addFrequencyToCharacter([i for i in str])'''

















                
