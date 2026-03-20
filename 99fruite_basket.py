# brute force solution 
class Solution:
    def totalFruit(self,fruits):

        uniqe=list(set(fruits))
        maxi=0

        for i in range(len(uniqe)):
            for j in range(i,len(uniqe)):
                fr1=uniqe[i]
                fr2=uniqe[j]
                curr=0
                for k in fruits:
                    if k==fr1 or k==fr2:
                        curr+=1
                        maxi=max(maxi,curr)
                    else:
                        curr=0
        
        return maxi

# optimal solution 
class Solution:
    def totalFruit(self,fruits):
        dic={}
        L=0
        R=0
        maxi=0
        while R<len(fruits):
            if fruits[R] in dic:
                dic[fruits[R]]+=1
            else:
                dic[fruits[R]]=1
            R+=1  
            if len(dic)>2:
                if dic[fruits[L]]==1:
                    del dic[fruits[L]]
                else:
                    dic[fruits[L]]-=1
                L+=1
           
            maxi=max(maxi,R-L)
            
            
        return maxi




s=Solution()
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

        