from django.db import models

class UserSubmission(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронный адрес")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    attached_file = models.FileField(upload_to="uploads/", blank=True, null=True, verbose_name="Прикрепить файл")
    agreement = models.BooleanField(default=False, verbose_name="Согласие на обработку данных")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "Пользователи"