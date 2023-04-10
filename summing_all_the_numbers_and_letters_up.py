list = [1, 5, 8, ["a", 7, 10, [13, "b"], "c", [["d"], 11], 12, ["e"]], "f", 18]
sum = (list[0] + list[1] + list[2] + list[5]) + (list[3][1] + list[3][2] + list[3][6]) + (list[3][3][0] + list[3][5][1])
concatenate = (str(list[4])) + (str(list[3][0]) + str(list[3][4])) + (str(list[3][3][1]) + str(list[3][7][0]) + str(list[3][5][0][0])) 
print(sum)
print(concatenate)