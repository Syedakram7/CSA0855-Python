def countstrings(n,start):
    if n==0:
        return 1
      cnt = 0
      fori in range(start,5):
        cnt+=countstrings(n-1,i)
        return cnt
def countvowelsstrings(n):
  return countstrings(n,0)
n=int(input("enter the n value"))
print(countvowelstrings(n))
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Con
