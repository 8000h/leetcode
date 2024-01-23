def find_needle(haystack, needle):
    # Cheking if needle is in haystack
    if needle in haystack:
        # returning index of needle in haystack
        return haystack.index(needle)
    else:
        # returning -1 becuz needle not in haystack
        return -1