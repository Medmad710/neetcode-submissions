class Solution:
    def isValid(self, s: str) -> bool:



        stack = []
        for i in s:
            if stack ==[] and i in "}])":
                return False
            if i in "{[(":
                stack.append(i)
            if i == "}" and stack!=[]:
                if stack.pop() != "{":
                    return False
            if i == ")" and stack!=[]:
                if stack.pop() != '(':
                    return False
            if i == "]" and stack!=[]:
                if stack.pop() != '[':
                    return False
        if stack == []:
            return True
        else :
            return False