from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie
def register_user(request):
    if request.method == "POST":
        print("I am W@@@@@@@@@@@@")
        return render(request, "index.html", {})
