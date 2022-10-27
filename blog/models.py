from django.db import models

# 클래스는 항상 첫글자가 대문자
# 함수는 항상 소문자로

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)