from collections import deque

# Initialize an empty queue
queue = deque()

# Enqueue customers
customers = ["Alice", "Bob", "Carol"]
for name in customers:
    print(f"Arriving: {name}")
    queue.append(name)

# Dequeue customers as they are served
while queue:
    current = queue.popleft()
    print(f"Serving: {current}")

print("All customers served.")
