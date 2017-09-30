# Hamming-Code

Write a Program in C/ C++ for hamming code generation for error detection/correction

Hamming code uses redundant bits (extra bits) which are calculated according to the below formula:-

    2^r ≥ m+r+1

Where r is the number of redundant bits required and m is the number of data bits.
    R is calculated by putting r = 1, 2, 3 … until the above equation becomes true.
    R1 bit is appended at position 20
    R2 bit is appended at position 21
    R3 bit is appended at position 22 and so on.
    
These redundant bits are then added to the original data for the calculation of error at receiver’s end.

At receiver’s end with the help of even parity (generally) the erroneous bit position is identified and since data is in binary we take complement of the erroneous bit position to correct received data.

Respective index parity is calculated for r1, r2, r3, r4 and so on.

Advantages of Hamming Code

    1]Easy to encode and decode data at both sender and receiver end.
    2]Easy to implement.

Disadvantages of Hamming Code

    1]Cannot correct burst errors.
    2]Redundant bits are also sent with the data therefore it requires more bandwidth to send the data.
