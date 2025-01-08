from django.db import models

from django.db import models
from django.utils.html import mark_safe


#department model
status=(
    ('Pending...','Pending...'),
    ('Approved','Approved'),
    ('Rejected','Rejected'),
)
gender=(
  ('male','male'),
  ('female','female'),
)
academic_yearlist=(
  ('2020','2020'),
  ('2021','2021'),
  ('2022','2022'),
  ('2023','2023'),
  ('2024','2024'),
  ('2024','2024'),
  ('2025','2025'),
  ('2026','2026'),


)
Courselist=(
  ('Doctor of Philosophy in Education','Doctor of Philosophy in Education'),
  ('Master of Education','Master of Education'),
  ('Master of Business Administration ','Master of Business Administration '),
  ('Postgraduate Diploma in Education','Postgraduate Diploma in Education'),
  ('Bachelor of Education in Science','Bachelor of Education in Science'),
  ('Bachelor of Education in Arts','Bachelor of Education in Arts'),
  ('Bachelor of Geography and Environmental Studies','Bachelor of Geography and Environmental Studies'),
  ('Bachelor of Science in Mathematics and Statistics','Bachelor of Science in Mathematics and Statistics'),
  ('Bachelor of Sociology and Social Work','Bachelor of Sociology and Social Work'),
  ('Bachelor of Business Administration','Bachelor of Business Administration'),
  ('Bachelor of Philosophy with Ethics','Bachelor of Philosophy with Ethics'),
  ('Bachelor of Procurement and Supply Chain Management','Bachelor of Procurement and Supply Chain Management'),
  ('Bachelor of Science in Applied Biolog','Bachelor of Science in Applied Biolog'),
  ('Bachelor of Science in Chemistry','Bachelor of Science in Chemistry'),
  ('Bachelor of Science in Computer Science','Bachelor of Science in Computer Science'),

) 
departmentlist=(
  ('Department of Natural Sciences and Information Technology','Department of Natural Sciences and Information Technology'),
  ('Department of Agriculture, Earth and Environmental Sciences','Department of Agriculture, Earth and Environmental Sciences'),
  ('Department of Social Sciences and Humanities','Department of Social Sciences and Humanities'),
  ('Directorate of Non-Degree Programmes','Directorate of Non-Degree Programmes'),
)
facultylist=(
  ('Faculty of Science','Faculty of Science'),
  ('Faculty of Humanities and Business Studies','Faculty of Humanities and Business Studies'),
  ('education','education'),
)
class Department(models.Model):
    department_name=models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.department_name




#herroes


class Announcements(models.Model):
     heading=models.CharField(max_length=200)
     title=models.CharField(max_length=200)
     date_registered=models.DateField(auto_now_add=True)
     file=models.FileField(upload_to='announcements/')
     def __str__(self):
             return self.title
#class of status and view
class request_form(models.Model):
  regno=models.CharField(max_length=200,primary_key=True)
  Student_name=models.CharField(max_length=200)
  passport_size=models.ImageField(upload_to='passports/')
  gender=models.CharField(max_length=200,choices=gender)
  faculty=models.CharField(max_length=200,choices=facultylist)
  Course=models.CharField(max_length=200,choices=Courselist)
  department=models.CharField(max_length=200,choices=departmentlist)
  academic_year=models.CharField(max_length=200,choices=academic_yearlist)
  project_title=models.CharField(max_length=200)
  date_registered=models.DateField(auto_now_add=True)
  research_document=models.FileField(upload_to='research/')
  image=models.ImageField(upload_to='application/')
  status=models.CharField(max_length=200,choices=status)
  def __str__(self):
             return self.regno
       def image_tag(self):
            return mark_safe('<img src="%s"width="50"style="border-radius:4px">'% (self.passport_size.url))



  
