from django.shortcuts import render


def go_home(request):
    '''
    View for returning to homepage
    '''
    return render(request, 'wisecrack/wisecrack.html')
