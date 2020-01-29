from django.http import HttpResponseRedirect
from django.views import generic

from puzzles.forms import CrossedLinesForm, KeyForm, KeysForm, SomeManForm, WhatPuzzleForm
from puzzles.utils import check_puzzle_ans, check_puzzle_crossed_lines, check_puzzle_fourth_key, check_puzzle_three_keys, check_what_puzzle


class KeysTemplateView(generic.TemplateView):
    template_name = "puzzles/keys.html"


class Keys2TemplateView(generic.TemplateView):
    template_name = "puzzles/keys2.html"


class Keys3TemplateView(generic.TemplateView):
    template_name = "puzzles/keys3.html"


class Keys4FormView(generic.FormView):
    form_class = KeysForm
    template_name = "puzzles/keys4.html"
    success_url = '/solved-three-keys/'

    def form_valid(self, form):
        key_one = form.cleaned_data['key_one']
        key_two = form.cleaned_data['key_two']
        key_three = form.cleaned_data['key_three']
        solved = check_puzzle_three_keys(key_one, key_two, key_three)
        if solved:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class Solved3KeysFormView(generic.FormView):
    form_class = KeyForm
    template_name = "puzzles/solved-three-keys.html"
    success_url = '/crossed-lines/'

    def form_valid(self, form):
        key_four = form.cleaned_data['key_four']
        solved = check_puzzle_fourth_key(key_four)
        if solved:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CrossedLinesFormView(generic.FormView):
    form_class = CrossedLinesForm
    template_name = "puzzles/crossed-lines.html"
    success_url = '/what-puzzle/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        solved = check_puzzle_crossed_lines(name)
        if solved:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class WhatPuzzleFormView(generic.FormView):
    form_class = WhatPuzzleForm
    template_name = "puzzles/what-puzzle.html"
    success_url = '/some-man/'

    def form_valid(self, form):
        what = form.cleaned_data['what']
        solved = check_what_puzzle(what)
        if solved:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SomeManFormView(generic.FormView):
    form_class = SomeManForm
    template_name = "puzzles/some-man.html"
    success_url = '/solved-some-man/'

    def form_valid(self, form):
        ans = form.cleaned_data['ans']
        solved = check_puzzle_ans(ans)
        if solved:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SolvedSomeManTemplateView(generic.TemplateView):
    template_name = "puzzles/solved-some-man.html"



