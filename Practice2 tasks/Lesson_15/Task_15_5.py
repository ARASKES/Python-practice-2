def find_index(collection, element):
    index = 0
    for k in range(len(collection)):
        if collection[k] == element:
            index = k
            break

    return index


def enqueue_after(queue, element, prev_element):
    prev_index = find_index(queue, prev_element)
    last_part = queue[prev_index + 1: len(queue):]
    queue = queue[0: prev_index + 1:]
    queue.append(element)
    queue += last_part

    return queue


def dequeue(queue, element):
    index = find_index(queue, element)
    queue = queue[0: index:] + queue[index + 1: len(queue):]

    return queue


N = int(input())
events = []
for i in range(N):
    events.append(input())

names = []
for event in events:
    name = ""
    penultimate_symbol = event[len(event) - 2]
    if penultimate_symbol == "ь":
        for i in range(len(event)):
            if (i == len(event) - 18 or i == len(event) - 17) and event[i] == " ":
                break
            else:
                name += event[i]
        names.append(name)
    elif penultimate_symbol == "й":
        exclamation_index = event.find("!")
        prev_name = ""
        for i in range(len(event)):
            if 7 < i < exclamation_index:
                prev_name += event[i]
            elif exclamation_index + 1 < i < len(event) - 16:
                name += event[i]
        names = enqueue_after(names, name, prev_name)
    elif penultimate_symbol == "а":
        for i in range(len(event)):
            if i == len(event) - 34:
                break
            else:
                name += event[i]
        names = dequeue(names, name)

for name in names:
    print(name)
