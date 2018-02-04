# Program that handles IP addresses.
# Just count number of length of segments

ip = "127.0.0.1"
ip2 = ".196.168.0.1"

numBlocks = 0
blockLength = 0
blockLengths = []

for char in ip:
    if char == ".":
        if blockLength == 0:
            continue
        numBlocks += 1
        blockLengths.append(blockLength)
        blockLength = 0
        continue
    blockLength += 1

# could aternatively append a . to the input string
if blockLength > 0:
    numBlocks += 1
    blockLengths.append(blockLength)

print(numBlocks)
print(blockLengths)
