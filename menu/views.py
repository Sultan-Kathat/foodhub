from django.shortcuts import render

# Create your views here.
dish_name=["Chicken Biryani", "Mutton Biryani", " Chicken Biryani (Boneless)", "Mutton Biryani(Boneless)", "Egg Biryani",  ]

price=["250.00", "300.00", "350.00","300.00", "350.00", ],

ingredients=[
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",

],
menu={}








def menu(request, name_fp):
    print(len(dish_name))

    for dish in dish_name:
        print(dish)

    data = dish_name[2]
    print(data)


    name_fp = "Biryani Moods"
    return render(request, 'menu/menu.html',{
        "name_fp": name_fp,
        #"menu":menu,
     

    })
