wl_count = int(input())
white_list = []
for i in range(wl_count):
    white_list.append(input())

request_count = int(input())
requests = []
for i in range(request_count):
    requests.append(input())

for req in requests:
    if white_list.__contains__(req):
        print(req)
