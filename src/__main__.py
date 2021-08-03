from Student import Student,BuilderStudent

if __name__ == "__main__":
    builder= Student.getBuilder()
    builder.withName("Vladimir").withSurname("Putin").withEmail("mail@gmail.com").withAge(66)
    student= builder.build()
    print(student)