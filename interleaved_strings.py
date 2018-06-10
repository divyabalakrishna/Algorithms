def is_interleaved(str1, str2, result):
    if len(str1) + len(str2) != len(result):
        return False

    for c in str1:
        if c not in result:
            return False

    for c in str2:
        if c not in result:
            return False

    temp = []
    for c1 in str1:
        index = result.rfind(c1)
        temp.append(index)
        result = result[:index] + result[index+1:]
        if sorted(temp) != temp:
            return False

    temp = []
    for c1 in str2:
        index = result.rfind(c1)
        temp.append(index)
        result = result[:index] + result[index+1:]
        if sorted(temp) != temp:
            return False

    return True

ans = is_interleaved('abc', 'def', 'abcdef')
print(ans)

ans = is_interleaved('', '', 'abcdef')
print(ans)

ans = is_interleaved('', '', '')
print(ans)

ans = is_interleaved('abc', 'def', 'bacdef')
print(ans)

ans = is_interleaved('xy', 'yx', 'yxxy')
print(ans)
