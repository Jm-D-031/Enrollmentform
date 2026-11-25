from datetime import date
from django.db import models


class SchoolClass(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "classes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Student(models.Model):
    STATUS = [("Enrolled", "Enrolled"), ("Pending", "Pending")]
    PAYMENT = [("Paid", "Paid"), ("Partial", "Partial"), ("Unpaid", "Unpaid")]
    GENDER = [("Female", "Female"), ("Male", "Male")]

    school_class = models.ForeignKey(SchoolClass, on_delete=models.PROTECT, related_name="students")
    student_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=10, choices=STATUS, default="Pending")

    # Personal info
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    nationality = models.CharField(max_length=60, default="Filipino")
    religion = models.CharField(max_length=60, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # Background info
    father_name = models.CharField(max_length=120, blank=True)
    father_job = models.CharField(max_length=80, blank=True)
    mother_name = models.CharField(max_length=120, blank=True)
    mother_job = models.CharField(max_length=80, blank=True)
    guardian_name = models.CharField(max_length=120, blank=True)
    guardian_phone = models.CharField(max_length=30, blank=True)
    siblings = models.PositiveSmallIntegerField(default=0)
    previous_school = models.CharField(max_length=150, blank=True)
    last_grade_completed = models.CharField(max_length=30, blank=True)

    # Enrollment
    enrolled_on = models.DateField(default=date.today)
    payment = models.CharField(max_length=10, choices=PAYMENT, default="Unpaid")

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    @property
    def full_name(self):
        mid = f" {self.middle_name[0]}." if self.middle_name else ""
        return f"{self.first_name}{mid} {self.last_name}"

    @property
    def initials(self):
        return (self.first_name[:1] + self.last_name[:1]).upper()

    @property
    def age(self):
        t = date.today()
        return t.year - self.birthdate.year - ((t.month, t.day) < (self.birthdate.month, self.birthdate.day))

    @property
    def average(self):
        grades = [g.score for g in self.grades.all()]
        return round(sum(grades) / len(grades), 1) if grades else None


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    subject = models.CharField(max_length=80)
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.student} – {self.subject}"


class Document(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="documents")
    name = models.CharField(max_length=100)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} – {self.name}"
