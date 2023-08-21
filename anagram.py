class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for character in s:
            letters[character] = 1 if character not in letters.keys() else letters.get(character) + 1

        for character in t:
            times = letters.get(character)
            if times == None:
                return False
            if not times > 0:
                return False
            if times - 1 == 0:
                letters.pop(character)
            else:
                letters[character] = times - 1
        return True if len(letters) == 0 else False
