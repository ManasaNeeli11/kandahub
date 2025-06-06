import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.conf import settings
from .models import Quiz, Question, Choice, UserQuizResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Password match check
        if password1 != password2:
            return render(request, "signup.html", {"error": "Passwords do not match"})

        # Password rules check
        # Minimum 8 characters, at least one uppercase letter, one lowercase letter, one digit and one special character
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password1):
            rules_msg = ("Password must be at least 8 characters long and include at least one uppercase letter, "
                         "one lowercase letter, one digit, and one special character (@, $, !, %, *, ?, &).")
            return render(request, "signup.html", {"error": rules_msg})

        # Username uniqueness
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already taken"})

        # Email uniqueness
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error": "Email already in use"})

        # Create user with hashed password
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        return redirect('login')

    return render(request, "signup.html")



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Replace with your homepage URL name
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def about(request):
      return render(request, 'aboutus.html')



@login_required(login_url='login')  # Use the name of your login URL
def explore(request):
    # your logic
    return render(request, 'explore.html')

@login_required(login_url='login')


def kandas(request):
    kandas = [
        {
            "title": "Bala Kanda",
             
            "image_url": settings.STATIC_URL + "media/pictures/7KANDA-1.jpg",
            "brief": "Witness the divine beginnings! Bala Kanda unfolds the enchanting childhood of Lord Rama, filled with wisdom, valor, and celestial grace. From sacred birth to the legendary swayamvara of Sita, every moment is a glimpse of destiny in motion.",
            "full_story_points": [
                "Divine birth of Lord Rama in Ayodhya.",
                "His growth into a noble and righteous prince.",
                "Training under Sage Vishwamitra and protecting sacred rituals.",
                "Breaking Lord Shiva's bow and marrying Sita in the grand swayamvara."
            ],
            "summary": "Bala Kanda paints a portrait of purity and promise, where a divine child steps forth to shape dharma.",
            "quote": "“Even in youth, greatness shines like the sun rising over still waters.”"
        },
        {
            "title": "Ayodhya Kanda",
            "image_url": settings.STATIC_URL + "media/pictures/7KANDA-2.jpg",
            "brief": "Dive into sacrifice and sorrow. Ayodhya Kanda captures the emotional saga of Rama’s exile, a tale of royal politics, motherly betrayal, and unwavering dharma.",
            "full_story_points": [
                "Dasharatha’s joy at Rama’s coronation turns into despair.",
                "Kaikeyi’s demand shocks the kingdom—Rama must go to exile.",
                "Rama, Sita, and Lakshmana leave the palace behind.",
                "Bharat’s agony and refusal to accept the throne."
            ],
            "summary": "This Kanda explores the burdens of duty and nobility of sacrifice in the face of heart-wrenching choices.",
            "quote": "“True royalty lies not in the crown, but in the courage to walk away from it.”"
        },
        {
            "title": "Aranya Kanda",
            "image_url": settings.STATIC_URL + "media/pictures/7KANDA-3.jpg",
            "brief": "Enter the sacred wild! Aranya Kanda brings to life the exile journey—encounters with sages, demons, and the dark turn with Sita’s abduction.",
            "full_story_points": [
                "Forest wanderings filled with divine and demonic interactions.",
                "Surpanakha’s insult and the wrath of Ravana.",
                "Golden deer and Sita’s longing lead to her abduction.",
                "Rama and Lakshmana discover the loss and prepare for war."
            ],
            "summary": "A tale of trials where dharma is tested and love proves its resilience in adversity.",
            "quote": "“When shadows fall, even the purest hearts must face the fire.”"
        },
        {
            "title": "Kishkindha Kanda",
            "image_url": settings.STATIC_URL + "media/pictures/7KANDA-4.jpg",
            "brief": "Bonds beyond blood! Kishkindha Kanda weaves brotherhood, loyalty, and new hope as Rama meets Hanuman and allies with the monkey king Sugriva.",
            "full_story_points": [
                "Rama meets Hanuman and forms an eternal bond.",
                "He helps Sugriva defeat Bali and regain his kingdom.",
                "Monkeys are rallied to search for Sita.",
                "Hanuman prepares for his divine leap."
            ],
            "summary": "Friendship is sacred; in this Kanda, loyalty becomes the bridge to destiny.",
            "quote": "“In the storm of sorrow, a friend’s hand becomes the anchor of hope.”"
        },
        {
            "title": "Sundara Kanda",
            "image_url": settings.STATIC_URL + "media/pictures/7KANDA-6.jpg",
            "brief": "A saga of strength and devotion! Sundara Kanda follows Hanuman’s heroic leap across the ocean, bringing hope to a grieving heart.",
            "full_story_points": [
                "Hanuman crosses the ocean defying all odds.",
                "Discovers Sita in Ashoka Vatika and gives her Rama’s ring.",
                "Destroys Lanka’s gardens and threatens Ravana.",
                "Returns victoriously with hope and assurance."
            ],
            "summary": "A solo act of faith becomes the turning point of war, lit by devotion’s fire.",
            "quote": "“The smallest being can carry the weight of the mightiest faith.”"
        },
        {
            "title": "Yuddha Kanda",
            "image_url": settings.STATIC_URL + "media/pictures/7KANDA-5.jpg",
            "brief": "Good versus evil in its grandest form! Yuddha Kanda roars with war cries, heroism, divine weapons, and the fall of the tyrant Ravana.",
            "full_story_points": [
                "Bridge to Lanka is built by Rama’s army.",
                "Fierce battles between vanaras and rakshasas.",
                "Kumbhakarna, Indrajit fall; Ravana is slain by Rama.",
                "Sita is rescued; Rama returns victorious."
            ],
            "summary": "The triumph of truth and justice echoes through every clash of steel.",
            "quote": "“Victory bows before the one who walks with dharma.”"
        },
        {
            "title": "Uttara Kanda",
            "image_url": settings.STATIC_URL + "media/pictures/7KANDA-7.jpg",
            "brief": "After the storm, comes the test of peace. Uttara Kanda portrays Rama’s reign, Sita’s sorrow, and the bittersweet farewell of a divine king.",
            "full_story_points": [
                "Rama returns to Ayodhya and is crowned king.",
                "Sita faces a second trial and is exiled.",
                "Birth and valiance of Lava and Kusha.",
                "Rama departs, leaving behind a legacy of righteousness."
            ],
            "summary": "Even after victory, the righteous path tests the heart with choices beyond judgment.",
            "quote": "“In sacrifice lies the soul of a true ruler.”"
        }
    ]
    return render(request, "kandas.html", {"kandas": kandas})


 


# def knowmore(request):
#     return redirect(request,"kandas.html") 



def logout(request):
    auth_logout(request)
    return redirect('login')


def quizzes(request):
    quiz_topics = [
        {
            'id': 1,
            'title': 'Bala Kanda Quiz',
            'description': 'Questions on the childhood and early life of Lord Rama.',
            'num_questions': 3
        },
        {
            'id': 2,
            'title': 'Ayodhya Kanda Quiz',
            'description': 'Test your knowledge about Rama’s exile and challenges.',
            'num_questions': 3
        },
        {
            'id': 3,
            'title': 'Aranya Kanda Quiz',
            'description': 'Quiz on Rama’s life in the forest and the challenges faced there.',
            'num_questions': 3
        },
        {
            'id': 4,
            'title': 'Kishkindha Kanda Quiz',
            'description': 'Explore the alliance between Rama and the monkey kingdom.',
            'num_questions': 6
        },
        {
            'id': 5,
            'title': 'Sundara Kanda Quiz',
            'description': 'Test your knowledge about Hanuman’s heroic journey to Lanka.',
            'num_questions': 6
        },
        {
            'id': 6,
            'title': 'Yuddha Kanda Quiz',
            'description': 'Questions on the epic battle between Rama and Ravana.',
            'num_questions': 6
        },
        {
            'id': 7,
            'title': 'Uttara Kanda Quiz',
            'description': 'Quizzes about Rama’s return and later life.',
            'num_questions': 6
        },
    ]
    return render(request, 'quizzes.html', {'quiz_topics': quiz_topics})


def quizzes_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes_list.html', {'quiz_topics': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.prefetch_related('choices').all()

    if request.method == 'POST':
        total = questions.count()
        correct = 0
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                choice = Choice.objects.filter(id=selected_choice_id, question=question).first()
                if choice and choice.is_correct:
                    correct += 1

        # Save user response
        UserQuizResponse.objects.create(
            user=request.user,
            quiz=quiz,
            score=correct
        )
        
        return render(request, 'quiz_result.html', {
            'quiz': quiz,
            'score': correct,
            'total': total,
        })

    return render(request, 'quiz_detail.html', {
        'quiz': quiz,
        'questions': questions
    })

def quiz_list_view(request):
    quiz_topics = Quiz.objects.all()
    return render(request, 'quizzes.html', {'quiz_topics': quiz_topics})

import logging
from django.views.defaults import server_error

logger = logging.getLogger(__name__)

def custom_500(request):
    logger.error("Server error on path: %s", request.path, exc_info=True)
    return server_error(request)
