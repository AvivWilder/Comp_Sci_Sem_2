sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"



y = 0
q = 0

while True:
    x = sentence[y:y+5]
    if x == "whale":
        q = q + 1
    if y == len(sentence):
        break
    y = y + 1
    

print("There are " + str(q) + " whales in the sentence.")










#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
