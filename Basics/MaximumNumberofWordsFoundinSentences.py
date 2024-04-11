class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for sentence in sentences:
            if(len(sentence.split(" "))>max):
                max = len(sentence.split(" "))
        return max