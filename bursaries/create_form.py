from django import forms


class CreateBursaryForm(forms.Form):
    genders = (("male", "Male"), ("female", "Female"), ("other", "Other"))
    modes_of_study = (
        ("regular", "Regular"),
        ("parallel", "Parallel"),
        ("boarding", "Boarding"),
        ("part_time", "Part Time"),
    )

    full_name = forms.CharField(
        max_length=200, label="Name (as it appears in official documents)"
    )
    id_no = forms.CharField(max_length=200, label="ID or Passport NO")
    gender = forms.ChoiceField(choices=genders)
    dob = forms.DateField(label="Date of Birth")

    institution_name = forms.CharField(label="Name of School/College/University")
    admission_no = forms.CharField(label="Admission/Registration No", required=False)
    campus = forms.CharField(label="Campus or Branch", required=False)
    department = forms.CharField(label="Faculty or Department", required=False)
    course = forms.CharField(label="Course of Study", required=False)
    mode_of_study = forms.ChoiceField(choices=modes_of_study)
    class_grade_or_year = forms.CharField(label="Class, Grade or Year of Study")
    course_duration = forms.IntegerField(
        label="Course Duration (in years)", min_value=1, max_value=20
    )
    completion_date = forms.CharField(label="Completion Date (MMYY)")
    telephone_no = forms.CharField(label="Mobile/Telephone Number")
