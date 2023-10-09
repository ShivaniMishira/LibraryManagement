from django import forms
from info.models import Books, Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
                