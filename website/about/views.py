from django.shortcuts import render
from django.conf import urls


def about(request):
    content = [
            {
                "text" : "Director , CEO",        
                "description" : "CEO is not always easy to understand. Both are high-ranking executives; however, they have a number of key differences in their roles. Simply put, a managing director is typically responsible for a single business unit, while the CEO is accountable for the entire organization.",
                "rasm" : "/img/director.png",
                "instagram" : "https://www.instagram.com/myurl/",
                "telegram" : "https://t.me/kunuzofficial"
            },

            {
                "text" : "Administration manager",        
                "description" : "Business administration, also known as business management, is the administration of a commercial enterprise. It includes all aspects of overseeing and supervising the business operations of an organization",
                "rasm" : "/img/programmer.png",
                 "instagram" : "https://www.instagram.com/korzinkauz/",
                 "telegram" : "https://t.me/kunuzofficial"
            },
            {
                "text" : "Marketing group manager",        
                "description" : "A group marketing manager leads and supervises a team of marketing professionals. They oversee all activities related to marketing, promotions, advertisements; and are often heavily involved in conceptualization and implementation. That said, their role is imperative for the growth and success of a company.",
                "rasm" : "/img/marketing.jpg",
                 "instagram" : "https://www.instagram.com/makro_supermarket/",
                 "telegram" : "https://t.me/kunuzofficial"
            },
            {
                "text" : "Programmer",        
                "description" : "Programmers write code for computer programs and mobile applications. They also are involved in maintaining, debugging and troubleshooting systems and software to ensure that everything is running smoothly.",
                "rasm" : "/img/adminhelper.jpg",
                 "instagram" : "https://www.instagram.com/havasuz/",
                 "telegram" : "www.telegram.org"
            },
    ]

    context = {

        'content' :content

    }

    return render(request , 'about.html', context)


