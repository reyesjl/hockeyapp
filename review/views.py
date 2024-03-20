from django.shortcuts import render

def thankyou(request, message):
    """
    Renders the thank you page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the thank you page.
    """
    return render(request, 'review/thankyou.html', {'message': message})
