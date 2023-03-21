def palindrome(s):
    if (len(s) == 0):
        return False
    
    for i in range(len(s) // 2):
        if(s[i] != s[(len(s) - 1) - i]):
            return False
    return True

# print(palindrome("abba"))
# print(palindrome("ciao!"))
# print(palindrome("subbus"))
# print(palindrome("aaaaaaaaaaaaaaaaaaaaaaafgaaaaaaaaaaaaaaaaaaaa"))
# print(palindrome("cavac"))
# print(palindrome("aaafdaaa"))

def lps(s):
    size = 0
    result = ""
    for i in range(len(s)):
        tempString = s[i : len(s)]
        for j in range(1, len(tempString) + 1):
            tempTempString = tempString[0 : j]
            if(palindrome(tempTempString) and j > size):
                result = tempTempString
                size = j
    return result if size != 1 and size != 0 else None

# print(lps("babad"))
# print(lps("cbbd"))
# print(lps("racecar"))