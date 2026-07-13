

text = input()
fist_second_index = []
start_index = 0

for i in text:
    if i == "f":
        fist_second_index.append(start_index) # type: ignore
    start_index += 1
if len(fist_second_index) == 0: # type: ignore
    print("NO")
elif len(fist_second_index) == 1: # type: ignore
    print(*fist_second_index) # type: ignore
else:
    print(fist_second_index[0], fist_second_index[-1]) # type: ignore
