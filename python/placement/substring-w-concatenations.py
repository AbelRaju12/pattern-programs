from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = Counter(words)
    result = []

    for i in range(word_len):
        left, right = i, i
        current_count = Counter()

        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len
            current_count[word] += 1

            while current_count[word] > word_count[word]:
                left_word = s[left:left + word_len]
                left += word_len
                current_count[left_word] -= 1

            if right - left == total_len:
                result.append(left)

    return result

# Example usage:
s = "barfoothefoobarman"
words = ["foo","the","foo", "bar"]
indices = findSubstring(s, words)
print("Starting Indices:", indices)