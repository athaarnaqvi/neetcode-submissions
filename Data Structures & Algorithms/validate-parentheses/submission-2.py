class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            if bracket in ")}]" and len(stack)==0:
                return False
            elif bracket == ")" and len(stack)>0:
                c = stack.pop()
                if ord(c) == 40:
                    continue
                else:
                    return False
            elif bracket == "]" and len(stack)>0:
                c = stack.pop()
                if ord(c) == 91:
                    continue
                else:
                    return False
            elif bracket == "}" and len(stack)>0:
                c = stack.pop()
                if ord(c) == 123:
                    continue
                else:
                    return False
        
        return len(stack) == 0
                        