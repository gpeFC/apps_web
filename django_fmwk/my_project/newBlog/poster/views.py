# Vistas para la app Poster (Project: newBlog)

from django.shorcuts import render_to_response

from poster.models import Category
from poster.models import Post

# Vista para un solo post.
def one_post(request, idpost):
    post = Post.objects.get(id=idpost)
    
    return render_to_response(
             "post.html",
              {
               "post":post,
              },
           )


# Vista para un listado de posts.
def home(request):
    post = Post.object.order_by("-creation_date")

    return render_to_response(
            "home.html",
            {
             "posts":posts,
            },
           )


# Vista para un listado de posts filtrado por categoria.
def post_by_category(request, idcategory):
    category = Category.objects.get(id=idcategory)
    post = category.post_set.order_by("-creation_date")

    return render_to_response(
             "home.html",
             {
              "posts":posts,
             },
           )
