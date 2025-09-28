class StudentData:
    def __init__(
        self, __name: str, __birth: int, __SID: str, __major: str, __gpa: float
    ):
        self.name = __name
        self.birth = __birth
        self.sid = __SID
        self.major = __major
        self.gpa = __gpa

    # @property meaning Getter and Setter
    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if not 0.0 <= value <= 4.0:
            raise ValueError(f"Error: GPA {value} just around 0.0 to 4.0")

        self._gpa = value

    def __str__(self):
        return f"Name: {self.name} \nBirth: {self.birth} \nID: {self.sid} \nMajor: {self.major} \nGPA: {self.gpa}"