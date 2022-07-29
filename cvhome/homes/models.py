import mailbox

from MySQLdb import _mysql
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField





class Mohmed(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    name = models.CharField(_("nae:"),max_length=50)


    img=models.ImageField(("img"),upload_to='profile',blank=True,null=True)
    slug = models.SlugField(_("slug"), blank=True, null=True)
    skis_name=models.TextField(_("skills"),blank=True, null=True)
    aboutme = models.TextField(_("about me "), blank=True, null=True)



    #about your
    phone = models.CharField(_("phone"),max_length=12, blank=True, null=True)
    address=models.CharField(_("your address"),max_length=50, blank=True, null=True)
    email=models.EmailField(_("email"))
    dgree=models.CharField(_("Dgree"),max_length=50, blank=True, null=True)
    experns=models.IntegerField(_("experns"), blank=True, null=True)
    brith=models.DateField(_("brithday"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Mohmed, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Mohmed")
        verbose_name_plural = _("Mohmeds")

    def __str__(self):
        return self.name



def create_profile(sender, **kwargs):

    if kwargs["created"]:

        Mohmed.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


class catagry(models.Model):
    name = models.CharField( max_length=100)
    slug = models.SlugField( max_length=100)



    def __str__(self):

        return self.name


class skills(models.Model):
    skil=models.CharField(_("nae:"),max_length=50)
    exp = models.IntegerField(_("how exp"))


    def __str__(self):
        return self.skil



class viewblogs(models.Model):

    title = models.CharField(_("title:"), max_length=50)
    slug = models.SlugField(_("slug"),max_length=200, unique=True)
    img = models.ImageField(("img"), upload_to='profile', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField(_("body"),blank=True, null=True)
    updated_on = models.DateTimeField(_("updated_on"),auto_now=True)
    catag = models.ForeignKey(catagry, on_delete=models.CASCADE, related_name='catagry', blank=True, null=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(_("created "),auto_now_add=True)





    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        viewblogs, on_delete=models.CASCADE, related_name='comments')



    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class portfol(models.Model):
     title=models.CharField(_('title'),max_length=200)
     img=models.ImageField(_('img'))
     link=models.CharField(_('link'),max_length=300)


     def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(_('title'), max_length=200)
    icon = models.CharField(_('icon'), max_length=300)
    body = models.TextField(_('body'))

    def __str__(self):
        return self.title


