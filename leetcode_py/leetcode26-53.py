26. 删除排序数组中的重复项
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range(len(nums)):
            if i<1 or nums[j] != nums[j-1]:
                nums[i]=nums[j]
                i+=1
        return i

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        slow,fast=0,0
        while slow<l:
            if slow > 0 and nums[slow]<=nums[slow-1]:
                while fast<l and nums[fast]<=nums[slow-1]:
                    fast+=1
                if fast == l:
                    return slow
                else:
                    nums[slow] = nums[fast]
            slow += 1
        return slow

27. 移除元素
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i=0
        for j in range(0,len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=len(nums)
        for i in range(l-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

28. 实现strStr()
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i,char in enumerate(haystack):
            if char == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

29. 两数相除
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        op=1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            op=-1
        dividend,divisor = abs(dividend),abs(divisor)
        res=0
        while dividend>=divisor:
            dividend-=divisor
            res+=1
        INT_MIN=-(2**31)
        INT_MAX=2**31-1
        res*=op
        return res if INT_MIN<=res<=INT_MAX else INT_MAX

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        op=1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            op=-1
        dividend,divisor=abs(dividend),abs(divisor)
        res=0
        while dividend>=divisor:
            multidivisor,multi=divisor,1
            while dividend>=multidivisor:
                res += multi
                dividend-=multidivisor
                multi = multi<<1
                multidivisor=multidivisor<<1
        INT_MIN=-(2**31)
        INT_MAX=2**31-1
        res *= op
        return res if INT_MIN<=res<=INT_MAX else INT_MAX

31. 下一个排列
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        for i in range(l-1,-1,-1):
            if nums[i-1]<nums[i]:
                break
        if i== 0:
            nums[:]=nums[::-1]
            return nums

        for j in range(l-1,i-1,-1):
            if nums[j] > nums[i-1]:
                break

        nums[i-1],nums[j] = nums[j],nums[i-1]
        nums[i:] = nums[i:][::-1]
        return nums

32. 最长有效括号
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)):
            for j in range(i+1,len(s),2):
                if self.isValid(s[i:j+1]):
                    res = max(res,j-i+1)
        return res
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
         mapping = {")":"(", "]":"[", "}":"{"}
         stack=[]
         for i,char in enumerate(s):
            if char not in mapping:
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return len(stack) == 0

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[-1]
        res=0
        for i,x in enumerate(s):
            if x=="(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res=max(res,i-stack[-1])
                else:
                    stack.append(i)
        return res

33. 搜索旋转排序数组
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if mid+1<len(nums) and nums[mid]>nums[mid+1]:
                break
            if nums[mid] < nums[-1]:
                hi=mid-1
            elif nums[mid] >= nums[0]:
                lo=mid+1
        if lo>hi:
            lo,hi=0,len(nums)-1
        else:
            if target >= nums[0]:
                lo,hi = 0,mid
            else:
                lo,hi=mid+1,len(nums)-1

        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi=mid-1
            else:
                lo=mid+1

        return -1

34. 在排序数组中查找元素的第一个和最后一个位置
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo,hi = 0,len(nums) - 1
        while lo <= hi:
            mid=(lo+hi)//2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                hi=mid-1
            else:
                lo=mid+1
        if lo>hi:
            return [-1,-1]

        midtarget=mid
        lo,hi=0,mid
        leftpos=0
        while lo<=hi:
            if (hi>=1 and nums[hi-1]!=target) or hi==0:
                leftpos=hi
                break
            mid=(lo+hi)//2
            if nums[mid]==target:
                hi=mid
            elif nums[mid]<target:
                lo=mid+1

        rightpos=0
        lo,hi=midtarget,len(nums)-1
        while lo<=hi:
            if (lo<=len(nums)-2 and nums[lo+1] !=target) or lo=len(nums)-1:
                rightpos=lo
                break
            mid=(lo+hi+1)//2
            if nums[mid] == target:
                lo=mid
            elif nums[mid] > target:
                hi=mid-1

        return [leftpos,rightpos]

35. 搜索插入位置
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return sorted(list(set(nums+[target]))).index(target)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                hi=mid-1
            else:
                lo=mid+1
        return lo

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,nums in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

36. 有效的数独
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        row,column,squre=defaultdict(set),defaultdict(set),defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in squre[(i//3,j//3)]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        column[j].add(board[i][j])
                        squre[(i//3,j//3)].add(board[i][j])
        return True

37. 解数独
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        row,column,squre = defaultdict(set),defaultdict(set),defaultdict(set)
        fill_set=[]
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    row[i].add(board[i][j]).encode("utf-8")
                    column[j].add(board[i][j]).encode("utf-8")
                    squre[(i//3,j//3)].add(board[i][j]).encode("utf-8")
                else:
                    fill_set.append([i,j])

        self.resul=[]
        def backtrack(idx):
            if idx == len(fill_set):
                for row1 in board:
                    self.result.append(row1[:])
                return
            if not self.result:
                i,j=fill_set[idx][0],fill_set[idx][1]
                for digit in range(1,10):
                    if str(digit) in row[i] or str(digit) in column[j] or str(digit) in squre[(i//3,j//3)]:
                        continue
                    board[i][j] = str(digit)
                    row[i].add(board[i][j])
                    column[j].add(board[i][j])
                    squre[(i//3,j//3)].add(board[i][j])

                    backtrack(idx+1)

                    row[i].remove(board[i][j])
                    column[j].remove(board[i][j])
                    squre[(i//3,j//3)].remove(board[i][j])

        backtrack(0)
        for i in range(9):
            for j in range(9):
                board[i][j]=self.result[i][j]

#2019.6.6解法如下：
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        row, column, squre  = defaultdict(set), defaultdict(set), defaultdict(set)
        
        self.res = []
        def dfs(x,y):

            if x==8 and y==9:
                for roww in board:
                    self.res.append(roww[:])
                return
            if y==9:
                dfs(x+1,0)
                return
            if board[x][y].isdigit():
                dfs(x,y+1)
                return

            for k in range(1,10):
                if str(k) not in row[x] and str(k) not in column[j] and str(k) not in squre[(i//3,j//3)]
                board[x][y]=str(k)
                row[x].add(str(k))
                column[y].add(str(k))
                squre[(x//3,y//3)].add(str(k))

                dfs(x,y+1)

                board[x][y]="."
                row[x].remove(str(k))
                column[y].remove(str(k))
                squre[(x//3,y//3)].remove(str(k))

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    row[i].add(board[i][j].encode("utf-8"))
                    column[j].add(board[i][j].encode("utf-8"))
                    squre[(i // 3, j // 3)].add(board[i][j].encode("utf-8"))
 
        dfs(0, 0)
        board[:] = self.res

38. 报数
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        record=["1"]
        for i in range(1,n):
            pre=record[i-1]
            idx=0
            tmp=""
            while idx<len(pre):
                cnt=1
                while (idx+1<len(pre) and pre[idx]==pre[idx+1]):
                    idx+=1
                    cnt+=1
                tmp+=str(cnt)+pre[idx]
                idx+=1
            record.append(tmp)
        return record[-1]

#leetcode 39. 组合总和
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
class Solution:
    def combinationSum(self，candidates:List[int],target:int)->List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path=[]
        res=[]
        self._dfs(candidates,0,size,path,res,target)
        return res
    def _dfs(self,candidates,begin,size,path,res,target):
        if target == 0:
            res.append(path[:])
            return
        for index in range(begin,size):
            residue = target-ccandidates[index]
            if residue < 0 :break
            path.append(candidates[index])
            self._dfs(candidates,index,size,path,res,residue)
            path.pop()
if __name__ == '__main__':
    candidates=[2,3,6,7]
    target=7
    solution=Solution()
    res=Solution.combinationSum(candidates,target)
    print(res)
# 40. 组合总和 II
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
class Solution:
    def combinationSum2(self,candidates:List[int],target:int)->List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path=[]
        res=[]
        self._DFS(candidates,target,0,path,res)
        return res
    def _DFS(self,candidates,target,begin,path,res):
        if target == 0:
            res.append(path[:])
            return
        if begin > len(candidates)-1:return
        for cur in range(begin,len(candidates)):
            if cur>begin and candidates[cur] == candidates[cur-1]:
                continue
            temp=target-ccandidates[cur]
            if temp<0:return
            else:
                path.append(candidates[cur])
                self._DFS(candidates,temp,cur+1,path,res)
                path.pop()

# 216. 组合总和 III
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
class Solution:
    def combinationSum3(self,k:int,n:int)->List[List[int]]:
        res=[]
        def helper(count,i,tmp,target):
            print(count,i,tmp,target)
            if count == k:
                if target == 0:
                    res.append(tmp.copy())
                return
            for j in range(i,10):
                if j>target:
                    break
                helper(count+1,j+1,tmp+[j],target-j)
        helper(0,1,[],n)
        return res

class Solution:
    def combinationSum3(self,k:int,n:int)->List[List[int]]:
        def back(candidates,cur,target,length):
            if len(cur)==length and target==0:
                res.append(cur.copy())
                return
            for i in range(len(candidates)):
                if len(cur)>0 and candidates[i] < cur[-1]:
                    continue
                cur.append(candidates[i])
                back(candidates[:i]+candidates[i+1:],cur,target-candidates,length)
                cur.pop()
        res=[]
        nums=[i for i in range(1,10)]
        back(nums,[],n,k)
        return res

# 377. 组合总和 Ⅳ
# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
# 示例:
# nums = [1, 2, 3]
# target = 4
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 因此输出为 7。
class Solution(object):
    def combinationSum4(self,nums:List[int],target:int)->int:
        if not nums:
            return 0
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for num in nums:
                if i>=num:
                    dp[i]+=dp[i-num]
        return dp[target]

# 77. 组合
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 示例:
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
class Solution(object):
    def combine(self,n:int,k:int)->List[List[int]]:
        if n<=0 or k<=0 or k>n:
            return []
        res=[]
        self._dfs(1,k,n,[],res)
        return res
    def _dfs(self,start,k,n,pre,res):
        if len(pre)==k:
            res.append(pre[:])
            return
        for i in range(start,n+1):
            pre.append(i)
            self._dfs(i+1,k,n,pre,res)
            pre.pop()




39. 组合总和
#回溯法。
#自己写的丑陋版本，很慢……
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=list()
        def generate(c,t,tmp,s):
            if s==target:
                res.append(tmp[:])
                return
            if s>t:
                return
            for digit in c:
                s=sum(tmp)+digit
                tmp.append(digit)
                generate(c,t,tmp,s)
                tmp.pop()
        generate(candidates,target,[],0)
        for i in range(0,len(res)):
            res[i].sort()
        ress=list()
        for i in range(0,len(res)):
            flag=0
            for j in range(i+1,len(res)):
                if res[i] == res[j]:
                    flag=1
                    break
            if not flag:
                ress.append(res[i])
        return ress

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        def backtrack(remain,temp,start):
            if not remain:
                res.append(temp[:])
            else:
                for i,n in enumerate(candidates[start:]):
                    if n>remain:
                        break
                    backtrack(remain-n,temp+[n],start+i)
        backtrack(target,[],0)
        return res

40. 组合总和 II
class Solution(object):
    def combinationSum2(self, c, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=list()
        l=len(c)
        def dfs(start,tmp):
            s=sum(tmp)
            if s==t:
                tt=sort(tmp)
                if tt not in res:
                    res.append(tt[:])
                return
            if start>=l:
                return
            for i in range(start,l):
                if c[i]>t or s+c[t]>t:
                    continue
                tmp.append(c[i])
                dfs(i+1,tmp)
                tmp.pop()

        for i,x in enumerate(c):
            dfs(i,list())

        return res

41. 缺失的第一个正数
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while 1<=nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]

        for i,x in enumerate(nums):
            if x!=i+1:
                return i+1

        return len(nums)+1

42. 接雨水
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max=[0 for _ in height]
        right_max=[0 for _ in height]
        water=[0 for _ in height]
        for i in range(len(height)):
            if i-1>=0:
                left_max[i]=max(left_max[i-1],height[i])
            else:
                left_max[i]=height[i]
        for i in range(len(height)-1,-1,-1):
            if i<len(height)-1:
                right_max[i]=max(right_max[i+1],height[i])
            else:
                right_max[i]=height[i]
        for i in range(len(height)):
            tmp=min(left_max[i],right_max[i])-height[i]
            if tmp>0:
                water[i]=tmp
        return sum(water)

43. 字符串相乘
# # 第二种思路：
# # 作弊……
# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         return str(int(num1)*int(num2))

# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         if len(num1) < len(num2):
#             num1,num2=num2,num1
#         if num1 == "0" or num2 == "0":
#             return "0"

#         num2=num2[::-1]
#         tmp,res=[],[]
#         for i,char in enumerate(num2):
#             tmp=self.stringMultiDigit(num1,int(char))+"0"*i
#             res=self.stringPlusString(res,tmp)
#         return "".join(res)
#         def stringMultiDigit(self,s,n):
#             s=s[::-1]
#             l=[]
#             for char in s:
#                 l.append(int(char))
#             for i,char in enumerate(l):
#                 l[i]*=n
#             for i,char in enumerate(l):
#                 while l[i]>9:
#                     tmp=l[i]//10
#                     l[i]-=tmp*10
#                     if i==len(l)-1:
#                         l.append(0)
#                     l[i+1]+=tmp
class Solution(object):
    def multiply(self,num1:str,num2:str):
        a=list(num1)
        b=list(num2)
        c=[0]*(len(num1)+len(num2))
        for i in range(len(a)):
            a[i]=int(a[i])
        for i in range(len(b)):
            b[i] = int(b[i])
        a.reverse()
        b.reverse()

        for i in range(len(a)):
            for j in range(len(b)):
                c[i+j] += a[i]*b[j]

        ans=""
        for i in range(len(c)):
            if i+1<len(c):
                c[i+1]+=c[i]//10
            c[i] = c[i]%10
            ans=str(c[i])+ans
        ans=ans.lstrip("0")
        return "0" if ans == "" else ans

46. 全排列
class Solution(object):
    def permute(self,nums:List[int])->List[List[int]]:
        res=[]
        def back(nums,tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                back(nums[:i]+nums[i+1:]，tmp+[nums[i]])
        back(nums,[])
        return res

class Solution(object):
    def permute(self,nums:List[int])->List[List[int]]:
        if depth==size:
            res.append(path[:])
            return
        for i in range(size):
            if not used[i]:
                used[i]=True
                path.append(nums[i])

                dfs(nums,size,depth+1,path,used,res)

                used[i]=False
                path.pop()

        size=len(nums)
        if len(nums)==0:
            return []
        used=[False for _ in range(size)]
        res=[]
        dfs(nums,size,0,[],used,res)
        return res

from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums,len(nums)))

47. 全排列 II
class Solution:
    def permuteUnique(self,nums:List[int])->List[List[int]]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        res=[]
        def back(dic,path):
            if len(nums)==len(path):
                res.append(path[:])
            for i in dic.keys():
                if dic[i]==0:
                    continue
                dic[i]-=1
                path.append(path)
                back(dic,path)
                path.pop()
                dic[i]+=1
        back(dic,[])
        return res

class Solution:
    def permuteUnqiue(self,nums:List[int])->List[List[int]]:
        def dfs(nums,size,depth,path,used,res):
            if depth==size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                        continue
                    used[i]=True
                    path.append(nums[i])
                    dfs(nums,size,depth+1,path,used,res)
                    used[i]=False
                    path.pop()
        size=len(nums)
        if size==0:
            return []
        nums.sort()
        used=[[False]*len(nums)]
        res=[]
        dfs(nums,size,0,[],used,res)
        return res

#用hashmap代替list判断重复。
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        record=dict()
        def dfs(tmp,nums):
            if not nums:
                if record.get(tuple(tmp),0) == 0:
                    res.append(tmp)
                    record[tuple(tmp)]=1
            for i,x in enumerate(nums):
                dfs(tmp+[x],nums[:i]+nums[i+1:])
        dfs([],nums)
        return res

# 在循环里去重
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        record=dict()
        def dfs(tmp,nums):
            if not nums:
                res.append(tmp)
            for i,x in enumerate(nums):
                if i==0 or nums[i]!=nums[i-1]:
                    dfs(tmp+[x],nums[:i]+nums[i+1:])
        dfs([],nums)
        return res

48. 旋转图像
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #先转置再左右对称翻转
        if not matrix or not matrix[0]:
            return matrix
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        fro row in matrix:
        for i in range(n//2):
            row[i],row[n-1-i]=row[n-1-i],row[i]
        return matrix

49. 字母异位词分组
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap=dict()
        for s in strs:
            t="".join(sorted(s))
            if t in hashmap:
                hashmap[t].append(s)
            else:
                hashmap[t]=[s]
        return hashmap.values()

#下面是丑陋的修改前版本
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap=dict()
        for s in strs:
            t=str(sorted(s))
            if t in hashmap.keys():
                hashmap[t]=" "+s
            else:
                hashmap[t]=s
        res=[]
        for key in hashmap.keys():
            res.append([s for s in hashmap[key].split(" ")])
        return res

#以下是2019/6/13写的： 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        record=dict()
        for word in strs:
            tmp=tuple(sorted(word))
            if tmp in record:
                record[tmp].append(word)
            else:
                record[tmp]=[word]
        return [val for key,val in record.items()]

50. Pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        i=abs(n)
        res=1.0
        while i!=0:
            if i%2:
                res*=x
            x*=x
            i/=2
        return res if n>0 else 1/res

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        def helper(x,n,tmp):
            if n<=1:
                return x*tmp
            if n%2:
                tmp*=x
                n-=1
            return helper(x*x,n//2,tmp)
        res=helper(x,abs(n),1)
        return res if n>0 else 1.0/res

51. N皇后
class Solution:
    def solveNQueens(self,n:int)->List[List[str]]:
        def could_palce(row,col):
            return not(cols[col]+hill_diagonals[row-col]+dale_diagonals[row+col])
        def place_queen(row,col):
            queens.add((row,col))
            cols[col]=1
            hill_diagonals[row-col]=1
            dale_diagonals[row+col]=1
        def remve_queen(row,col):
            queens.remove((row,col))
            cols[col]=0
            hill_diagonals[row-col]=0
            dale_diagonals[row+col]=0
        def add_solution():
            solution=[]
            for _,col in sorted(queens):
                solution.append('.'*col+'Q'+'.'*(n-col-1))
            output.append(solution)
        def backtrack(row=0):
            for col in range(n):
                if could_palce(row,col):
                    place_queen(row,col)
                    if row+=1 == n:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row,col)
        cols=[0]*n
        hill_diagonals=[0]*(2*n-1)
        dale_diagonals=[0]*(2*n-1)
        queens=set()
        output=[]
        backtrack()
        return output

52. N皇后 II
class Solution:
    def totalNQueens(self,n:int)->int:
        def could_place(row,col):
            return not (cols[col]+hill_diagonals[row-col]+dale_diagonals[row+col])
        def place_queen(row,col):
            queens.add((row,col))
            cols[col]=1
            hill_diagonals[row-col]=1
            dale_diagonals[row+col]=1
        def remove_queen(row,col):
            queens.remove((row,col))
            cols[col]=0
            hill_diagonals[row-col]=0
            dale_diagonals[row+col]=0
        def backtrack(row==0):
            for col in range(n):
                if count_place(row,col):
                    place_queen(row,col)
                    if row+1=n:
                        self.ans+=1
                    else:
                        backtrack(row+1)
                    remove_queen(row,col)
        cols=[0]*n
        hill_diagonals=[0]*(2*n-1)
        dale_diagonals=[0]*(2*n-1)
        queens=set()
        self.ans=0
        backtrack()
        return self.ans

53. 最大子序和
class Solution:
    def maxSubArray(self,nums:List[int])->int:
        if nums is None:
            return 0
        sum = 0
        max=float("-inf")
        for i in range(len(nums)):
            sum += nums[i]
            if sum <= nums[i]:
                sum = nums[i]
            if max<sum:
                max=sum
        return max







































