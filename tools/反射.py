# for i in range(1, 11):
#     for m in range(2, i):
#         if i % m == 0:
#             # print(f'i:{i}')
#             # print(f'm:{m}')
#             break
#     else:
#         print(i)
#
# aa = {"kk":99,"ll":999}
# aa["kkkk"] = 0000
# print(aa)


class A(object):
     bar = 1


     def hhh(self):
         print("hdsjhids")

a = A()
getattr(a, 'hhh')


class Student:
    student_id = ""
    student_name = ""

    # initial constructor to set the values
    def __init__(self):
        self.student_id = "101"
        self.student_name = "Adam Lam"

    def hhh(self):
        return 999


student = Student()
# get attribute values by using getattr() function
print('\ngetattr : name of the student is =', getattr(student, "student_name"))
print('\ngetattr : name of the student is =', getattr(student, "hhh"))
print('\ngetattr : name of the student is =', student.hhh)

choice_8 = models.Choice.objects.all().extra(
    select={'m': "select modify_time from question WHERE id=%s"},
    select_params=[1, ],
    tables=['question'],
    where=['choice.question_choice_id=question.id'],
    # params=[None, ],
    order_by=['-choice.id'],
)
print(choice_8)
print(choice_8.query)