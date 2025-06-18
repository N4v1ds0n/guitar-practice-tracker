from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Goal, PracticeSession, StandardGoalDefinition
from .forms import GoalForm, PracticeSessionForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def about(request):
    return render(request,'practice/about.html')


@login_required
def dashboard(request):
    goals_queryset = Goal.objects.filter(user=request.user).order_by('-created_at')
    sessions_queryset = PracticeSession.objects.filter(user=request.user).order_by('-date')

    # Paginators
    goals_paginator = Paginator(goals_queryset, 2)  # 5 goals per page
    sessions_paginator = Paginator(sessions_queryset, 3)  # 10 sessions per page

    # Get current pages
    goals_page_number = request.GET.get('goals_page')
    sessions_page_number = request.GET.get('sessions_page')

    goals_page_obj = goals_paginator.get_page(goals_page_number)
    sessions_page_obj = sessions_paginator.get_page(sessions_page_number)

    return render(request, 'practice/dashboard.html', {
        'goals': goals_page_obj,
        'sessions': sessions_page_obj,
    })


def home(request):
    return render(request, 'practice/home.html')



@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    sessions = PracticeSession.objects.filter(goal=goal)
    goal_progress = goal.get_overall_progress()
    return render(request, 'practice/goal_detail.html', {
        'goal': goal,
        'sessions': sessions,
        'goal_progress': goal_progress
    })


@login_required
def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST, user=request.user)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = GoalForm(user=request.user)
    return render(request, 'practice/goal_form.html', {'form': form})


@login_required
def session_create(request):
    goal_types = {str(goal.id): goal.goal_type for goal in Goal.objects.filter(user=request.user)}
    if request.method == 'POST':
        form = PracticeSessionForm(request.POST, user=request.user)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('dashboard')
    else:
        form = PracticeSessionForm(user=request.user)
    return render(request, 'practice/session_form.html', {'form': form, 'goal_types': goal_types,})


@login_required
def session_create_for_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    goal_types = {str(goal.id): goal.goal_type for goal in Goal.objects.filter(user=request.user)}

    if request.method == 'POST':
        form = PracticeSessionForm(request.POST, user=request.user)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.goal = goal
            session.save()
            return redirect('goal_detail', pk=goal.id)
    else:
        form = PracticeSessionForm(initial={'goal': goal}, user=request.user)

    return render(request, 'practice/session_form.html',
                  {'form': form,
                   'goal': goal,
                   'goal_types': goal_types,
                   }
                  )


@login_required
def session_detail(request, pk):
    session = get_object_or_404(PracticeSession, pk=pk, user=request.user)
    return render(request, 'practice/session_detail.html', {'session': session})


@login_required
def get_standard_goal_description(request):
    goal_id = request.GET.get('id')
    try:
        goal = StandardGoalDefinition.objects.get(id=goal_id)
        return JsonResponse({'description': goal.description, 'title': goal.name})
    except StandardGoalDefinition.DoesNotExist:
        return JsonResponse({'error': 'Goal not found'}, status=404)