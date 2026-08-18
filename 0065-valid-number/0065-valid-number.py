class Solution:
    def isNumber(self, s):
        d = e = dot = False

        for i, c in enumerate(s):
            if c.isdigit():
                d = True
                if e: dot = True
            elif c == '.':
                if dot or e: return False
                dot = True
            elif c in 'eE':
                if e or not d: return False
                e, d = True, False
            elif c in '+-':
                if i and s[i-1] not in 'eE': return False
            else:
                return False

        return d