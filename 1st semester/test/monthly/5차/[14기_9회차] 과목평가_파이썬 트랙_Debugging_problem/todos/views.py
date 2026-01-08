from django.shortcuts import render, redirect
from .models import Todo, Comment
from .forms import TodoForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
  todos = Todo.objects.all()
  context = {
    'todos': todos
  }
  return render(request, 'todos/index.html', context) 

def create(request):
  if request.method == 'POST':
    form = TodoForm(request.POST, request.FILES) 
    if form.is_valid():
      todo = form.save(commit=False)
      todo.user = request.user
      todo.save()
      return redirect('todos:index')
  else:
    form = TodoForm()
  context = {
    'form': form
  }
  return render(request, 'todos/create.html', context)


def detail(request, pk):
  todo = Todo.objects.get(pk=pk)
  comment_form = CommentForm() 
  context = {
    'todo': todo,
    'comment_form': comment_form 
  }
  return render(request, 'todos/detail.html', context)

def update(request, pk):
  todo = Todo.objects.get(pk=pk)
  # 요청을 보낸 유저와 작성자가 같은지 확인한다.
  if todo.user == request.user:
    created_at = todo.created_at
    if request.method == 'POST':
      form = TodoForm(request.POST, request.FILES) 
      # form으로 받지 않은 필드들의 값 할당
      if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.pk=pk
        todo.created_at = created_at
        todo.save()
        return redirect('todos:detail', pk=pk)
  else:
    # 요청자와 작성자가 일치하지 않을경우 수정 페이지 접근 불가.
    return redirect('todos:detail', pk=pk)
  form = TodoForm(instance=todo)
  context = {
    'form': form,
    'todo': todo,
  }
  return render(request, 'todos/update.html', context)
        
def delete(request, pk):
  todo = Todo.objects.get(pk=pk)
  todo.delete()
  return redirect('todos:index')

def comment_create(request, pk):
  todo = Todo.objects.get(pk=pk)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.todo = todo
      comment.user = request.user
      comment.save()
      return redirect('todos:detail', pk=pk)
  else:
    form = CommentForm()
  context = {
    'comment_form': form,
    'todo': todo
  }
  return render(request, 'todos/detail.html', context)


@require_POST 
def comment_delete(request, pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('todos:detail', pk=pk)

def toggle_complete(request, pk):
  todo = Todo.objects.get(pk=pk)
  todo.completed = not todo.completed
  todo.save()
  return redirect('todos:index')