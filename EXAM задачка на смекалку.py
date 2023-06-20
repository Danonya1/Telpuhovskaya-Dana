def longest(s1, s2):
    combined_list = list(s1 + s2)
    unique_chars = sorted(list(set(combined_list)))
    return ''.join(unique_chars)
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
sorted_str = longest(a, b)
print(sorted_str)
