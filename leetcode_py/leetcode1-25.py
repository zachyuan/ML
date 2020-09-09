1.两数之和
#第一种思路：
#双重循环暴力解
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        for index,item in enumerate(nums):
            for count in range(index+1，len(nums)):
                if item + nums[count] == target:
                    return [index,count]

#第二种思路：
#用hashmap记录之前出现的数字及下标，key是数字，val是下标。
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for index,item in enumerate(nums):
            if hashmap.has_key(target-item):
                return hashmap[target-item],index
            hashmap[item]=index

2.两数相加
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.getLength(l1) < self.getLength(l2):
            l1,l2=l2,l1
        head = l1
        while(l2):
            l1.val += l2.val
            l1=l1.next
            l2=l2.next
        p=head
        while(p):
            if p.val>9:
                p.val -= 10
                if p.next:
                    p.next.val += 1
                else:
                    p.next=ListNode(1)
            p=p.next
        return head
    def getLength(self,l):
        length=0
        while(l):
            length+=1
            l=l.next
        return length

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length1,length2=0,0
        p=l1
        while p:
            length1 += 1
            p=p.next
        p=l2
        while p:
            length2 += 1
            p=p.next
        if length1 < length2:
            l1,l2=l2,l1
        p1,p2=l1,l2
        c=0
        while p2:
            p1.val += p2.val
            p1=p1.next
            p2=p2.next
        p1=l1
        while p1:
            p1.val += c
            c = 0
            if p.val > 9:
                p1.val -= 10
                c = 1
            if not p1.next and c:
                p1.next = ListNode(1)
                break
            p1=p1.next
        return l1

3. 无重复字符的最长子串
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()
        for end in range(len(s)):
            if s[end] in record:
                start=max(start,record[s[end]]+1)
            record[s[end]] = end
            res=max(res,end-start+1)
        return res

4.寻找两个有序数组的中位数
from heapq import *
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_h = list()
        self.min_h = list()
        heapify(self.max_h)
        heapify(self.min_h)
    def addNum(self,num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.min_h,num)
        heappush(self.max_h,-heappop(self.min_h))
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h,-heappop(self.max_h))
    def findMedian(self):
        """
        :rtype: float
        """
        max_len=len(self.max_h)
        min_len=len(self.min_h)
        if max_h==min_len:
            return (self.min_h[0] + -self.max_h[0])/2.
        else:
            return self.min_h[0]/1.
class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mf=MedianFinder()
        for num in nums:
            mf.addNum(num)
        for num in nums:
            mf.addNum(num)
        return mf.findMedian()

5.最长回文子串,
#第一种思路：第一种思路太慢了
class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        max_l=0
        res=""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                substring=s[i:j+1]
                if substring == substring[::-1]:
                    if max_l < j+1-i:
                        max_l = j+1-i
                        res=substring
        return res

class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        max_l=0
        res=""
        for i in range(0,len(s)):
            left,right = i,i
            while(left >=0 and right<len(s) and s[left]==s[right]):
                if max_l < right-left+1:
                    max_l=right-left+1
                    res=s[left:right+1]
                left-=1
                right+=1

            left,right=i,i+1
            while(left>=0 and right<len(s) and s[left] == s[right]):
                if max_l < right-left+1:
                    max_l=right-left+1
                    res=s[left:right+1]
                left -=1
                right+=1
        return res

6. Z 字形变换
class Solution(object):
    def convert(self,s,n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if n<=1:
            return s
        l=len(s)
        record=[[0]*l for _ in range(n)]
        x,y=0,0
        state="down"
        for i,char in enumerate(s):
            record[x][y] = char
            if state == "down":
                if x!=n-1:
                    x+=1
                else:
                    state="up"
                    x-=1
                    y+=1
                continue
            elif state=="up":
                if x!=0:
                    x-=1
                    y+=1
                else:
                state = "down"
                x+=1
        res = ""
        for row in record:
            for char in row:
                if char!=0:
                    res+=char
        return res

class Solution(object):
    def convert(self,s,n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if n<=1:
            return s
        l=len(s)
        res=""
        for i in range(n):
            tmp,index = "",i
            if i in [0,n-1]:
                while(index<l):
                    tmp+=s[index]
                    index += 2*(n-1)
            else:
                state="down"
                while (index<l):
                    tmp+=s[index]
                    if state=="down":
                        state = "up"
                        index+=2*(n-1-i)
                    else:
                        state = "down"
                        index += 2*i
            res += tmp
        return res

class Solution(object):
    def convert(self,s,n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #第一行和最后一行都是相差 2 * (n - 1)
        #对于直角在上面的直角三角形， 相差 2 * (n - 1 - i)
        #对于直角在下面的直角三角形， 相差 2 * i
        if not s:
            return s
        res = ""
        for idx in range(n):
            res += s[idx]

            if idx in [0,n-1]:
                tmp = idx+2*(n-1)
                while (tmp<len(s)):
                    res += s[tmp]
                    tmp += 2(n-1)
            else:
                tmp=idx+2(n-1-idx)
                tri="down"
                while (tmp<len(s)):
                    res += s[tmp]
                    if tri == "up":
                        tmp += 2*(n-1-idx)
                        tri="down"
                    else:
                        tmp+=2*idx
                        tri="up"
        return res

7. 整数反转
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=0
        if x<0:
            flag = 1
        if flag:
            s=str(x)[1:]
            s=s[::-1]
            x=-*int(s)
        else:
            s=str(x)
            s=s[::-1]
            x=int(x)
        if x<-1*2**31 or x>2**31-1:
            return 0
        return x

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN=-2**31
        INT_MAX=2**31-1
        op=1
        if x<0:
            op=-1
            s=str(x)[1:]
        else:
            s=str(x)
        res=op*int(x[::-1])
        return res if INT_MIN<=res<=INT_MAX else 0

8. 字符串转换整数 (atoi)
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s=s.strip(" ")
        if not len(s):
            return 0
        if s[0] not in ["+","-"] and not s[0].isdigit():
            return 0
        op=1
        res=""
        for i,char in enumerate(s):
            if i == 0:
                if char == "-":
                    op=-1
                    continue
                elif char == "+":
                    continue
            if char == " " or not char.isdigit():
                break
            res += char
        if len(res) > 0:
            res = op*int(res)
        else:
            return 0
        INT_MIN=-2**31
        INT_MAX=2**31-1
        if res>INT_MAX:
            return INT_MAX
        elif:
            return INT_MIN
        return res

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s=s.strip(" ")
        if not s or (s[0] not in ["+","-"] and not s[0].isdigit()):
            return 0
        op=1
        tmp=""
        for i,char in enumerate(s):
            if i==0:
                if char == "-":
                    op=-1
                    continue
                elif char == "+":
                    pass
                    continue
            if char.isdigit():
                tmp+=char
            else:
                break
        if tmp:
            res = op*int(tmp)
        else:
            res = 0
        INT_MIN=-2**31
        INT_MAX=2**31-1
        if res>INT_MAX:
            return INT_MAX
        elif:
            return INT_MIN
        return res

9. 回文数
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xx=x
        if x<0:
            return False
        reverse=0
        while x>0:
            x,tmp=divmod(x,10)
            reverse=reverse*10+tmp
        return reverse == xx

10.正则表达式匹配
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        match=s and p[0] in [s[0],'.']
        if len(p)>1 and p[1] == "*":
            return self.isMatch(s,p[2:]) or (match and self.isMatch(s[1:],p))
        return match and self.isMatch(s[1:],p[1:])

11. 盛最多水的容器
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo,hi=0,len(height)-1
        res=0
        while (lo<hi):
            if height[lo] > height[hi]:
                area=height[hi]*(hi-lo)
                hi-=1
            else:
                area=height[lo]*(hi-lo)
                lo+=1
            res=max(area,res)
        return res

12.整数转罗马数字
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        mapping = {1000:"M", 900:"CM", 500:"D",400:"CD", 100:"C", 90: "XC", 50:"L",40: "XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        res = ""
        for i in digit:
            res += (num/i)*mapping[i]
            num-=i*(num/i)
            if num==0
        return res

13.罗马数字转整数
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V":5, "X": 10, "L":50, "C":100, "D": 500, "M": 1000}
        stack = []
        res = 0
        for inx,item in enumerate(s):
            res += dic[item]
            if item == "V" or item == "X":
                if stack and stack[-1] == "I":
                    res -= 2
            elif item == "L" or item == "C":
                if stack and stack[-1] == "X":
                    res -= 20
            elif item == "D" or item == "M":
                if stack and stack[-1] == "C":
                    res -= 200
        return res

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        ans=0
        for i in range(len(s)):
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans

14.最长公共前缀
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return os.path.commonprefix(strs)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_l=len(strs[0])
        for word in strs:
            min_l = min(min_l,len(word))
        common=strs[0][:min_l]

        for index,item in enumerate(strs):
            i=0
            while (i<min_l and item[i]==common[i]):
                i+=1
            min_l=min(min_l,i)
            common=common[:min_l]
        return common

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        mins=min(strs)
        maxs=max(strs)

        for index,item in enumerate(mins):
            if maxs[index] != mins[index]:
                return mins[:index]

        return mins

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()
        res = ""

        for x,y in zip(strs[0],strs[-1]):
            if x==y:
                res += x
            else:
                break

        return res

15. 三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #固定a,用双指针在排序数组里找两数之和为-a
        nums.sort()
        l=len(nums)
        res=[]
        for i,a in enumerate(nums):
            if i==0 or nums[i]>nums[i-1]:
                left,right = i+1,len(nums)-1
                while (left<right):
                    s=a+nums[left]+nums[right]
                    if s==0:
                        tmp = [a,nums[left],nums[right]]
                        res.append(tmp)
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while right>left and nums[right]==nums[right+1]:
                            right-=1
                    elif s<0:
                        left+=1
                    elif s>0:
                        right-=1
        return res

16.最接近的三数之和
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i,num in enumerate(nums):
            left,right = i+1,len(nums)-1
            while left<right:
                s=num+nums[left]+nums[right]
                if abs(s-target) < abs(res-target):
                    res=s
                if s==target:
                    return s
                elif s<target:
                    left+=1
                else:
                    right-=1
        return res

17.电话号码的字母组合
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res=[]
        for digit in digits:
            temp=[]
            n=int(digit)
            for char in mapping[n]:
                if not res:
                    temp.append(char)
                else:
                    for item in res:
                        temp.append(item+char)
            res=temp
        return res

18. 四数之和
class Solution(object):
    def fourSum(self, n, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res=[]
        n.sort()
        # print n
        def threeSum(nums,t, d):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            #固定a,用双指针在排序数组里找两数之和为-a
            l=len(nums)
            res=[]
            for i,a in enumerate(nums):
                if i==0 or nums[i]>nums[i-1]:
                    left,right=i+1,len(nums)-1
                    while left<right:
                        s=a+nums[left]+nums[right]
                        if s==t:
                            tmp=[d,a,nums[left],nums[right]]
                            self.res.append(tmp)
                            left+=1
                            right-=1
                            while left<right and nums[left]==nums[left-1]:
                                left+=1
                            while right>left and nums[right]==nums[right+1]:
                                right-=1
                        elif s<t:
                            left+=1
                        elif s>t:
                            right+=1

        for i in range(len(n)-3):
            if i==0 or n[i]>n[i-1]:
                threeSum(n[i+1:],target-n[i],n[i])
        return self.res

19.删除链表的倒数第N个节点
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p=head
        slow,fast=p,p
        while n:
            n-=1
            fast=fast.next
        if fast is None:
            return p.next
        while (fast and fast.next):
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return p

20. 有效的括号
class Solution(object):
    def isValid(self, s):
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

21.合并两个有序链表
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead=ListNode(0)
        p=newhead
        while (l1 and l2):
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1=l1.next
            else:
                p.next=ListNode(l2.val)
                l2=l2.next
            p=p.next
        if l1:
            p.next=l1
        else:
            p.next=l2
        return newhead.next

22. 括号生成
class Solution(object):
    def generate(self, temp, left, right, result):
        if left==0 and right==0:
            result.append(temp)
            return
        if left>0:
            self.gernerate(temp+"(",left-1,right,result)
        if left<right:
            self.gernerate(temp+")",left,right-1,result)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        self.gernerate("",n,n,result)
        return result

23. 合并K个排序链表
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums=[]
        for i in range(len(lists)):
            while lists[i]:
                nums.append(lists[i].val)
                lists[i]=lists[i].next
        nums.sort()
        dummy=ListNode(1)
        p=dummy
        for i,num in enumerate(nums):
            p.next=ListNode(num)
            p=p.next
        return dummy.next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists)>1:
            a=lists.pop() if len(lists)>0 else None
            b=lists.pop() if len(lists)>0 else None
            lists.insert(0,self.mergeTwoLists(a,b))
        return None if len(lists)<1 else lists[0]
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead=ListNode(0)
        p=newhead
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1=l1.next
            else:
                p.next=ListNode(l2.val)
                l2=l2.next
            p=p.next
        if l1:
            p.next=l1
        else:
            p.next=l2
        return newhead.next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import *
        pq=[]
        for i in range(len(lists)):
            if lists[i]:
                heappush(pq,(lists[i].val,i))
                lists[i]=lists[i].next

        dummy=ListNode(1)
        p=dummy
        while pq:
            val,idx=heappop(pq)
            p.next=ListNode(val)
            p=p.next
            if lists[idx]:
                heappush(pq,(lists[idx].val,idx))
                lists[idx]=lists[idx].next
        return dummy.next

24. 两两交换链表中的节点
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node1,node2=head,head.next
        tmp=self.swapPairs(node2.next)
        node2.next=node1
        node1.next=tmp
        return node2

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        while pre.next and pre.next.next:
            node1,node2=pre.next,pre.next.next
            pre.next,node1.next=node2,node2.next
            node2.next=node1
            pre=node1
        return dummy.next

25. K 个一组翻转链表
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=ListNode(1)
        cnt=0
        p=head
        kthnode=None
        while (p):
            cnt+=1
            if cnt==k-1:
                kthnode=p.next
                break
            p=p.next
        if not kthnode:
            return head
        tail=kthnode.next
        kthnode.next=None
        dummy.next=self.reverseLL(head)
        head.next=self.reverseKGroup(tail,k)
        return dummy.next
    def reverseLL(self,head):
        if not head or not head.next:
            return head
        p=self.reverseLL(head.next)
        head.next.next=head
        head.next=None
        return p

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l=0
        p=head
        while p:
            l+=1
            if l==k:
                break
            p=p.next
        if l<k:
            return head
        tmp=self.reverseKGroup(p.next,k)
        p.next=None
        newhead=self.reverseLL(head)
        head.next=tmp
        return newhead
    def reverseLL(self,head):
        if not head or not head.next:
            return head
        p=self.reverseLL(head.next)
        head.next.next=head
        head.next=None
        return p

