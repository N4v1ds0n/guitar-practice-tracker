from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, PracticeSession
from .forms import GoalForm, PracticeSessionForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def dashboard(request):
    goals = Goal.objects.filter(user=request.user).order_by('-created_at')
    sessions = PracticeSession.objects.filter(user=request.user).order_by('-date')
    return render(request, 'practice/dashboard.html', {
        'goals': goals,
        'sessions': sessions
        })


def home(request):
    return render(request, 'practice/home.html')


@login_required
def goals_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'practice/goals_list.html', {'goals': goals})


@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    sessions = PracticeSession.objects.filter(goal=goal)
    return render(request, 'practice/goal_detail.html', {
        'goal': goal,
        'sessions': sessions
    })


@login_required
def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'practice/goal_form.html', {'form': form})


@login_required
def session_create(request):
    if request.method == 'POST':
        form = PracticeSessionForm(request.POST, user=request.user)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('dashboard')
    else:
        form = PracticeSessionForm(user=request.user)
    return render(request, 'practice/session_form.html', {'form': form})


@login_required
def session_create_for_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)

    if request.method == 'POST':
        form = PracticeSessionForm(request.POST, user=request.user)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.goal = goal
            session.save()
            return redirect('goal_detail', pk=goal.id)
    else:
        form = PracticeSessionForm(initial={'goal': goal})

        # Optionally hide the goal field in the form if it exists
        if 'goal' in form.fields:
            form.fields['goal'].widget = forms.HiddenInput()

    return render(request, 'practice/session_form.html', {'form': form, 'goal': goal})


@login_required
def session_detail(request, pk):
    session = get_object_or_404(PracticeSession, pk=pk, user=request.user)
    return render(request, 'practice/session_detail.html', {'session': session})
