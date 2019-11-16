def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split(' ')
    words.reverse()
    for j in range(len(words)-1, -1, -1):
        if words[j] == "":
            words.remove(words[j])
    print(words)
    re = ""
    for i in range(len(words)-1):
        re += words[i]
        re += " "
    re += words[len(words) - 1]
    return re

print(reverseWords("  hello world!  "))