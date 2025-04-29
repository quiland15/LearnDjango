from django.shortcuts import render

def index(request):
    context = {
        'title':'blog bersama',
        'developer':'quiland wenas',
        'navbar':[
            ['/', 'Home'],
            ['/blog','Blog'],
            ['/kontak','Kontak'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ],
        'banner':'blog/image/blog.png',
    }
    return render(request, 'index.html', context)

def artikel(request):
    context = {
        'title':'Artikel',
        'developer':'quild',
        'navbar':[
            ['/', 'Home'],
            ['/blog','Blog'],
            ['/kontak','Kontak'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ],
    }
    return render(request, 'index.html', context)

def berita(request):
    context = {
        'title':'Berita',
        'developer':'wenas',
        'navbar':[
            ['/', 'Home'],
            ['/blog','Blog'],
            ['/kontak','Kontak'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ],
    }
    return render(request, 'index.html', context)
