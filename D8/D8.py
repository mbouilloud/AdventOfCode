import fileinput

def compute_score(area, i, j, M, N):
    v = area[i][j]
    s_up = 0
    s_right = 0
    s_left = 0
    s_down = 0

    if(i > 0):
        for m in range(i-1, -1, -1):
            s_up += 1

            if area[m][j] >= v:
                break
        
    if(i < M-1):
        for m in range(i+1, M):
            s_down += 1

            if area[m][j] >= v:
                break
        

    if(j > 0):
        for m in range(j-1, -1, -1):
            s_left += 1

            if area[i][m] >= v:
                break

    if(j < N - 1):
        for m in range(j+1, N):
            s_right += 1

            if area[i][m] >= v:
                break

    return s_up*s_down*s_left*s_right

area = []
for f in fileinput.input():
    if(f[-1:] == "\n"):
        line = f[:-1]
    else:
        line = f

    l = []
    for c in line:
        # l.append((int(c), False))
        l.append(int(c))

    area.append(l)

# print(len(area))
# print(area)
N = len(area[0])
M = len(area)

m = 0
for i in range(M):
    for j in range(N):
        v = compute_score(area, i, j, N, M)
        if(v > m):
            m = v
print(m)

# print(compute_score(area, 3, 2, N, M))

# for line in area[1:N-1]:

#     m = line[0][0]
#     for i in range(1, N - 1):
#         (e, b) = line[i]
#         if(e > m):
#             m = e
#             if(not b):
#                 visible += 1
#                 line[i] = (e, True)
    
#     m = line[N-1][0]
#     for i in range(N-2, 0, -1):
#         (e, b) = line[i]
#         if(e > m):
#             m = e
#             if(not b):
#                 visible += 1
#                 line[i] = (e, True)

# for j in range(1, N-1):

#     m = area[0][j][0]

#     for i in range(1, N - 1):
#         (e, b) = area[i][j]
#         if(e > m):
#             m = e
#             if(not b):
#                 visible += 1
#                 area[i][j] = (e, True)
#                 m = e
    
#     m = area[N - 1][j][0]

#     for i in range(N-2, 0, -1):
#         (e, b) = area[i][j]
#         if(e > m):
#             m = e
#             if(not b):
#                 visible += 1
#                 area[i][j] = (e, True)
#                 m = e
# print(visible)

