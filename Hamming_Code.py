def HammingDataWord(DataWord):
    print("DataWord = ", DataWord)

    r1 = DataWord[0] ^ DataWord[2] ^ DataWord[3]
    r2 = DataWord[0] ^ DataWord[1] ^ DataWord[3]
    r4 = DataWord[0] ^ DataWord[1] ^ DataWord[2]

    DataWord.insert(3, r4)
    DataWord.insert(5, r2)
    DataWord.insert(6, r1)

    return DataWord

def CheckDataWord(RecDataWord):
    print("Received DataWord = ", RecDataWord)

    p1 = RecDataWord[6] ^ RecDataWord[4] ^ RecDataWord[2] ^ RecDataWord[0]
    p2 = RecDataWord[5] ^ RecDataWord[4] ^ RecDataWord[1] ^ RecDataWord[0]
    p3 = RecDataWord[3] ^ RecDataWord[2] ^ RecDataWord[1] ^ RecDataWord[0]

    z = p3 * 4 + p2 * 2 + p1

    return z

DataWord = list(input("Enter the 4 bit DataWord"))
DataWord = [int(i) for i in DataWord]

HammingDataWord = HammingDataWord(DataWord)

print("Hamming/Encoded DataWord = ", HammingDataWord)

RecDataWord = list(input("Enter the Received DataWord"))
RecDataWord = [int(i) for i in RecDataWord]

z = CheckDataWord(RecDataWord)

if (z == 0):
    print("No Error in Transmission")
else:
    print("Error on Position ",8 - z)

    print("Sent DataWord = ",DataWord)
    print("Received DataWord = ", RecDataWord)

    RecDataWord[7 - z] = int(not RecDataWord[7 - z])
    print("Corrected Received Data Word = ", RecDataWord)
