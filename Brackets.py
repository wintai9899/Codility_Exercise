def solution(S):
    hashmap = {
        "]" : "[",
        "}" : "{",
        ")" : "("
    }
    stack = []

    for c in S:
        if c in hashmap:
            if stack and stack[-1] == hashmap[c]:
                stack.pop()

            else:
                return 0

        else:
            stack.append(c)

    return 1 if not stack else 0