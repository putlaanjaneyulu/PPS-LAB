n = int(input())

responses = []

for i in range(n):
    q_id, correct, chosen = input().split()
    responses.append((q_id, correct, chosen))

score = 0
correct_count = 0

for response in responses:
    if response[1] == response[2]:
        score += 4
        correct_count += 1


accuracy = (correct_count/n) * 100
print(f"Total Score: {score}")
print(f"Accuracy: {round(accuracy, 2)}%")

    
