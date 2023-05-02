from django.shortcuts import render

def home(request):
    content = [
            {
                "text" : "Dubai",        
                "title" : "About DUBAI",
                "rasm" : "img/rasm1.jpg",
                "description" : "Dubai (/duːˈbaɪ/, doo-BY; Arabic: دبي, romanized: Dubayy, IPA: [dʊˈbajj], Gulf Arabic pronunciation: [dəˈbaj]) is the most populous city in the United Arab Emirates (UAE) and the capital of the Emirate of Dubai, the most populated of the 7 emirates of the United Arab Emirates.[7][8][9] Established in the 18th century as a small fishing village, the city grew rapidly in the early 21st century with a focus on tourism and luxury,[10] having the second most five-star hotels in the world,[11] and the tallest building in the world, the Burj Khalifa, which is 828 metres (2,717 ft) tall.[12]"
            },

            {
                "text" : "Turkey",        
                "title" : "About TURKEY",
                "rasm" : "img/rasm2.jpg",
                "description" : "Turkey (Turkish: Türkiye Turkish pronunciation: [ˈtyɾcije]), officially the Republic of Türkiye (Turkish: Türkiye Cumhuriyeti [ˈtyɾcije dʒumˈhuːɾijeti] (listen)), is a transcontinental country located mainly on the Anatolian Peninsula in Western Asia, with a small portion on the Balkan Peninsula in Southeast Europe. It borders the Black Sea to the north; Georgia to the northeast; Armenia, Azerbaijan, and Iran to the east; Iraq to the southeast; Syria and the Mediterranean Sea to the south; the Aegean Sea to the west; and Greece and Bulgaria to the northwest. Cyprus is off the south coast. Most of the country's citizens are ethnic Turks, while Kurds are the largest ethnic minority.[4] Ankara is Turkey's capital and second-largest city; Istanbul is its largest city and main financial centre. "
            },
            {
                "text" : "Europe",        
                "title" : "About EUROPE",
                "rasm" : "img/rasm3.jpg",
                "description" : "Europe is a continent[a] comprising the westernmost peninsulas of Eurasia,[12][13] located entirely in the Northern Hemisphere and mostly in the Eastern Hemisphere. It shares the continental landmass of Afro-Eurasia with both Africa and Asia. It is bordered by the Arctic Ocean to the north, the Atlantic Ocean to the west, the Mediterranean Sea to the south, and Asia to the east. Europe is commonly considered to be separated from Asia by the watershed of the Ural Mountains, the Ural River, the Caspian Sea, the Greater Caucasus, the Black Sea and the waterways of the Turkish Straits.[14]"
            },
            {
                "text" : "Unites States of America",        
                "title" : "About  USA",
                "rasm" : "img/rasm4.jpg",
                "description" : "The United States of America (U.S.A. or USA), commonly known as the United States (U.S. or US) or America, is a country primarily located in North America. It consists of 50 states, a federal district, five major unincorporated territories, nine Minor Outlying Islands,[i] and 326 Indian reservations. The United States is the world's third-largest country by both land and total area.[c] It shares land borders with Canada to its north and with Mexico to its south and has maritime borders with the Bahamas, Cuba, Russia, and other nations.[j] With a population of over 333 million,[k] it is the most populous country in the Americas and the third most populous in the world. The national capital of the United States is Washington, D.C., and its most populous city and principal financial center is New York City. "
            },
    ]

    context = {

        'content' :content

    }
    return render(request , 'home.html' , context)

    
