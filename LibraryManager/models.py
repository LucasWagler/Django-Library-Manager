from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(_("Title"), max_length=100)
    num_pages = models.IntegerField(_("Number of Pages"))


    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

class Author(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    country = models.CharField(_("Country"), max_length=50)

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

class Employee(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.PhoneNumberField(_("Phone Number"))

    class Meta:
        verbose_name = _("employee")
        verbose_name_plural = _("employees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("employee_detail", kwargs={"pk": self.pk})
