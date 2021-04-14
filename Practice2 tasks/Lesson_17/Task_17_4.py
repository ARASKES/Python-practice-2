N = int(input())
posts = []
for i in range(N):
    post_info = input().split(" ")
    posts.append(post_info)

for i in range(N):
    actual_info = [posts[i][0]]
    if i != 0:
        actual_info.append(posts[i][4][0: -1:])
    actual_info.append(int(posts[i][-1]))
    posts[i] = actual_info

for i in range(N - 1, 0, -1):
    for j in range(0, i):
        if posts[j][0] == posts[i][1]:
            posts[j][-1] += posts[i][2]

for post in posts:
    print(post[-1])
