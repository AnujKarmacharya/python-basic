class Person:
    def __init__(self, name, salary, password) -> None:
        self.name = name  # public
        self._salary = salary  # protected
        self.__password = password  # private

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


ram = Person(name="ram", salary=19000, password=123)
ram.password = "1234"
print(ram.password)
