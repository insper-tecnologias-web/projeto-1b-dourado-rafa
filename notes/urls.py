from django.urls import path

from . import views

urlpatterns = [
    path('',                       views.index,          name='index'),
    path('tag/',                   views.view_tags,      name='view-tags'),
    path('tag/<int:id>/',          views.view_notes_tag, name='view-notes_tag'),

    path('delete/tag/<int:id>/',   views.delete_tag,     name='delete-tag'),
    path('edit/tag/<int:id>/',     views.edit_tag,       name='edit-tag'),
    path('update/tag/<int:id>/',   views.update_tag,     name='update-tag'),

    path('delete/note/<int:id>/',  views.delete_note,    name='delete-note'),
    path('edit/note/<int:id>/',    views.edit_note,      name='edit-note'),
    path('update/note/<int:id>/',  views.update_note,    name='update-note'),
]