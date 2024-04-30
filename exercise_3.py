result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
element_count = {}

for char in result_link:
    if char in element_count:
        element_count[char] += 1
    else:
        element_count[char] = 1

print(element_count)