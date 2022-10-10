from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML
from django import forms
from apps.reviews.models import Review, Ticket
from crispy_forms.bootstrap import InlineRadios
from betterforms.multiform import MultiModelForm


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        label='Note',
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'headline',
            InlineRadios('rating'),
            'body',
            Div(
                Div(
                    Submit('ajouter', 'Ajouter', css_class='w-75 mt-2'),
                    css_class="col-12 col-lg-6 text-center text-lg-left"
                ),
                Div(HTML(
                    "<input class='btn btn-primary w-75 mt-2' type='button' value='Retour' onclick='history.go(-1)'>"
                    ),
                    css_class="col-12 col-lg-6 text-center text-lg-right"
                    ),
                css_class="row mt-2 mb-4"
            ),
        )


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class TicketReviewMultiForm(MultiModelForm):
    form_classes = {
        'ticket': TicketForm,
        'review': ReviewForm,
    }