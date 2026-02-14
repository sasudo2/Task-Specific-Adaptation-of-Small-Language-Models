def min_moves(H, W, A_iborders):
    grid = [[0] * W for _ in range(H)]
    
    for i in range(H):
        for j in range(W):
            if i + 1 < H and grid[i + 1][j] > 0:
                grid[i][j] = min(grid[i][j], grid[i + 1][j])
            if j + 1 < W and grid[i][j] > 0:
                grid[i][j] = min(grid[i][j], grid[i][j + 1])
                
    for i in range(1, H):
        for j in range(1, W):
            if grid[i][j] > 0:
                grid[i][j] -= 1
                
    for k in range(1, H):
        for j in range(1, W):
            if grid[k][j] > 0:
                print(-1)
                return
        for i in range(k, H):
            j = (k - i) % W
            grid[i][j] = min(grid[i][j], grid[i][j + 1])
            
    print(0)

def main():
    (H, W) = map(int, input().split())
    A_iborders = [list(map(int, input().split())) for _ in range(H)]
    min_moves(H, W, A_iborders)

main()