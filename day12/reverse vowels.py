class Solution(object):
    def reverseVowels(self, s):
        vowels = set({"a", "e", "i", "o","u","A","E","I","O","U"})
        s = list(s)
        i,j = 0, (len(s) - 1)
        while i<j:
            if s[i] not in vowels and s[j] not in vowels:
                i = i + 1
                j = j - 1
            elif s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1
            elif s[i] in vowels and s[j] not in vowels:
                j = j - 1
            else:
                i = i + 1
        return ''.join(s)

if __name__=='__main__':
    s='duke daffin'
    ob1=Solution()
    print(s)
    print(ob1.reverseVowels(s))