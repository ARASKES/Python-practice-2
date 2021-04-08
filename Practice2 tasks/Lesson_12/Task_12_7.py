N = int(input())
M = int(input())

image = []
for i in range(N):
    image.append(input())

compressed_image = []
for i in range(0, M, 2):
    line = ""
    for j in range(0, N, 2):
        line += image[i][j]
    compressed_image.append(line)

for line in compressed_image:
    print(line)
