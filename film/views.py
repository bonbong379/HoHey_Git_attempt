from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import film_profile, Review, Essay, Comment

@login_required
def register(request):
    if request.method == "POST":
        form = FilmRegisterForm(request.POST)
        if form.is_valid():
        	form.instance.author = request.user
        	form.save()
        	film_name = form.cleaned_data.get('film_name')
        	messages.success(request, f'The profile for {film_name} is created on HoHey!')
        	return redirect('blog-home')
    else:
        form = FilmRegisterForm()
    return render(request, 'film_register.html', {'form': form})

def film_list(request):
    context = {
        'film_profiles': film_profile.objects.all()
    }
    return render(request, 'film_list.html', context)

def reviews_base(request, id, obj_type, create_form, del_form, edit_form, renderthing):
    
    if (form := create_form(request.POST)).is_valid():           #create review
        contents = form.cleaned_data['contents']
        obj_type.objects.create(master = film_profile.objects.get(id=id), content = contents, 
                                author = request.user, date_posted=timezone.now())
    elif (form := del_form(request.POST)).is_valid():    #delete review
        deleteid = form.cleaned_data['deleteid']
        if obj_type.objects.get(id=deleteid).author != request.user: #user not owner of this post
            messages.error(request, 'attempt to delete a post that isnt yours')
        else:
            thing = obj_type.objects.filter(id=deleteid)
            thing.delete()
    elif (form := edit_form(request.POST)).is_valid():    #edit review
        reviewid = form.cleaned_data['reviewid']
        if obj_type.objects.filter(id=reviewid).first().author != request.user: #user not owner of this post
            messages.error(request, 'attempt to change a post that isnt yours')
        else:
            newcont = form.cleaned_data['changecontents']
            orig = obj_type.objects.filter(id = reviewid).update(content = newcont)
            # the line above uses filter and not get because update wants query set for whatever reason
    context = {
        'Film': film_profile.objects.filter(id=id).first(),
        'Review': obj_type.objects.filter(master=film_profile.objects.filter(id=id).first()),
        'Form': create_form(),
        'currentuser': request.user,
        'deletereviewform': del_form(),
    }
    return render(request, renderthing, context)

def film_reviews(request, filmid):
    if request.method == 'POST':    
        return reviews_base(request, filmid, Review, ReviewForm, DelReviewForm, EditReviewForm, 'film.html')
    else:
        context = {
            'Film': film_profile.objects.filter(id=filmid).first(),
            'Review': Review.objects.filter(master=film_profile.objects.filter(id=filmid).first()),
            'Form': ReviewForm(),
            'currentuser': request.user,
            'deletereviewform': DelReviewForm(),
        }
    return render(request, 'film.html', context)

def film_essays(request, filmid):
    if request.method == 'POST':    
        if (form := CommentForm(request.POST)).is_valid():#if a new comment is made, add the comment
            parent = form.cleaned_data['commentparent']
            commentcontents = form.cleaned_data['commentcontents']
            masteressay = form.cleaned_data['commentmasteressay']
            if parent == '0':         #parent is '0' if it has no parent comment
                parent = None
            else:
                parent = Comment.objects.get(id=parent)
            Comment.objects.create(film_master = Film.objects.get(id=filmid), content = commentcontents, parent = parent, 
                                    author = request.user, date_posted=timezone.now(), master=Essay.objects.get(id=masteressay))
        else:
            return reviews_base(request, filmid, Essay, EssayForm, DelEssayForm, EditEssayForm, 'films/essays.html')    
    context = {
        'Film': Film.objects.filter(id=filmid).first(),
        'Review': Essay.objects.filter(master=Film.objects.get(id=filmid)),
        'comments': Comment.objects.filter(film_master = Film.objects.get(id=filmid)),
        'Form': EssayForm(),
        'currentuser': request.user,
        'deletereviewform': DelEssayForm(),
        'commentform': CommentForm(),
    }
    return render(request, 'films/essays.html', context)