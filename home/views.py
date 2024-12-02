from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Myview(View):
        
    def get(self,request):
        peoples = [
            {"id":1,"first_name":"Toby","last_name":"Walklot","email":"twalklot0@lycos.com","gender":"Male"},
            {"id":2,"first_name":"Ottilie","last_name":"Heyward","email":"oheyward1@imdb.com","gender":"Female"},
            {"id":3,"first_name":"Jaclyn","last_name":"Rupp","email":"jrupp2@addthis.com","gender":"Female"},
            {"id":4,"first_name":"Ike","last_name":"Winders","email":"iwinders3@blog.com","gender":"Male"},
            {"id":5,"first_name":"Kylie","last_name":"Prettejohns","email":"kprettejohns4@rediff.com","gender":"Female"},
            {"id":6,"first_name":"Avictor","last_name":"Pettigree","email":"apettigree5@sogou.com","gender":"Male"},
        ]

        text = '''
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vero, ratione molestiae veritatis ipsum minus iure labore modi atque optio voluptatem commodi? Suscipit cumque saepe consequatur, incidunt id at, aspernatur laudantium tempora ab, ipsum cupiditate dignissimos adipisci quasi? Ut labore blanditiis laborum nisi, excepturi, voluptatum quia itaque ratione, assumenda eum ullam? 
        '''

        page = 'Home'
        return render( request, 'index.html', context={'peoples':peoples , 'text' : text , 'page' : page} )


def about(request):
    context = {'page' : ' About'}
    return render(request , 'about.html' , context)

def contact(request):
    context = {'page' : ' Contact'}
    return render(request , 'contact.html' , context)