from django.shortcuts import render

# Create your views here. Наша страициа из приложения
def index_helloapp(request):  #http reqest На вход
    return render(request, 'index.html') # http response отправляем нашу начальную страницу

def about_page(request):
    return render(request, 'about_employ.html')

