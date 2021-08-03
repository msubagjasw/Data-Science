height = 0
blocks = int(input("Enter the number of blocks: "))
while height < blocks :
    height +=1
    #print(height)
    blocks -= height
    #print(blocks)

print("The height of the pyramid:", height)
