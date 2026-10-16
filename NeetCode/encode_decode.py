# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }
# So Machine 1 does:

# String encoded_string = encode(strs);
# and Machine 2 does:

# List<String> decoded_strs = decode(encoded_string);
# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: strs = ["Hello","World"]

# Output: ["Hello","World"]
# Explanation:

# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

# // Machine 1 ---encoded_string---> Machine 2

# List<String> decoded_strs = solution.decode(encoded_string);

# Example 2:

# Input: strs = [""]

# Output: [""]

# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.


from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}-{s}"
        return res

    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        for i, c in enumerate(s):
            if c == "-":
                num_str = s[start: i]
                try:
                    n_num_str = int(num_str)
                    res.append(s[i + 1: i + 1 + n_num_str])
                    start = i + 1 + int(n_num_str)
                except ValueError:
                    continue
        return res

s = Solution()
strs = ["Hello","World"]
str_encoded = s.encode(strs)
print(str_encoded)
str_decoded = s.decode(str_encoded)
print(str_decoded)