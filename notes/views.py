from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note(title=title, content=content).save()
        return redirect('index')
    
    all_notes = Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': all_notes})


def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return redirect('index')


def edit_note(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'notes/edit.html', {'note': note})


def update_note(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('index')