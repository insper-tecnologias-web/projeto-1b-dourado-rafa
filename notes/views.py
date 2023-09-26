from django.shortcuts import render, redirect
from .models import Note, Tag
import random

COLORS = ['Branco', 'Marrom', 'Azul', 'Rosa', 'Amarelo', 'Verde']

def create_tag(tagname:str) -> Tag:
    tagname = tagname.upper() if tagname != '' else 'SEM TAG' 
    tag , created = Tag.objects.get_or_create(name=tagname)
    if created:
        tag.color = random.randint(1, len(COLORS)-1)
    tag.save()
    return tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tagname = request.POST.get('tag')
        tag = create_tag(tagname)
        Note(title=title, content=content, tag=tag).save()
        return redirect('index')
    
    all_notes = Note.objects.all()
    all_tags = Tag.objects.all()
    return render(request, 'notes/create.html', {'notes': all_notes, 'tags': all_tags})


def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return redirect('index')


def edit_note(request, id):
    note = Note.objects.get(id=id)
    all_tags = Tag.objects.all()
    return render(request, 'notes/edit-note.html', {'notes': [], 'tags': all_tags, 'note': note})


def update_note(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.tag = create_tag(request.POST.get('tag'))
        note.save()
        return redirect('index')


def view_tags(request):
    all_tags = Tag.objects.all()
    tags_amounts = [(tag, Note.objects.filter(tag=tag.id).count()) for tag in all_tags]
    return render(request, 'notes/tags.html', {'tags_amounts': tags_amounts})


def view_notes_tag(request, id):
    tag = Tag.objects.get(id=id)
    tag_notes = Note.objects.filter(tag=id)
    return render(request, 'notes/notes-tag.html', {'notes': tag_notes, 'tag': tag, 'amount': len(tag_notes)})


def delete_tag(request, id):
    tag = Tag.objects.get(id=id)
    if tag.name != 'SEM TAG':
        tag_none = Tag.objects.get(name='SEM TAG')
        for note in Note.objects.filter(tag=tag.id):
            if note.tag.name == tag.name:
                note.tag = tag_none
                note.save()
        tag.delete()
    return redirect('index')


def edit_tag(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, 'notes/edit-tag.html', {'notes': [], 'tag': tag, 'tagcolor':COLORS[tag.color], 'colors':COLORS})


def update_tag(request, id):
    if request.method == 'POST':
        tag = Tag.objects.get(id=id)
        name = request.POST.get('name').upper()
        color = request.POST.get('color')
        
        if name != tag.name and Tag.objects.filter(name=name).count() > 0:
            tag_new = create_tag(name)
            Note.objects.filter(tag=tag.id).update(tag=tag_new)
            if tag.name != 'SEM TAG':
                tag.delete()
            tag = tag_new
        tag.name = name
        tag.color = COLORS.index(color)
        tag.save()
        
        return redirect('index')