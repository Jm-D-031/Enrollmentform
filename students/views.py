from django.db.models import Q
from django.shortcuts import render

from .models import SchoolClass, Student

TABS = [("personal", "Personal info"), ("background", "Background info"),
        ("academic", "Academic"), ("enrollment", "Enrollment")]


def student_list(request):
    classes = SchoolClass.objects.all()
    current = classes.filter(pk=request.GET.get("class")).first() or classes.first()

    students = Student.objects.filter(school_class=current) if current else Student.objects.none()
    total = students.count()

    q = request.GET.get("q", "").strip()
    if q:
        students = students.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(student_id__icontains=q)
        )

    selected = students.filter(pk=request.GET.get("student")).prefetch_related("grades", "documents").first() \
        if request.GET.get("student") else None

    tab = request.GET.get("tab", "personal")
    if tab not in dict(TABS):
        tab = "personal"

    return render(request, "students/student_list.html", {
        "classes": classes, "current": current, "students": students, "total": total,
        "selected": selected, "tab": tab, "tabs": TABS, "q": q,
    })
