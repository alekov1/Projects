class Solution(object):

    """Принятое решение

        Ссылка на задачу: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
        Мой профиль на LeetCode: https://leetcode.com/alekov1/
        Мой профиль на GitHub: https://github.com/alekov1

    """

    def __init__(self, s):
        self.s = s

    def countPalindromicSubsequence(self, s):

        counttext = 0
        for i in range(26):
            FirstLetter, LastLetter = s.find(chr(i + 97)), s.rfind(chr(i+97))
            if FirstLetter != -1 and LastLetter != -1:
                text = set(s[FirstLetter +1: LastLetter])
                counttext += len(text)
        return counttext



A = Solution('aabca')
print(A.countPalindromicSubsequence('aabca'))


class Solution(object):

    def countPalindromicSubsequence(self, s):

        """Не принятое решение
            Проходит только до 30 тестов

        """

        textstr = ''
        counttext = 0
        textspisok = []
        for letter1 in range(len(s)):
            for lettercenter in range(len(s)):
                if letter1 == lettercenter:
                    continue
                else:
                    for letter2 in range(len(s)):
                        if lettercenter == letter2 or lettercenter > letter2 or (s[letter1] + s[lettercenter] + s[letter2] in textspisok):
                            continue
                        else:
                            if letter1 == lettercenter == letter2:
                                continue
                            if (s[letter1] == s[letter2] and letter1 != letter2) and s.count(s[letter1]) > 1 and letter1 < lettercenter:
                                textstr += s[letter1] + s[lettercenter] + s[letter2]
                                counttext += 1
                                textspisok.append(textstr)
                                textstr = ''
        return counttext