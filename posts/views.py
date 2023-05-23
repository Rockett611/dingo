from django.contrib import messages
from django.shortcuts import render


from .forms import AuthorForm, PostForm
from .models import Author, Post
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_details(request, id):
    post = Post.objects.get(id=id)
    author = Author.objects.get(id=post.author_id)
    return render(request, 'posts/post_details.html', {'post': post, 'author': author})


def add_post(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()

            # f_title = form.cleaned_data["title"]
            # f_content = form.cleaned_data["content"]
            # a_author = form.cleaned_data["author"]
            # a_email = form.cleaned_data["email"]
            # obj_a, created = Author.objects.get_or_create(nick = a_author, email = a_email)
            # obj_p, created = Post.objects.get_or_create(title = f_title, content = f_content, author = obj_a)

    form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})


def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['email'] == '':
                form.cleaned_data['email'] = None

            form_nick = form.cleaned_data['nick']
            form_mail = form.cleaned_data['email']
            obj, created = Author.objects.get_or_create(nick = form_nick, email = form_mail)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy Result!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = AuthorForm()
    authors = Author.objects.all()
    return render(request, 'posts/authors_list.html', {'authors': authors, "form": form})


def authors_details(request, id):
    author = Author.objects.get(id=id)
    posts = Post.objects.filter(author_id=id)
    return render(request, 'posts/author_details.html', {'author': author, 'posts': posts})
