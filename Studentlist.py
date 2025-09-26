class ManagerList:
    def __init__(self,
                 name : str,
                 birth : str,
                 id : str,
                 major : str,
                 gpa : float
                 ):
        self.__name = name
        self.__birth = birth
        self.__id = id
        self.__major = major
        self.__gpa = gpa

    def __str__(self):
        return(f"Name: {self.__name} Birth: {self.__birth} ID: {self.__id}"
               f"Major: {self.__major} GPA: {self.__gpa}")
    
    def to_dict(self):
        return {
            'StudentsName' : self.__name,
            'StudentsBirth': self.__birth,
            'ID': self.__id,
            'Major': self.__major,
            'GPA': self.__gpa
        }
        
        
        