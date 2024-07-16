class Grand:
    house="appartment"
    
    
class Father(Grand):
    car="farari"
    
    def __init__(self) -> None:
        print("new house")
        print(self.car)
        super().__init__()
        
class Mother:
    jewelry="Diamond"
    
class Son(Father,Mother):
    console="PS5"
    def __init__(self) -> None:
        print(self.console)
        super().__init__()

son=Son()

