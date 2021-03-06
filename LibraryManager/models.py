from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import mark_safe

class Author(models.Model):

    name = models.CharField(max_length=50, default="Unknown")
    country = models.CharField(max_length=50, default="Unknown", blank=True, null=True)

    # class Meta:
    #     verbose_name = _("author")
    #     verbose_name_plural = _("authors")

    def __str__(self):
        return self.name + ' [' + str(self.pk) + ']'

    # def get_absolute_url(self):
    #     return reverse("author_detail", kwargs={"pk": self.pk})

class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey("LibraryManager.Author", on_delete=models.CASCADE, null=True, blank=True)
    num_pages = models.PositiveIntegerField(null=True, blank=True)
    price = models.FloatField(default=12.99, null=True, blank=True, validators=[MinValueValidator(0.00)])
    # photo = models.ImageField(upload_to='/book_img')
    # image = models.ImageField(upload_to='./book_img', null=True, blank=True)

    # def image_tag(self):
    #     return mark_safe('<img src="/book_img/%s" width="150" height="150" />' % (self.image))

    # image_tag.short_description = 'Image'


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
    address_1 = models.CharField(max_length=100, null=True, blank=True)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True, default='NY')
    postal_code = models.PositiveIntegerField(default=44444, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)

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
    number_of_copies = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Branch's Copies"
        verbose_name_plural = "Branch Copies"

    def __str__(self):
        return self.book.title + ', ' + self.branch.name + ', ' + str(self.number_of_copies)

    # def get_absolute_url(self):
    #     return reverse("bookcopies_detail", kwargs={"pk": self.pk})

class Department(models.Model):

    name = models.CharField(max_length=50)
    budget = models.FloatField(validators=[MinValueValidator(0.00)])

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
    # email = models.EmailField(max_length=254)
    phone = PhoneNumberField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.00)])
    branch = models.ForeignKey("LibraryManager.Branch", null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey("LibraryManager.Department", null=True, blank=True, on_delete=models.SET_NULL)

    # class Meta:
    #     verbose_name = _("employee")
    #     verbose_name_plural = _("employees")

    def __str__(self):
        return self.user.first_name + self.user.last_name

    # def get_absolute_url(self):
    #     return reverse("employee_detail", kwargs={"pk": self.pk})
