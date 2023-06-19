from django.shortcuts import render

# Create your views here.

def my_html_file(request):
    return render(request, 'index.html')


def page_not_found(request, exception):
    return render(request, '404.html', status=404)

