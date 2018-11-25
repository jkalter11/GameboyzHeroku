from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Comment
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileEditForm, UserEditForm, CommentForm
from .models import Profile
from igdb_api_python.igdb import igdb
from twitch import TwitchClient
import json

igdb = igdb("d1299d9ef9359fa3d5dcc112abf4b956")
#igdb = igdb("03af7252c1029ac5f2235e4d92e9ab4d")


def home(request):
    return render(request, 'shop/home.html',
                 {'home': home})


def about(request):
    return render(request, 'shop/about.html', {})


def contact(request):
    return render(request, 'shop/contact.html', {})

@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    result = igdb.games({
        'ids': [1942, 5503, 27081, 7346, 1905, 25657, 19565, 19560, 7331, 37777, 26758, 25076, 359, 11156, 8173, 103054,
                28540, 3750, 9498, 7334, 9630, 11133, 9176, 76885, 12571, 11800, 19470, 36926, 7603, 19562],
        'fields': ['cover', 'slug', 'name', 'summary', 'rating']
    })
    results = igdb.companies({
        'ids': [70, 168, 51],
        'fields': 'name'
    })
    game1 = json.dumps(result.body[0]['summary'])
    games1 = json.loads(game1)
    game2 = json.dumps(result.body[1]['summary'])
    games2 = json.loads(game2)
    game3 = json.dumps(result.body[2]['summary'])
    games3 = json.loads(game3)
    game4 = json.dumps(result.body[3]['summary'])
    games4 = json.loads(game4)
    game5 = json.dumps(result.body[4]['summary'])
    games5 = json.loads(game5)
    game6 = json.dumps(result.body[5]['summary'])
    games6 = json.loads(game6)
    game7 = json.dumps(result.body[6]['summary'])
    games7 = json.loads(game7)
    game8 = json.dumps(result.body[7]['summary'])
    games8 = json.loads(game8)
    game9 = json.dumps(result.body[8]['summary'])
    games9 = json.loads(game9)
    game10 = json.dumps(result.body[9]['summary'])
    games10 = json.loads(game10)
    game11 = json.dumps(result.body[10]['summary'])
    games11 = json.loads(game11)
    game12 = json.dumps(result.body[11]['summary'])
    games12 = json.loads(game12)
    game13 = json.dumps(result.body[12]['summary'])
    games13 = json.loads(game13)
    game14 = json.dumps(result.body[13]['summary'])
    games14 = json.loads(game14)
    game15 = json.dumps(result.body[14]['summary'])
    games15 = json.loads(game15)
    game16 = json.dumps(result.body[15]['summary'])
    games16 = json.loads(game16)
    game17 = json.dumps(result.body[16]['summary'])
    games17 = json.loads(game17)
    game18 = json.dumps(result.body[17]['summary'])
    games18 = json.loads(game18)
    game19 = json.dumps(result.body[18]['summary'])
    games19 = json.loads(game19)
    game20 = json.dumps(result.body[19]['summary'])
    games20 = json.loads(game20)
    game21 = json.dumps(result.body[20]['summary'])
    games21 = json.loads(game21)
    game22 = json.dumps(result.body[21]['summary'])
    games22 = json.loads(game22)
    game23 = json.dumps(result.body[22]['summary'])
    games23 = json.loads(game23)
    game24 = json.dumps(result.body[23]['summary'])
    games24 = json.loads(game24)
    game25 = json.dumps(result.body[24]['summary'])
    games25 = json.loads(game25)
    game26 = json.dumps(result.body[25]['summary'])
    games26 = json.loads(game26)
    game27 = json.dumps(result.body[26]['summary'])
    games27 = json.loads(game27)
    game28 = json.dumps(result.body[27]['summary'])
    games28 = json.loads(game28)
    game29 = json.dumps(result.body[28]['summary'])
    games29 = json.loads(game29)
    game30 = json.dumps(result.body[29]['summary'])
    games30 = json.loads(game30)
    co1 = json.dumps(results.body[0]['name'])
    comp1 = json.loads(co1)
    co2 = json.dumps(results.body[1]['name'])
    comp2 = json.loads(co2)
    co3 = json.dumps(results.body[2]['name'])
    comp3 = json.loads(co3)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'games1': games1,
                   'games2': games2,
                   'games3': games3,
                   'games4': games4,
                   'games5': games5,
                   'games6': games6,
                   'games7': games7,
                   'games8': games8,
                   'games9': games9,
                   'games10': games10,
                   'games11': games11,
                   'games12': games12,
                   'games13': games13,
                   'games14': games14,
                   'games15': games15,
                   'games16': games16,
                   'games17': games17,
                   'games18': games18,
                   'games19': games19,
                   'games20': games20,
                   'games21': games21,
                   'games22': games22,
                   'games23': games23,
                   'games24': games24,
                   'games25': games25,
                   'games26': games26,
                   'games27': games27,
                   'games28': games28,
                   'games29': games29,
                   'games30': games30,
                   'comp1': comp1,
                   'comp2': comp2,
                   'comp3': comp3,
                   })

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'shop/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'shop/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'shop/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def game_reviews(request):
    result = igdb.games({
        'ids': [1942, 5503, 27081, 7346, 1905, 25657, 19565, 19560, 7331, 37777, 26758, 25076, 359, 11156, 8173, 103054,
                28540, 3750, 9498, 7334, 9630, 11133, 9176, 76885, 12571, 11800, 19470, 36926, 7603, 19562],
        'fields': ['cover', 'slug', 'name', 'summary', 'rating']
    })
    game1 = json.dumps(result.body[0]['rating'])
    games1 = json.loads(game1)
    game2 = json.dumps(result.body[1]['rating'])
    games2 = json.loads(game2)
    game3 = json.dumps(result.body[2]['rating'])
    games3 = json.loads(game3)
    game4 = json.dumps(result.body[3]['rating'])
    games4 = json.loads(game4)
    game5 = json.dumps(result.body[4]['rating'])
    games5 = json.loads(game5)
    game6 = json.dumps(result.body[5]['rating'])
    games6 = json.loads(game6)
    game7 = json.dumps(result.body[6]['rating'])
    games7 = json.loads(game7)
    game8 = json.dumps(result.body[7]['rating'])
    games8 = json.loads(game8)
    game9 = json.dumps(result.body[8]['rating'])
    games9 = json.loads(game9)
    game10 = json.dumps(result.body[9]['rating'])
    games10 = json.loads(game10)
    game11 = json.dumps(result.body[10]['rating'])
    games11 = json.loads(game11)
    game12 = json.dumps(result.body[11]['rating'])
    games12 = json.loads(game12)
    game13 = json.dumps(result.body[12]['rating'])
    games13 = json.loads(game13)
    game14 = json.dumps(result.body[13]['rating'])
    games14 = json.loads(game14)
    game15 = json.dumps(result.body[14]['rating'])
    games15 = json.loads(game15)
    game16 = json.dumps(result.body[15]['rating'])
    games16 = json.loads(game16)
    game17 = json.dumps(result.body[16]['rating'])
    games17 = json.loads(game17)
    game18 = json.dumps(result.body[17]['rating'])
    games18 = json.loads(game18)
    game19 = json.dumps(result.body[18]['rating'])
    games19 = json.loads(game19)
    game20 = json.dumps(result.body[19]['rating'])
    games20 = json.loads(game20)
    game21 = json.dumps(result.body[20]['rating'])
    games21 = json.loads(game21)
    game22 = json.dumps(result.body[21]['rating'])
    games22 = json.loads(game22)
    game23 = json.dumps(result.body[22]['rating'])
    games23 = json.loads(game23)
    game24 = json.dumps(result.body[23]['rating'])
    games24 = json.loads(game24)
    game25 = json.dumps(result.body[24]['rating'])
    games25 = json.loads(game25)
    game26 = json.dumps(result.body[25]['rating'])
    games26 = json.loads(game26)
    game27 = json.dumps(result.body[26]['rating'])
    games27 = json.loads(game27)
    game28 = json.dumps(result.body[27]['rating'])
    games28 = json.loads(game28)
    game29 = json.dumps(result.body[28]['rating'])
    games29 = json.loads(game29)
    game30 = json.dumps(result.body[29]['rating'])
    games30 = json.loads(game30)
    gname1 = json.dumps(result.body[0]['name'])
    name1 = json.loads(gname1)
    gname2 = json.dumps(result.body[1]['name'])
    name2 = json.loads(gname2)
    gname3 = json.dumps(result.body[2]['name'])
    name3 = json.loads(gname3)
    gname4 = json.dumps(result.body[3]['name'])
    name4 = json.loads(gname4)
    gname5 = json.dumps(result.body[4]['name'])
    name5 = json.loads(gname5)
    gname6 = json.dumps(result.body[5]['name'])
    name6 = json.loads(gname6)
    gname7 = json.dumps(result.body[6]['name'])
    name7 = json.loads(gname7)
    gname8 = json.dumps(result.body[7]['name'])
    name8 = json.loads(gname8)
    gname9 = json.dumps(result.body[8]['name'])
    name9 = json.loads(gname9)
    gname10 = json.dumps(result.body[9]['name'])
    name10 = json.loads(gname10)
    gname11 = json.dumps(result.body[10]['name'])
    name11 = json.loads(gname11)
    gname12 = json.dumps(result.body[11]['name'])
    name12 = json.loads(gname12)
    gname13 = json.dumps(result.body[12]['name'])
    name13 = json.loads(gname13)
    gname14 = json.dumps(result.body[13]['name'])
    name14 = json.loads(gname14)
    gname15 = json.dumps(result.body[14]['name'])
    name15 = json.loads(gname15)
    gname16 = json.dumps(result.body[15]['name'])
    name16 = json.loads(gname16)
    gname17 = json.dumps(result.body[16]['name'])
    name17 = json.loads(gname17)
    gname18 = json.dumps(result.body[17]['name'])
    name18 = json.loads(gname18)
    gname19 = json.dumps(result.body[18]['name'])
    name19 = json.loads(gname19)
    gname20 = json.dumps(result.body[19]['name'])
    name20 = json.loads(gname20)
    gname21 = json.dumps(result.body[20]['name'])
    name21 = json.loads(gname21)
    gname22 = json.dumps(result.body[21]['name'])
    name22 = json.loads(gname22)
    gname23 = json.dumps(result.body[22]['name'])
    name23 = json.loads(gname23)
    gname24 = json.dumps(result.body[23]['name'])
    name24 = json.loads(gname24)
    gname25 = json.dumps(result.body[24]['name'])
    name25 = json.loads(gname25)
    gname26 = json.dumps(result.body[25]['name'])
    name26 = json.loads(gname26)
    gname27 = json.dumps(result.body[26]['name'])
    name27 = json.loads(gname27)
    gname28 = json.dumps(result.body[27]['name'])
    name28 = json.loads(gname28)
    gname29 = json.dumps(result.body[28]['name'])
    name29 = json.loads(gname29)
    gname30 = json.dumps(result.body[29]['name'])
    name30 = json.loads(gname30)
    return render(request, 'shop/product/reviews.html', {'games1': games1,
                                                         'games2': games2,
                                                         'games3': games3,
                                                         'games4': games4,
                                                         'games5': games5,
                                                         'games6': games6,
                                                         'games7': games7,
                                                         'games8': games8,
                                                         'games9': games9,
                                                         'games10': games10,
                                                         'games11': games11,
                                                         'games12': games12,
                                                         'games13': games13,
                                                         'games14': games14,
                                                         'games15': games15,
                                                         'games16': games16,
                                                         'games17': games17,
                                                         'games18': games18,
                                                         'games19': games19,
                                                         'games20': games20,
                                                         'games21': games21,
                                                         'games22': games22,
                                                         'games23': games23,
                                                         'games24': games24,
                                                         'games25': games25,
                                                         'games26': games26,
                                                         'games27': games27,
                                                         'games28': games28,
                                                         'games29': games29,
                                                         'games30': games30,
                                                         'name1': name1,
                                                         'name2': name2,
                                                         'name3': name3,
                                                         'name4': name4,
                                                         'name5': name5,
                                                         'name6': name6,
                                                         'name7': name7,
                                                         'name8': name8,
                                                         'name9': name9,
                                                         'name10': name10,
                                                         'name11': name11,
                                                         'name12': name12,
                                                         'name13': name13,
                                                         'name14': name14,
                                                         'name15': name15,
                                                         'name16': name16,
                                                         'name17': name17,
                                                         'name18': name18,
                                                         'name19': name19,
                                                         'name20': name20,
                                                         'name21': name21,
                                                         'name22': name22,
                                                         'name23': name23,
                                                         'name24': name24,
                                                         'name25': name25,
                                                         'name26': name26,
                                                         'name27': name27,
                                                         'name28': name28,
                                                         'name29': name29,
                                                         'name30': name30,
                                                         })



def comment_rev (request, year, month, day, post):
    post = get_object_or_404(Product, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # List of active comments for this review
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'shop/product/reviews.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts})

