class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        Each string is stored as: <length>#<string>

        Example:
            ["leet", "code"] → "4#leet4#code"
        """
        encoded_string = ''
        for word in strs:
            # Append length of the word + '#' delimiter + the word itself
            encoded_string += str(len(word)) + '#' + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back into a list of strings.

        Example:
            "4#leet4#code" → ["leet", "code"]
        """
        decoded_strings = []
        start = 0

        # Iterate through the encoded string
        while start < len(s):
            # Find where the next '#' delimiter is (marks end of length)
            word_len_index = start
            while s[word_len_index] != '#':
                word_len_index += 1

            # Extract the length of the next word
            length_of_word = int(s[start:word_len_index])

            # Extract the word itself using the length
            decoded_strings.append(s[word_len_index + 1 : word_len_index + 1 + length_of_word])

            # Move start pointer to next encoded word
            start = word_len_index + 1 + length_of_word

        return decoded_strings
    #TC - O(N)
    #SC - O(N)