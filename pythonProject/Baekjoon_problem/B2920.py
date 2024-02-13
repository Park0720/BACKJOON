music_list = list(map(int, input().split()))

sorted_list = sorted(music_list)

sorted_reverse_list = sorted_list[::-1]

if music_list == sorted_list:
    print('ascending')
elif music_list == sorted_reverse_list:
    print('descending')
else:
    print('mixed')