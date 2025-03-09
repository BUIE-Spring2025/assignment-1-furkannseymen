def int_to_roman(num):
    Roman_numeral = ''
    while num > 0:
        if num >= 1000:
            Roman_numeral += 'M'
            num -= 1000
        elif num >= 900:
            Roman_numeral += 'CM'
            num -= 900
        elif num >= 500:
            Roman_numeral += 'D'
            num -= 500
        elif num >= 400:
            Roman_numeral += 'CD'
            num -= 400
        elif num >= 100:
            Roman_numeral += 'C'
            num -= 100
        elif num >= 90: 
            Roman_numeral += 'XC'
            num -= 90
        elif num >= 50:
            Roman_numeral += 'L'
            num -= 50
        elif num >= 40:
            Roman_numeral += 'XL'
            num -= 40
        elif num >= 10:
            Roman_numeral += 'X'
            num -= 10
        elif num >= 9:
            Roman_numeral += 'IX'
            num -= 9
        elif num >= 5:
            Roman_numeral += 'V'
            num -= 5
        elif num >= 4:
            Roman_numeral += 'IV'
            num -= 4
        elif num >= 1:
            Roman_numeral += 'I'
            num -= 1
    return Roman_numeral

