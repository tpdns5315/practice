from django.db import models
from django.contrib.auth.models import User
# User 는 쟝고 accounts에 있는 데이터 테이블 = 로그인 정보

# Create your models here.

class Simu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    # accounts 테이블의 id(pk)를 가져오는(foreignkey)
    # foreign key가 accounts 테이블의 id(pk) 필드랑 이어지게 해줌
    body = models.TextField()
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_users')
    # user和liked-users结合起来

    # 미리보기 이름
    def __str__(self):
        if self.user:
            return f'{self.user.get_username()} : {self.body}'

        return f'{self.body}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Simu, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)