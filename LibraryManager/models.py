from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Author(models.Model):

    name = models.CharField(max_length=50, default="Unknown")
    country = models.CharField(max_length=50, default="Unknown", blank=True)

    # class Meta:
    #     verbose_name = _("author")
    #     verbose_name_plural = _("authors")

    def __str__(self):
        return self.name + ' [' + str(self.pk) + ']'

    # def get_absolute_url(self):
    #     return reverse("author_detail", kwargs={"pk": self.pk})

class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey("LibraryManager.Author", on_delete=models.CASCADE)
    num_pages = models.IntegerField()



    # class Meta:
    #     verbose_name = _("book")
    #     verbose_name_plural = _("books")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("book_detail", kwargs={"pk": self.pk})

# class BookAuthor(models.Model):

#     book = models.ForeignKey("LibraryManager.Book", verbose_name=_(""), on_delete=models.CASCADE)
#     author = models.ForeignKey("LibraryManager.Author", verbose_name=_(""), on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = _("bookauthor")
#         verbose_name_plural = _("bookauthors")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("bookauthor_detail", kwargs={"pk": self.pk})

class Branch(models.Model):

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = PhoneNumberField()

    class Meta:
        verbose_name = "branch"
        verbose_name_plural = "branches"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("branch_detail", kwargs={"pk": self.pk})


class BookBranchCopies(models.Model):

    book = models.ForeignKey("LibraryManager.Book", on_delete=models.CASCADE)
    branch = models.ForeignKey("LibraryManager.Branch", on_delete=models.CASCADE)
    number_of_copies = models.IntegerField()

    class Meta:
        verbose_name = "Branch's Copies"
        verbose_name_plural = "Branch Copies"

    def __str__(self):
        return self.book + ', ' + self.branch + ', ' + self.number_of_copies

    # def get_absolute_url(self):
    #     return reverse("bookcopies_detail", kwargs={"pk": self.pk})

class Department(models.Model):

    name = models.CharField(max_length=50)
    budget = models.FloatField()

    # class Meta:
    #     verbose_name = _("department")
    #     verbose_name_plural = _("departments")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("department_detail", kwargs={"pk": self.pk})

class Employee(models.Model):

    # name = models.CharField(_("Name"), max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    salary = models.FloatField()
    branch = models.ForeignKey("LibraryManager.Branch", null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey("LibraryManager.Department", null=True, on_delete=models.SET_NULL)

    # class Meta:
    #     verbose_name = _("employee")
    #     verbose_name_plural = _("employees")

    def __str__(self):
        return self.user.name

    # def get_absolute_url(self):
    #     return reverse("employee_detail", kwargs={"pk": self.pk})
