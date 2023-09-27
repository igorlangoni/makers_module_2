class Contact():
    def __init__(self, name, phone_number):
        index = 0
        for char in phone_number:
            if index < 4 or index > 4:
                if not char.isnumeric():
                    raise Exception("NUMERO INCORRETO")
                else:
                    index += 1
            elif index == 4:
                if char != '-':
                    raise Exception("NUMERO INCORRETO")
                else:
                    index += 1
        self.name = name
        self.phone_number = phone_number