class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        Each string is stored as: <length>#<string>

        Example:
            ["leet", "code"] → "4#leet4#code"
        """
        encoded_string =''
        for word in strs:
            encoded_string += str(len(word))+'#'+word

        return encoded_string       

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back into a list of strings.

        Example:
            "4#leet4#code" → ["leet", "code"]
        """
        decoded_strings = []
        start = 0
        while start < len(s):
            word_len_index = start
            while s[word_len_index] != '#':
                word_len_index += 1
            len_of_word = int(s[start:word_len_index])
            decoded_strings.append(s[word_len_index+1:word_len_index+1+len_of_word])
            start = word_len_index+len_of_word+1
        return decoded_strings
    #TC - O(N)
    #SC - O(N)