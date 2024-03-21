from django.shortcuts import render, redirect
from .forms import PromotionForm, ContactForm, FeedbackForm, ApplicationForm

def promotion(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:thankyou', message='Your promotion form has been submitted.')
    else:
        form = PromotionForm()
    
    return render(request, 'info/promotion.html', {'form':form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:thankyou', message='Your contact form has been submitted.')
    else:
        form = ContactForm()

    return render(request, 'info/contact.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:thankyou', message='Your feedback form has been submitted.')
    else:
        form = FeedbackForm()

    return render(request, 'info/feedback.html', {'form': form})

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:thankyou', message='Your application form has been submitted.')
    else:
        form = ApplicationForm()
    return render(request, 'info/application.html', {'form':form})


def thankyou(request, message):
    """
    Renders the thank you page for promotions, feedback, contact, and apply.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the thank you page.
    """
    return render(request, 'info/thankyou.html', {'message': message})