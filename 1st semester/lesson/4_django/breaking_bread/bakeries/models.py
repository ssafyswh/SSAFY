from django.db import models

class Bakery(models.Model):
    # 빵집 이름 (20자 이내)
    name = models.CharField(max_length=20)

    # 주소
    address = models.TextField()

    # 평점 (예: 0.0 ~ 10.0 범위 예상, 소수점 1자리까지)
    rating = models.FloatField()

    # 시작/종료 시간
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()

    def __str__(self):
        return f'{self.name} ({self.rating}/10)'