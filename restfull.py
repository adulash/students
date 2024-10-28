from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


#اعداد السماح بتشغيل اي بي اي على الويب اسمها ميدلوير
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"], 
                   allow_credentials=True,
                   allow_methods=["*"],allow_headers=["*"],)


class Student(BaseModel):
    id: int
    name: str
    grade: int



students = [
    Student(id=1,name="Abdullah",grade=5),
    Student(id=2,name="Ali",grade=4),
    Student(id=3,name="Mohammed",grade=3)
]


@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def creat_student(new_student: Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: Student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = update_student    # في حالة الحقيقة ربما لا يعمل هذا الاندكس بسبب ربما يتغير الرقم في أي وقت
            return update_student
    return {"error": "student not found"}
    

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            del students[i]  # في حالة الحقيقة ربما لا يعمل هذا الاندكس بسبب ربما يتغير الرقم في أي وقت
            return {"message": "student deleted"}
    return {"error": "student not found"}