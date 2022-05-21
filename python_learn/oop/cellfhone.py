import phone

class CellPhone(phone.Phone):
    def decline_call(self):
        print("сбрасываем звонок")
    
    def call(self, phoneNumber):
        super().call(phoneNumber)
        print("Звоним через сотовую связь")