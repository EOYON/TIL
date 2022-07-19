T = int(input())

for i in range(1, T + 1):
    text = ""
    num_al = int(input())
    
    for j in range(num_al):
        al, num = input().split()
        text += al * int(num)
    
    print(f"#{i}")
    
    while len(text) > 10:
        print(text[:10])
        text = text[10:]
    
    print(text)