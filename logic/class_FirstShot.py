from dataclasses import dataclass

class FirstShot:
    first_shot: bool = False


    def __bool__(self):
        return self.first_shot


