class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

        arr = list(s)
        f, r = 0, len(s) - 1

        while f < r:
            if arr[f] in vowels and arr[r] in vowels:
                arr[f], arr[r] = arr[r], arr[f]
                f += 1
                r -= 1
                continue
            
            if arr[f] in vowels:
                r -= 1
            else:
                f += 1
        
        return ''.join(arr)
        