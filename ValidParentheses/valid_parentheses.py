class Solution:
    def isValid(self, s: str) -> bool:
        start_parentheses = ["(", "{", "["]
        end_parentheses = [")", "}", "]"]
        p_stack = []
        ptr = 0
        if s[ptr] in start_parentheses:
            p_stack.add(s[ptr])
            ptr += 1
        else:
            if s[ptr] in end_parentheses:
                if s[ptr] == ")":
                    if p_stack[ptr] != ")":
                        return False
                if s[ptr] == "}":
                    if p_stack[ptr] != "}":
                        return False
                if s[ptr] == "]":
                    if p_stack[ptr] != "]":
                        return False
                ptr -= 1


solv = Solution()
s = "(){}[]"
print(solv.isValid(s))
