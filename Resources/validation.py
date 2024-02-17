import re

class validation:
    PHONE = None

    def validation(number):
        number = str(number)
        validation.PHONE = ''.join(filter(str.isdigit, number))
    
        try:
            country_code = re.search(r'\((.*?)\)', number).group(1)
        except:
            print(f'''The {number} is not a valid number, the number must have the country code in parentheses 55 for Brazil or 1 for USA 
                  ex: (55) 9XXXX-XXXX or (1)-AAA-PPP-NNNN''')
            exit()

        if country_code == '55':
            return validation.number_validation_brazil()

        elif country_code == '1':
            return validation.number_validation_USA()

        else:
            print(f'The {number} is not a valid number, the number must have the country code 55 for Brazil or 1 for USA')
            exit()


    def number_validation_brazil():
        number = validation.PHONE
        if len(number) == 13:
            return number
        else:
            print(f'''O número {number} não é válido, o número deve conter código do país (55), DDD 
            e começar com o digito 9 seguido dos 8 números de telefone ex: (55) 9XXXX-XXXX''')
            exit()
    
    def number_validation_USA():
        number = validation.PHONE
        if len(number) == 11:
            return number
        else: 
            print(f'The {number} is not a valid number, the number must have the country code(1), the NPA and the number ex: (1)-AAA-PPP-NNNN')
            exit()
