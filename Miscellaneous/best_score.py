#Use bubble sort to sort the given list and find the best score in the list 


score = [66,57,54,53,64,52,59]

size = len(score)-1

for i in range(size):
    for j in range(size):
        if score[j]>score[j+1]:
            (score[j+1],score[j]) = (score[j],score[j+1])

print(score[-1])
        