class Student:
    def __init__(self,name,sid):
        self.name=name
        self.sid=sid
        self.lessons={}
    
    def add_score(self,course_name,score):
        self.lessons[course_name]=score
        print("score added.")
    
    def show_info(self):
        print(f"{self.name}-{self.sid}")
        for keys, values in self.lessons.items():
            print(f"{keys}-->{values}")