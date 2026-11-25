from datetime import date
from django.core.management.base import BaseCommand
from students.models import Document, Grade, SchoolClass, Student

SUBJECTS = ["Mathematics", "Science", "English", "Filipino", "Araling Panlipunan"]
DOCS = ["Birth certificate", "Report card", "Good moral certificate", "2x2 ID photo"]

# (class, id, first, middle, last, birthdate, gender, religion, address, father, fjob, mother, mjob,
#  phone, school, status, payment, grades, missing_docs)
DATA = [
    (0, "2026-0001", "Maria", "Santos", "Dela Cruz", date(2010, 3, 14), "Female", "Roman Catholic",
     "12 Mabini St., Calapan City", "Roberto Dela Cruz", "Fisherman", "Elena Dela Cruz", "Teacher",
     "0917 123 4567", "Calapan Elementary School", "Enrolled", "Paid", [94, 92, 95, 93, 91], []),
    (0, "2026-0002", "Juan", "Reyes", "Garcia", date(2010, 7, 2), "Male", "Iglesia ni Cristo",
     "45 Rizal Ave., Naujan", "Pedro Garcia", "Driver", "Lita Garcia", "Vendor",
     "0922 555 0192", "Naujan National High School", "Enrolled", "Paid", [86, 89, 88, 90, 88], [3]),
    (0, "2026-0003", "Angela", "Mendoza", "Ramos", date(2009, 11, 21), "Female", "Born Again Christian",
     "8 Luna St., Baco", "Carlos Ramos", "Engineer", "Divina Ramos", "Nurse",
     "0933 888 2210", "Baco Integrated School", "Pending", "Partial", [96, 95, 94, 95, 95], [2]),
    (1, "2026-0004", "Mark", "Villanueva", "Tan", date(2010, 1, 9), "Male", "Buddhist",
     "77 Quezon Blvd., Calapan City", "Henry Tan", "Business owner", "Grace Tan", "Accountant",
     "0945 321 6543", "Divine Word Academy", "Enrolled", "Paid", [93, 90, 89, 88, 92], []),
    (1, "2026-0005", "Sofia", "Castillo", "Navarro", date(2010, 5, 30), "Female", "Roman Catholic",
     "3 Burgos St., Pinamalayan", "Ramon Navarro", "Farmer", "Cynthia Navarro", "Housewife",
     "0956 777 3030", "Pinamalayan Central School", "Enrolled", "Paid", [90, 92, 91, 93, 89], []),
    (1, "2026-0006", "Daniel", "Aquino", "Lopez", date(2009, 9, 17), "Male", "Roman Catholic",
     "21 Del Pilar St., Roxas", "Jose Lopez", "Electrician", "Mila Lopez", "Seamstress",
     "0966 404 8080", "Roxas Municipal High School", "Pending", "Unpaid", [84, 85, 87, 86, 86], [1, 2]),
]


class Command(BaseCommand):
    help = "Add sample classes and students"

    def handle(self, *args, **opts):
        classes = [SchoolClass.objects.get_or_create(name=n)[0]
                   for n in ("Grade 10 – Rizal", "Grade 10 – Bonifacio")]
        for (c, sid, fn, mn, ln, bd, g, rel, addr, fa, fj, mo, mj, ph, sch, st, pay, grades, missing) in DATA:
            s, created = Student.objects.get_or_create(student_id=sid, defaults=dict(
                school_class=classes[c], first_name=fn, middle_name=mn, last_name=ln, birthdate=bd,
                gender=g, religion=rel, address=addr, father_name=fa, father_job=fj, mother_name=mo,
                mother_job=mj, guardian_name=mo, guardian_phone=ph, phone=ph,
                email=f"{fn.lower()}.{ln.lower().replace(' ', '')}@email.com",
                siblings=2, previous_school=sch, last_grade_completed="Grade 9", status=st, payment=pay))
            if created:
                for subj, score in zip(SUBJECTS, grades):
                    Grade.objects.create(student=s, subject=subj, score=score)
                for i, d in enumerate(DOCS):
                    Document.objects.create(student=s, name=d, submitted=i not in missing)
        self.stdout.write(self.style.SUCCESS("Sample data added."))
