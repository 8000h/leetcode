def longest_palindromic_substring(s):
    # Starting by assuming that no palindromic substring has been found yet
    start = 0
    end = 0
    # Loop over the string.
    for i in range(len(s)):
        # Checking for odd length palindromes
        len1 = expand(s, i, i)
        # Checking for even length palindromes
        len2 = expand(s, i, i+1)
        # Finding the maximum length palindrome.
        len_ = max(len1, len2)
        # If the found palindrome is greater than the previous palindrome
        if len_ > end - start:
            # Updating the start and end points of the palindrome
            start = i - (len_ - 1) // 2
            end = i + len_ // 2
    # Returning the longest palindromic substring
    return s[start:end+1]
        
def expand(s, left, right):
    # this function finds the length of the palindrome having left and right as the centers
    # Expand as long as 'left' and 'right' expandable.
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # returning length of found palindrome
    return right - left - 1