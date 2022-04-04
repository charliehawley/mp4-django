from django.shortcuts import render


def go_home(request):
    return render(request, 'wisecrack/wisecrack.html')
