from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField("제품명", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to="thumbnail", height_field=None, width_field=None, max_length=None)
    description = models.TextField("제품 설명")
    dt_created = models.DateTimeField("등록 일자", auto_now_add=True)
    exposure_start_date = models.DateField("노출 시작일")
    exposure_end_date = models.DateField("노출 종료일")
    is_active = models.BooleanField("활성화 여부")

    def __str__(self):
        return f'{self.title} 이벤트 입니다.'
