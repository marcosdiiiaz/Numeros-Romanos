def decimal_a_romano(numeroDecimal):

    romano = ""
    del_1_al_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if numeroDecimal <= 3:
        for numero in range(numeroDecimal):
            romano += "I"
    if numeroDecimal == 4:
        romano = "IV"
    if numeroDecimal < 9 and numeroDecimal >= 5:
        for numero in range(numeroDecimal):
            romano = "V"
    if numeroDecimal == 9:
        romano = "IX"
    if numeroDecimal != del_1_al_9:
        romano = "X"
    
    return romano


    