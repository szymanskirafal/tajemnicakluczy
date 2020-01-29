from django import forms

class CrossedLinesForm(forms.Form):
    name = forms.CharField(label="", max_length=10, required=True)


class KeyForm(forms.Form):
    key_four = forms.CharField(label="", max_length=10, required=True)


class KeysForm(forms.Form):
    key_one = forms.CharField(label="", max_length=10, required=True)
    key_two = forms.CharField(label="", max_length=10, required=True)
    key_three = forms.CharField(label="", max_length=10, required=True)


class WhatPuzzleForm(forms.Form):
    what = forms.CharField(label="", max_length=10, required=True)

class SomeManForm(forms.Form):
    ans = forms.CharField(label="", max_length=10, required=True)
