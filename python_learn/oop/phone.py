class Phone:
    def __init__(self, name: str, age: int=0):
        self.__name = name
        self.__age = age
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.set_age(age)

    def set_age(self, age: int):
        if age >= 0 and age < 300:
            self.__age = age

    def get_age(self) -> int:
        return self.__age

    def call(self, phoneNumber: str):
        print(f"{self.__name} звоню на номер {phoneNumber}")
        print("Dial succesfull")
        print(f"AT+{phoneNumber}")
    
    def accept_call(self) -> None:
        print(f"{self.__name} принимаю звонок")

if __name__ == "__main__":
    print("hello")