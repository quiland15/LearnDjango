from django.shortcuts import render

def index(request):
    context = {
        'title':'Web Development',
        'developer':'Quiland',
        'navbar':[
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/kontak', 'Kontak']
        ],
        'banner':'image/beranda.png',
    }
    return render(request, 'index.html', context)