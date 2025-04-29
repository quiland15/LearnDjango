from django.shortcuts import render

def index(request):
    context = {
        'title':'Kontak saya',
        'developer':'Quiland Wenas',
        'navbar':[
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/kontak', 'Kontak']
        ],
        'banner':'kontak/image/kontak.png',
    }
    return render(request, 'index.html', context)