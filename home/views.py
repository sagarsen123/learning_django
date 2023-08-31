from django.shortcuts import render
from django.http import HttpResponse 

# def home(request):
#     return HttpResponse("""
#                         <h1>Hey I am a Django Server...</h1>
#                         <h2> This is the Mutlti line Response from the django server</h2>
#                         <hr>
#                         """)

def home(request):
    peoples =[
        {
            'name': "Abhijeet",
            'age': 26
        },
        {
            'name': "Rohan Das",
            'age': 28
        },
        {
            'name': "Umair Anjum",
            'age': 18
        },
        {
            'name': "Talha Anjum",
            'age': 15
        },
        {
            'name': "Dilpreet Singh",
            'age': 35
        },
    ]

    vegetables = ['Pumpkin', 'Tomato', 'Potato']

    text = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Praesentium non perferendis beatae omnis velit neque, reprehenderit harum! Quae dignissimos error incidunt! Dolores itaque consequuntur saepe architecto maiores magnam eveniet ducimus vitae aliquid doloremque? Saepe dolorum quaerat pariatur beatae ullam excepturi facere. Eaque placeat incidunt est blanditiis accusamus veritatis recusandae, iste nobis error sunt deleniti iure adipisci modi voluptates maiores. Nobis iste totam tempore, placeat optio ut minima debitis! Voluptatum quod libero dolores ad veniam accusamus quas, maxime voluptate error, laborum necessitatibus quis architecto aliquid consequatur repudiandae odio nesciunt incidunt recusandae, quisquam doloremque. Nemo sit provident architecto voluptate error earum minima iure excepturi nisi odio in minus eos maiores, asperiores magni rerum nam dolores adipisci modi fugiat perspiciatis hic? Nulla, quisquam. Et at quos, eius eos quibusdam harum quia provident corporis magnam quis modi veritatis sunt vitae iure adipisci corrupti beatae. Libero reprehenderit deserunt saepe, facilis hic voluptates numquam quae fugit, quidem reiciendis ratione. Blanditiis velit magni ullam atque esse officia sit alias, tempore nesciunt? Debitis, reprehenderit ut. Quos enim inventore accusantium praesentium similique aliquam cum tenetur? Adipisci consequatur ex itaque laudantium culpa ut blanditiis, laboriosam aperiam, quisquam sit sunt fugit dolore placeat ea incidunt vitae excepturi, deleniti ipsum? Voluptatibus, optio."
    return render(request , 'home/index.html', context= {'page': "Home",'peoples' : peoples, "text" : text, "vegetables": vegetables})

def success_page(request):
    return HttpResponse("""<h1>Hey this is the sucess page</h1>
                        
    <a href="/contact">Contact</a>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/success-page">Success</a>
                        """)


def about(request):
    return render(request , "home/about.html",context={'page': 'About Page'})

def contact(request):
    return render(request, 'home/contact.html', context={'page':'Contact Page'})