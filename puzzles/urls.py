from django.conf.urls import url

from puzzles import views

urlpatterns = [
    url(r'^keys/$', views.KeysTemplateView.as_view(), name='keys'),
    url(r'^keys2/$', views.Keys2TemplateView.as_view(), name='keys2'),
    url(r'^keys3/$', views.Keys3TemplateView.as_view(), name='keys3'),
    url(r'^keys4/$', views.Keys4FormView.as_view(), name='keys4'),
    url(r'^solved-three-keys/$', views.Solved3KeysFormView.as_view(), name='solved-three-keys'),
    url(r'^crossed-lines/$', views.CrossedLinesFormView.as_view(), name='crossed-lines'),
    url(r'^what-puzzle/$', views.WhatPuzzleFormView.as_view(), name='what-puzzle'),
    url(r'^some-man/$', views.SomeManFormView.as_view(), name='some-man'),
    url(r'^solved-some-man/$', views.SolvedSomeManTemplateView.as_view(), name='solved-some-man'),
]