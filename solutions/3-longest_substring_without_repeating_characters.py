def lengthOfLongestSubstring(s):
    start = max_length = 0
    used_char = {}   #dictionary to store repeating characters

    for i in range(len(s)):
        if s[i] in used_char and start <= used_char[s[i]]:
            start = used_char[s[i]] + 1   #move the start pointer one step ahead of repeated character
        else:
            max_length = max(max_length, i - start + 1)  #calculate maximum length of substring

        used_char[s[i]] = i   #store index of character
    return max_length  #return length of longest substring without repeated characters
