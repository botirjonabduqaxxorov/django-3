from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)    
    enrolled_at = models.DateTimeField(auto_now_add=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"Comment by {self.student.name} on {self.course.title}"
