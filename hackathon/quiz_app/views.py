from django.shortcuts import render, redirect
from quiz_app.models import UserProfile, userScore, Category, Question
from django.contrib.auth.models import User
from quiz_app.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse
import random
import json


# Create your views here.

#Helper Function



def index(request):

    context_dict = {}

    return render(request, "index.html", context=context_dict)


#This shows the amount of categori
def category_select(request):

    category_list = Category.objects.all()

    context_dict = {}
    context_dict["categories"] = category_list

    return render(request, "category.html", context=context_dict)

# I might leave this for now. I'll need to clarify how we are getting the answer input
# before I can really go any further with this view
@login_required
def question(request, category_name_slug):
    context_dict = {}
    try:
        the_category = Category.objects.get(slug=category_name_slug)
        context_dict["category"] = the_category
        the_questions = Question.objects.filter(category=the_category)
        the_question = the_questions[random.randint(0, len(the_questions)-1)]
        #Get the question based on the question_id      
        context_dict["question"] = the_question
        the_choices = [the_question.wAnswer1, the_question.wAnswer2, the_question.wAnswer3, the_question.correctAnswer]
        random.shuffle(the_choices)
        context_dict["choices"] = the_choices
        context_dict["correct_answer"] = the_question.correctAnswer
        #If a question does not exist or whether a category doesn't exist
        #then we remove the question from the context_dict
    except:
        context_dict["category"] = None
        context_dict["question"] = None
        context_dict["correct_answer"] = None

    return render(request, "js_version.html", context=context_dict)

def json_test(request):
    the_dict = json.dumps({"test": "Does this send json data"})
    return HttpResponse(the_dict)

def new_question(request, category_name_slug):
    context_dict = {}
    #try:
    the_category = Category.objects.get(slug=category_name_slug)
    the_questions = Question.objects.filter(category=the_category)
    the_question = the_questions[random.randint(0, len(the_questions)-1)]
    context_dict["question"] = the_question.question
    the_answers = [the_question.wAnswer1, the_question.wAnswer2, the_question.wAnswer3, the_question.correctAnswer]
    random.shuffle(the_answers)
    context_dict["answers"] = the_answers
    context_dict["correct"] = the_question.correctAnswer
    #except:
        #context_dict = {"category": None, "Answers": None, "correct": None}
    context_dict = json.dumps(context_dict)
    return HttpResponse(context_dict)




#This gets the set of user object and gets the scores 
def leaderboard(request):
    score_list = []
    the_users = User.objects.all()
    for user in the_users:
        the_scores = UserScore.objects.filter(user=user)
        high_score = sum([score.score for score in the_scores])
        score_list.append((user.username, high_score))
    #Sort the high score list in order of ranking
    score_list = sorted(score_list, key=lambda elem: elem[1], reverse=True)
    context_dict = {}
    context_dict["scores"] = score_list
    return render(request, "leaderboards.html", context=context_dict)

#This view will make use of a form - Harsh is doing this
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
    
        if user:
            if user.is_active:

                login (request, user)
                return redirect (reverse('quiz_app:index'))
        
            else:

                return HttpResponse("Your Rango account is disabled.")
        else:

            print("Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")

    else: 

        return render(request, 'login.html')

#This will also make use of a form
def register(request):
    registered = False

    # If it is a http post we want to process data
    if request.method == 'POST':
        # Attempt to grab the raw form info
        # This view uses both the UserForm and UserProfileForm
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # If both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # save users form data to the database
            user = user_form.save()

            # Set_password hashes the password for us, once we hash it we update the user model.
            user.set_password(user.password)
            user.save()

            # Now we deal with UserProfile
            # We set commit=False to delay saving the model until we are ready - to avoid integrity issues
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did they upload a photo?
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # now we save this instance of userprofile
            profile.save()

            # Update variable to reflect success in reg
            registered = True
            return render(request, 'index.html')

        else:

            print(user_form.errors, profile_form.errors)

    else:
        # Not a POST so render instances of the forms for user to complete
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', context={'user_form': user_form,
                                                          'profile_form': profile_form,
                                                          'registered': registered})



#This view must not be seen by people who haven't registered

@login_required
def profile(request):    
    context_dict = {}
    context_dict["user"] = the_user
    return render(request, "profile.html", context=context_dict)

