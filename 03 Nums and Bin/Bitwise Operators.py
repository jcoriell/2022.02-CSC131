
# Bitwise operators

#####
# &         bitwise AND (compares bit by bit)    ex: 1 & 0  yields 0
12 & 3   # 0b1100 AND 0b0011 give 0b0000 

#####
# | (pipe)  bitwise OR  (compares bit by bit)    ex: 1 | 0 yields 1
12 | 3   # 0b1100 OR 0b0011 gives 0b1111 (15 in base 10)

#####
# ^ (caret) XOR         (compares bit by bit)    ex: 1 ^ 1 yields 0
12 | 3   # 0b1100  XOR 0b0011 gives 0b1111


#####
# ~         bitwise NOT     
# reverses each bit (to explain python's output, see two's complement. will discuss in csc132)
# 1111 -> 0000
# 1010 -> 0101


#####
# <<        left shift      ex: 45 << 2 
12 << 2     # shifts 0b1100 to the left 2 places to give 0b110000

#####
# >>        right shift     ex: 45 >> 2
12 >> 2     # shifts 0b1100 to the right two places to give 0b11 