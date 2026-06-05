class User:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.notification_preferences = []  # "email", "sms", "push"

    def add_notification_preference(self, preference: str):
        if preference not in self.notification_preferences:
            self.notification_preferences.append(preference)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Student(User):
    def __init__(self, name: str, email: str, phone: str, student_id: str):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.role = "Öğrenci"

    def __str__(self):
        return f"[Öğrenci] {self.name} - {self.student_id}"


class Teacher(User):
    def __init__(self, name: str, email: str, phone: str, department: str):
        super().__init__(name, email, phone)
        self.department = department
        self.role = "Öğretmen"

    def __str__(self):
        return f"[Öğretmen] {self.name} - {self.department}"