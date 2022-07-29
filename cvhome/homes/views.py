import random


from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Mohmed, skills, Services,viewblogs,portfol, Comment, catagry
from .forms import CommentForm, ContactForm
from django.core.paginator import Paginator
from django.views.generic import ListView



def viewhome(ret):
    slug = "admin"
    skill = skills.objects.all()
    port = portfol.objects.all()
    Serv = Services.objects.all()
    mod = Mohmed.objects.get(slug=slug)
    form = ContactForm()
    if ret.method == 'POST':
        form = ContactForm(ret.POST)
        if form.is_valid():

            form.save()
            return render(ret, 'home/homecv.html', {'mohmed': mod,
                                                    'skills': skill,
                                                    'form': form,


                                                    })

    return render(ret, 'home/homecv.html', {'mohmed':mod,
                                            'skills': skill,
                                            'form': form,
                                            'port': port,
                                            'servs':Serv,

    })


def viewcv(ret):
    skill = skills.objects.all()
    slug="admin"
    mod = Mohmed.objects.get(slug=slug)
    view= viewblogs.objects.all().filter(active=True)
    cat=catagry.objects.all()

    return render(ret, 'home/home.html', {'skill':skill,
                                          'mohmed':mod,
                                          'blogs':view,
                                          'cat':cat,


                                          })




def viewblog(ret,slug):
    sl = "admin"
    mod = Mohmed.objects.get(slug=sl)
    skill = skills.objects.all()

    catt=catagry.objects.get(slug=slug)
    view = catt.catagry.filter(active=True)

    return render(ret, 'home/blog.html', {'skill':skill,
                                          'mohmed': mod,
                                          'blogs':view,
                                          'catts': catt,




                                          })





def viewreadblog(ret,slug):
    slugg = "admin"
    mod = Mohmed.objects.get(slug=slugg)
    view=viewblogs.objects.get(slug=slug)
    skill = skills.objects.all()
    com =view.comments.filter(active=True)

    new_comment = None
    if ret.method == 'POST':
        comment_form = CommentForm(data=ret.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = view
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(ret, 'home/readblog.html', {'skill':skill,
                                              'blogs': view,
                                              'mohmed': mod,
                                              'comm': com,
                                              'new_comment': new_comment,
                                           'comment_form': comment_form
                                          })














