from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

activity_id=30
activities=[
    {
        "id":"1",
        "name":"Go to orgo Night",
        "img":"https://arc-anglerfish-arc2-prod-spectator.s3.amazonaws.com/public/TL6NW4B24JBOVKG2JOMYS3JJL4.jpg",
        "text":" Orgo Night is held on the day before the Organic Chemistry exam, which is always on the first day of finals. At precisely the stroke of midnight, the Columbia University Marching Band occupies Room 209 (the main reading room) of Butler Library to distract diligent students from studying - in fact, one of its legendary purposes is to lower the curve of the Orgo exam. Despite the commotion, at least some students attempt to study through the event.Though the performance doesn't begin until midnight, early arrival is recommended as students begin to file in and claim prime spaces in the room as early as 20 to 25 minutes ahead of time.",
        "rating":"3.5",
        "alums":[[True, True, True],["John Jay", "Maggie Mead", "Alexander Hamilton"]],
    },
    {
        "id":"2",
        "name":"Take the swim test the day before graduation",
        "img":"https://gocolumbialions.com/images/2019/7/8/20160421DodgeFitnessCenter_0276.jpg?width=1000&height=563&mode=crop",
        "text":"The swim test is a bizarre Columbia College graduation requirement, shared with Cornell, Dartmouth, and MIT.The requirement at Columbia is three lengths of the pool using any stroke.The pool has open hours Monday through Friday 12-2pm, and 7-9:30pm, and 12-5 & 7-9 Saturday, 1-5, 7-9 Sunday. If individual instruction is needed consider joining beginner's swimming or lap swimming as a PE class, or contact a member of either the men's or women's Swimming Team who are qualified to teach swim lessons. The Beginner's Swimming course also fulfills the requirement, so if you take it and still, by the end, cannot swim, you do not have to take the swim test.",
        "rating":"5",
        "alums":[[True, True, True],["Roone Arledge", "Martha Stewart", "Diana Vagelos"]],
    },
    {
        "id":"3",
        "name":"Wade in the Columbia fountains",
        "img":"https://i.redd.it/obtg1rn6v8x11.jpg",
        "text":"The fountains on Low Plaza were first erected a long time ago, thanks, probably, to the donation of some class. Since then, they have almost become symbols of the school. They only rarely come into action; they get turned on at commencement and other large-scale events. Some say they are phallic or even misogynistic symbols, but no one knows for sure. Once, someone put soap into one of the fountains, cause its spray to turn all white and frothy. However, the university was quick to clean up the scene",
        "rating":"4",
        "alums":[[True, True],["Zora Hurston", "Isaac Asimov"]],
    },
    {
        "id":"4",
        "name":"Eat a slice of Koronet pizza",
        "img":"https://assets.dnainfo.com/generated/photo/2012/12/cleon-minakas-of-koronet-pizza-13545387409996.JPG/extralarge.jpg",
        "text":"Koronet Pizza or just Koronets is a legendary local pizza parlor on Broadway at 110th St.Koronets mainly doles out oversize jumbo slices for $3.75 each. The pizza has an inoffensive, even tasteless tomato sauce and crispy-on-the-outside-chewy-on-the-inside crust. There is so much grease that a slice can melt its way through a brown bag and slither onto the floor. Some people find it delicious. Others think it's just gross.",
        "rating":"3.5",
        "alums":[[True, True, True, True],["Thomas Merton", "Ruth Bader Ginsburg", "Barack Obama"]],
    },
    {
        "id":"5",
        "name":"Eat and get drunk with your Lit Hum professor",
        "img":"http://www.college.columbia.edu/core/sites/core/files/styles/top_image/public/anniversary.jpg?itok=XSt59qOz",
        "text":"Sing, Muse. Literature Humanities is popularly known as Lit Hum . Officially, it's called Masterpieces of Western Literature and Philosophy.The course is a central part of the Core Curriculum and is taken by all Columbia College first years. The first semester covers mainly Greek literature, with some Bible-stuff at the end. The second semester starts with Virgil and ends with Virginia Woolf. For your convenience, we have prepared a \"lite\" guide to the course (see below). That said, you probably won't get most of it until you've actually done the reading.",
        "rating":"4",
        "alums":[[True, True, True],["Robert Livingston", "Lou Gehrig", "Richard Rodgers"]],
    },
    {
        "id":"6",
        "name":"Explore the tunnels.",
        "img":"http://www.wikicu.com/images/thumb/8/8a/TunnelSystem.png/541px-TunnelSystem.png",
        "text":"Columbia has an extensive tunnel system connecting most buildings on campus and acting as conduits for steam, electricity, telecommunications, and other infrastructure. The tunnels are a mysterious, foreboding place fully explored only by legendary figures in campus history. They are rumored to be where unspeakable acts of pure horror are committed.",
        "rating":"5",
        "alums":[[True, True, True],["Joseph Engelberger", "Twyla Tharp", "Edwin Armstrong"]],
    },
    {
        "id":"7",
        "name":"Watch the Varsity Show all four years.",
        "img":"https://artsinitiative.columbia.edu/sites/default/files/events/images/varsity_0.jpg",
        "text":"The Varsity Show, founded in 1894 as a fundraiser for the university's fledgling athletic teams, is one of the university's oldest traditions, and certainly its oldest performing arts tradition. Every year, the Varsity Show produces a unique full-length show that skews and satirizes many aspects of life at Columbia. And every year, students, administrators, and many more members of the Columbia community pack Roone Arledge Auditorium to engage in the century-old tradition of the Varsity Show.Ironically, many of the administrators being parodied and lambasted are often sitting in the front rows of the audience. No study has been conducted to determine whether these administrators realize there's a reason they're being ridiculed on stage.",
        "rating":"4",
        "alums":[[True, True],["Amelia Earhart", "Nicholas Butler"]],
    },
    {
        "id":"8",
        "name":"Go to the campus tree-lighting ceremony",
        "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Collegewalk2.jpg/220px-Collegewalk2.jpg",
        "text":"The Tree Lighting Ceremony is an annual event held just before finals week in early December celebrating the illumination of the lights decorating the trees lining College Walk. The lights remain on until the end of February. To be specific, these are the trees between Kent and Hamilton on the east side of College Walk, and Dodge and Journalism Halls on the west.The event is centered around the Sundial, and features free hot chocolate, roasted chestnuts, performances by various groups, and speeches by the university president and a guest. At the end of the ceremony, the president pushes the switch to turn on the lights. Supposedly the podium with a big red switch is just for show, and the actual switching is coordinated by walkie-talkies.",
        "rating":"5",
        "alums":[[True],["Ferris", "Diana", "Obama"]],
    },
    {
        "id":"9",
        "name":"Forget to transfer at 96th Street and end up in central Harlem",
        "img":"https://upload.wikimedia.org/wikipedia/commons/a/a8/96th_Street_IRT_Broadway_1.JPG",
        "text":"The New York City Subway was designed by Columbia-educated engineer William Barclay Parsons in the 19th century, and looks as if it hasn't been upgraded much since. Still, it's the easiest and most economical means for getting around NYC should you be one of the brave souls who dare venture beyond Morningside Heights. The current base fare is $2.75 per ride. (Don't complain since in London the base fare is £4, or $8.) MetroCards are required for entry and can be purchased with cash, credit, and debit cards at any station.Occasionally, the subway stops running between 96th Street and 137th Street. It sucks when this happens.",
        "rating":"4",
        "alums":[[True, True, True],["Arthur Sulzberger", "Mortimer Adler", "William Parsons"]],
    },
    {
        "id":"10",
        "name":"Find the owl on Alma Mater",
        "img":"https://upload.wikimedia.org/wikipedia/commons/a/ac/2014_Columbia_University_Alma_Mater_closeup.jpg",
        "text":"Alma Mater is literally the mother soul of the college/university. In the context of Columbia, Alma Mater almost always means the Daniel Chester French sculpture that graces the steps to Low Library.It was a gift of Mrs. Robert Goelet and Robert Goelet Jr. in memory of Robert Goelet, Columbia College Class of 1860, and presented in 1903.Alma Mater was originally intended to be gilded, but never was. The bronze eventually oxidized and the statue was instead coated and sealed.Rumor has it that back-up Alma Maters are kept at the ready should need arise.An owl is hidden in the folds of Alma Mater's robes. According to legend, the first student of each College class to find the owl would graduate Valedictorian and marry a Barnard woman (back when Columbia College was still all-male.)",
        "rating":"5",
        "alums":[[True, True, True],["John Kluge", "Eddie Collins", "Max Lincoln"]],
    },
    {
        "id":"11",
        "name":"Take Freedom of Speech and Press with Bollinger",
        "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Lee_Bollinger_-_Daniella_Zalcman_less_noise.jpg/1200px-Lee_Bollinger_-_Daniella_Zalcman_less_noise.jpg",
        "text":"Once, in his spare time, he did something important involving law and affirmative action. Now, he mostly teaches undergrads how to behave like law students, luring them with a class on free speech, where he exercises Socratic Terror to compel debates that are still 1000 times more interesting than anything most actual lawyers do.PrezBo also promotes physical fitness, inaugurating the 5K Fun Run. The event, which occurs in September every fall, features free t-shirts and is led by PrezBo himself.",
        "rating":"4",
        "alums":[[True],["Richard Simon"]],
    },
    {
        "id":"12",
        "name":"Go to midnight breakfast",
        "img":"https://www.montclair.edu/responsive-media/cache/cdn/calendar/2016-12-07-midnight-breakfast.gif.3.1x.generic.jpg",
        "text":"Midnight Breakfast is a somewhat new Barnard College semi-annual tradition. It is held in the LeFrak Gymnasium during the finals weeks of the fall and spring semesters. At midnight, the college's deans, academic department heads, board of trustees chair, and president don chef hats and spatulas. For the remainder of the early morning, they are employed as servers for a breakfast buffet available to undergraduate students at both Barnard College and Columbia University.Menu items include French toast, pancakes, potatoes, waffles, muffins, bacon, sausage, a variety of cakes, and fruit. A separate Kosher section is also available.Midnight Breakfast is an excellent stop to make after attending Orgo Night.",
        "rating":"5",
        "alums":[[True, True, True, True],["Katy Bilodeaux", "Daniel Edelman", "Anna Quindlen", "Emanuel Celler"]],
    },
    {
        "id":"13",
        "name":"Go to a Bacchanal concert",
        "img":"https://arc-anglerfish-arc2-prod-spectator.s3.amazonaws.com/public/BBZCJNPVYZCUVOV24NG23ZXE34",
        "text":"Bacchanal is a student-run organization under ABC that plans a variety of events, including Columbia's premiere annual spring festival, Concert on the Steps, among other projects like carnivals, parties and more. It is organized by Bacchanal Events.The spring concert is a free concert on the steps of Low open to undergraduate Columbia ticket-holders. Its aim is to increase school spirit and release some of the students' stress before the end of the year exams. Past performers include: Macklemore, Big Sean, Snoop Dogg, Vampire Weekend, Kanye West, and Bob Saget. Before new restrictions placed in 2015, the spring concert was preceded by a week-long series of fun activities, such as a spring bbq, inviting food trucks onto college walk, and a public movie screenings on 4/20. The food trucks still make an appearance. Past themes have included 'Baccha90s', 'Abacchalypse', and 'Chewbacchanal'.",       "rating":"4",
        "alums":[[True, True, True],["Micheal Pupin", "Art Garfunkel", "Edward Rice"]],
    },
    {
        "id":"14",
        "name":"Do a trip with Urban New York",
        "img":"https://media.timeout.com/images/102991279/630/472/image.jpg",
        "text":"Urban New York is program organized every semester by the Division of Student Affairs for CC and SEAS. Students enter a lottery by ranking about 20 or so cultural events in order of preference. Spaces on these events are allocated to students in the order of their lottery number. The most coveted tickets are usually to Broadway shows, and dinner at Nobu Next Door.In the Fall semester, the lottery is only open to first-years; in the Spring semester, it is open to upperclassmen.",
        "rating":"5",
        "alums":[[True],["Max Frankel"]],
    },
    {
        "id":"15",
        "name":"Volunteer with Community Impact",
        "img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4PbjAOBfiw2q2Ny2NRA72aHCTt6KhAxnzln5HD1dH6n1MPLAA2A&s",
        "text":"Community Impact (CI) is a 501(c)3 nonprofit organization located at Columbia University. Community Impact (CI) serves community members from Harlem, Washington Heights, and Morningside Heights. Community Impact strives to provide high quality programs, advance the public good, and foster meaningful volunteer opportunities for students, faculty, and staff of Columbia University. CI provides food, clothing, shelter, education, job training, and companionship for residents in its surrounding communities. CI consists of a dedicated corps of about 950 Columbia University student volunteers participating in 25 community service programs, which serve more than 8,000 people each year. Community Impact has partnerships with more than 100 community organizations and agencies who do service work in the Harlem, Washington Heights, and Morningside Heights communities, including service organizations, social service offices, religious institutions, and schools. Many of these organizations refer their clients to Community Impact’s programs and work collaboratively to positively influence residents’ lives.",       "rating":"4",
        "alums":[[True, True],["Mary Antin", "James Fletcher"]],
    },
     {
        "id":"16",
        "name":"Go to frat row for parties",
        "img":"http://www.wikicu.com/images/thumb/5/58/04_05_38.JPEG/450px-04_05_38.JPEG",
        "text":"Frat Row is the stretch of 114th St between Broadway and Amsterdam where a lot of fraternities and sororities are located. Some also extend the definition to 113th St, where a number of other fraternity houses are located.Since Operation Ivy League cleared out Pi Kappa Alpha, Psi Upsilon, and Alpha Epsilon Pi—and the Brownstone Review Committee replaced them with Q House, Lambda Phi Epsilon, and Alpha Chi Omega—the 113th definition is gaining weight.",
        "rating":"5",
        "alums":[[True, True, True],["Jason Epstein", "Hamilton Fish", "Jhumpa Lahiri"]],
    },
    {
        "id":"17",
        "name":"Get a Broadway Shake at Tom's",
        "img":"http://www.wikicu.com/images/7/7b/Tomsdiner.jpg",
        "text":"Tom's Restaurant is a famous diner on Broadway at 112th St.It is internationally renowned as the Seinfeld Diner, because the exterior was used on that show. The interior was not, and is very different from that seen on the show. There is a portrait of Michael Richards's Kramer on the wall above the counter. It is not correctly referred to as Tom's Diner, despite the Suzanne Vega song by that name about this very restaurant.Barack Obama ate some breakfasts here during his first semester at the university. John McCain was also an enthusiastic patron when his daughter Meghan was studying at Columbia.",       "rating":"4",
        "alums":[[True, True, True],["Bennett Surf", "Barry Commoner", "Leon Cooper"]],
    },
     {
        "id":"18",
        "name":"Find your study spot in Butler",
        "img":"http://www.wikicu.com/images/1/16/Butler.jpg",
        "text":"Butler Library is Columbia's main library for undergraduate study and graduate research. It is named for longtime University President Nicholas Murray Butler, and holds 2 million volumes in the humanities. Butler has study rooms open 24 hours a day during the school year. Students in Butler tend to either work or spend time on Boredatbutler.com. Among its many facilities, Butler has a Blue Java outlet, a lounge (often used by students working on group assignments), and several computer labs.",
        "rating":"5",
        "alums":[[True, True],["Moran Weston", "Susan Stamberg"]],
    },
     {
        "id":"19",
        "name":"Learn the fight song",
        "img":"http://www.wikicu.com/images/2/27/Rahrah.jpg",
        "text":"Roar is Columbia's fight song and over time has become the song most closely associated with the school. When the Columbia University Alumni Federation offered up a prize for a new football song in 1923, Corey Ford CC '23 re-purposed a song from that years Varsity Show (which he co-wrote), and concocted new words for the final chorus of the show and sent the entry in. Thus did Bold, Buccaneers!become Roar, Lion Roar!In addition to crediting Ford for the lyrics, songbooks credit Roy Webb CC 1910 and Morris Watkins CC 1924 for the melody.",
        "rating":"5",
        "alums":[[True, True, True],["Herawati Diah", "Christiana Garcia", "Richard Wald"]],
    },
     {
        "id":"20",
        "name":"Ignore red flags on South Lawn and play football",
        "img":"https://arc-anglerfish-arc2-prod-spectator.s3.amazonaws.com/public/PX52AFUNWVHW5EFZNTUNFDK2AM",
        "text":"South Lawn refers to the two fields between Butler Library and College Walk. One gets to South Lawn from College Walk by descending the Rives Memorial Steps.Access to the fields is signaled by flags posted at the corner of the field. Green flags signal an open field, red signal closed. Sadly, the fields are almost always closed (or one of them is closed), as indicated by the red flags.",
        "rating":"5",
        "alums":[[True, True],["Arthur Burns", "Roald Hoffman"]],
    },
     {
        "id":"21",
        "name":"Participate in Take Back the Night",
        "img":"https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/21558562_1689556574402227_4211362697672099232_n.jpg?_nc_cat=107&_nc_sid=dd9801&_nc_ohc=8v8U_TlEAcoAX8Xhrtd&_nc_ht=scontent-lga3-1.xx&oh=8fced5966a8faf8424614f354678983c&oe=5E9A3105",
        "text":"Take Back the Night, often abbreviated to TBTN, is a march that takes place every April during which students protest sexual violence.In a reversal of the historical direction of sexual segregation, men were banned from taking part in the event for many years. Since 2008, they have been allowed to participate in the march, although they may not lead it.According to a group member, \"any woman or man from any undergraduate or graduate program of Columbia University can join Take Back the Night, or simply stop in and visit during our meetings\". Men interested in working on these issues with TBTN are also welcome to contact Columbia Men Against Violence.",
        "rating":"5",
        "alums":[[True],["Ellen Futter"]],
    },
    {
        "id":"22",
        "name":"Watch the \"Vagina Monologues\" on Valentine's Day",
        "img":"https://bwog.com/wp-content/uploads/2013/09/vday.jpg",
        "text":"The Vagina Monologues, or Project V-Day, are a theater group that perform annual feminist plays at Barnard.In 2013, they came under scrutiny for deciding to cast actors of color exclusively.Their press release stated:\"Barnard-Columbia V-Day is excited to announce that our annual production of The Vagina Monologues will feature an all self-identified women of color cast this year. This decision was made unanimously by the Barnard-Columbia V-Day board and is a product of both self-determination and allyship.",
        "rating":"5",
        "alums":[[True, True],["Edward Kendall", "Robert Stern"]],
    },
    {
        "id":"23",
        "name":"Watch/Take part in the naked run",
        "img":"https://www.nmnathletics.com/pics31/1024/RR/RRTGWANTIEGQPJO.20100921142141.jpg",
        "text":"The Naked Run is a hilarious annual event in which students take a nude dash down the steps of Low Library, around South Lawn, past Butler Library, and back up The Steps, all while singing the Columbia fight song, \"Roar, Lion, Roar\". The Naked Run is held every October. The runners are usually surrounded by a smattering of onlookers and photographers. The morning after the event, a select few runners have the fortune or misfortune of finding themselves in the pages of the Spectator.",
        "rating":"5",
        "alums":[[True, True, True],["Meyer Schapiro", "Norman Ramsey", "Lawrence Grossman"]],
    },
    {
        "id":"24",
        "name":"Read Orientalism",
        "img":"https://cup-us.imgix.net/covers/9780231187626.jpg?auto=format&w=350",
        "text":"Orientalism was a theory espoused by the late Columbia professor Edward Said, in a book of the same name, in 1978.It basically describes the stereotyping of \"Eastern\" peoples. There are various arguments and interpretations about to what extent and in what circumstances this phenomenon truly takes place, is dangerous, etc. Said's contention is that it both justified and enabled colonialism and latter-day practices that concern the projection of power.It is a concept that is batted around a lot in humanities classes, especially those in the MEALAC department, but has also been levelled as a charge against various features of campus life, including Cafe East and Cafe Nana.",
        "rating":"5",
        "alums":[[True, True],["Verginia Gildersleeve", "Marcellus Dodge"]],
    },
     {
        "id":"25",
        "name":"Fall over after Dance Marathon",
        "img":"http://www.wikicu.com/images/4/45/Dancemarathon1.jpg",
        "text":"Columbia University Dance Marathon is a 28-hour charity fund raising event held in Roone Arledge Auditorium, where participants must stay on their feet (and dance) for the duration of the event. The idea behind it is that the exhaustion that the human body feels from exerting that much energy without sleep, is to some degree comparable to the struggle facing those suffering from pediatric AIDS. Dancers are encouraged to invite their friends to the event and participate as moralers, as fatigue quickly sets in after the first few hours of line dancing and dodgeball.The event is usually held near the end of January, although the organizers begin planning for the event and dancers begin raising money early in the Fall Semester. Dance Marathon activities are not limited to the 28-hour dance",
        "rating":"5",
        "alums":[[True, True, True],["Irwin Edman", "Martha Nelson", "Robert Gottlieb"]],
    },
    {
        "id":"26",
        "name":"Hook up in the Butler stacks",
        "img":"https://arc-anglerfish-arc2-prod-spectator.s3.amazonaws.com/public/OU5VN4CTI5D4PNW2EYYJTNII3U",
        "text":"Butler Sex refers to the act of hooking up in Butler Library. Most hookups occur in the stacks after hours (\"staxxion\"), accessible through the basement. This much mythologized subculture of Columbia is driven by the unique pressurized scene that makes Butler a petri dish for desperate social interactions.Many a Butler hookup has been coordinated on Craigslist or on Bored at Butler.Having sex in the Butler stacks is one point of the Kings Quest challenge.",
        "rating":"5",
        "alums":[[True, True, True, True],["Edward Harris", "Eileen Ford", "John corigliano", "Katherine Boo"]],
    },
    {
        "id":"27",
        "name":"Be an Orientation Leader",
        "img":"https://www.cc-seas.columbia.edu/sites/dsa/files/styles/100_width/public/CC%202019.jpg?itok=59KMsuFt",
        "text":"The New Student Orientation Program takes up your first week at Columbia. There are no classes, but lots of events. Some of them are \"mandatory.\" None of them really are—NSOP is the last week you're treated like high school students, i.e. as if you really had to be anywhere. On account of some of the, ahem, extracurricular passtimes of NSOP prefrosh, the week is also known as NSLOP, as in, \"We got NSLOPPY last night.\"",
        "rating":"5",
        "alums":[[True, True],["Peter Barton", "David Horowitz"]],
    },
     {
        "id":"28",
        "name":"Go to a CB9 meeting",
        "img":"https://arc-anglerfish-arc2-prod-spectator.s3.amazonaws.com/public/4P7Z7HCS4ZGV5P6WAFV2SUZNEE.jpg",
        "text":"Community Board 9 (CB9) is the local government unit with jurisdiction over Columbia's planned Manhattanville campus. A vocal participant in the controversy over the development, it has generally reacted with hostility and/or skepticism toward the university's plans. Through the West Harlem Local Development Corporation, it is negotiating for more community benefits in exchange for closer cooperation.",
        "rating":"5",
        "alums":[[True, True],["Mark Wiles", "Atoosa Rubenstein"]],
    },
    {
        "id":"29",
        "name":"Use Arts Initiave to visit a museum",
        "img":"http://www.wikicu.com/images/8/8d/Ai_large_logo.gif",
        "text":"The Arts Initiative's website, the University's web compendium of campus and NYC arts information and resources, is now accessible directly from the Columbia University homepage. Over forty thousand visitors a month visit the site to link to Columbia's major arts schools, programs, organizations and venues, the Ticket and Information Center, listings of jobs/internships, arts libraries, campus rehearsal and performance venues, and much more. Through the Arts Initiative website, site visitors can sign up for the Arts Initiative's weekly newsletter, which goes out every Friday and provides a short list of on-campus and city-wide events for the upcoming week, normally for $20 or less.",
        "rating":"5",
        "alums":[[True, True, True],["Robert Merton", "Andrew Carroll", "Cliff Montgomery"]],
    },
     {
        "id":"30",
        "name":"Ride the Scholar's Lion",
        "img":"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT1CYl88CuyxmvGGpHoyEgni5L58GTeZbZ5n29aTF0H7193AhOn",
        "text":"The Scholar's Lion was gifted to the university by alumnus and sculptor Greg Wyatt. Presented on Dean's Day, April 3, 2004, in honor of Columbia's 250th anniversary, it depicts the Columbia Lion. Wyatt is sculptor in residence at the Cathedral of St. John the Divine[1]. The bronze lion resides in front of Mathematics and Havemeyer facing the Business School.",
        "rating":"5",
        "alums":[[True, True, True, True],["Brian De Palma", "James Lenox", "Lauryn Hill", "Eric Foner"]],
    },  


]

data=[]
@app.route('/')
def home_page():
    global activities
    global data
    data=activities[:-11:-1]
    return render_template('home.html', activities=activities, data=data)
   

@app.route('/search/<val>', methods=['GET', 'POST'])
def search(val):
    global activities 
    global data

    data=[]   
    print("val=",val)
    #chk if sent val is in name of activities
    
    val=val.lower()
    print(val) 
    for activity in activities:
        name=activity["name"].lower()
        text=activity["text"].lower()           
        if val in name or val in text:                           
            data.append(activity)
            ##print(toSend)
    data.append(val)  
    #send back the array of data, toSend so client can display
    return render_template("search.html", activities=activities, data = data)


@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id):
    global activities
    data=[]
    #print("inside view/id",id)
    ##print(activities)
    for activity in activities:
        i=str(activity["id"])
        ##print(i)
        ##print(id)
        if (i==id):
            #print("matched")
            data.append(activity)
    #print(data)
    return render_template('view.html', data=data)



@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('create.html')



@app.route('/createActivity', methods=['GET', 'POST'])
def createActivity():
    #print("reached createActivity")
    global activity_id
    global activities

    activity_id+=1
    json_data = request.get_json()   
    activity = json_data["new_activity"] 
    ##print(activity)
    activity["id"]=activity_id
    activities.append(activity)
    ##print(activities)
    data="http://127.0.0.1:5000/view/"+str(activity["id"])
    return jsonify(data=data)


@app.route('/delete_alum/<id>', methods=['GET', 'POST'])
def delete_alum(id):
    global activities
    global data
    i = request.get_json() 
    print("i in del=",i)
    #chk if sent val is in name of activities
    for activity in activities:        
        if (id==str(activity["id"])):   
            alums=activity["alums"][0]   
            
            alums[int(i)]=False
            print("alums",alums)
            #print("data",data)
        
    #send back the array of data, toSend so client can display
    return jsonify(activities = activities, data=data)

@app.route('/undo_delete_alum/<id>', methods=['GET', 'POST'])
def undo_delete_alum(id):
    global activities
    global data
    i = request.get_json() 
    print("i in del=",i)
    #chk if sent val is in name of activities
    for activity in activities:        
        if (id==str(activity["id"])):   
            alums=activity["alums"][0]           
            alums[int(i)]=True
            print("activities",activities)
            print("data",data)
        
    #send back the array of data, toSend so client can display
    return jsonify(activities = activities, data=data)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    global activities
    data=[]
    #print("inside edit/id",id)
    ##print(activities)
    for activity in activities:
        i=str(activity["id"])
        ##print(i)
        ##print(id)
        if (i==id):
            #print("matched")
            data.append(activity)
    #print(data)
    return render_template('editable.html', data=data)


@app.route('/submit_rating/<id>', methods=['GET', 'POST'])
def submit_rating(id):
    global activities
    data=[]
    #print("reached submit route,id=", id)
    edit = request.get_json() 
    #print(edit)
    for activity in activities:
        #print("activity id",activity["id"])        
        if (id==str(activity["id"])):
            #print("match") 
            activity["rating"]=edit["edits"]
            data=activity
            #print("activities",activities)
            #print("data",data)
    return jsonify(data=data)

@app.route('/submit_text/<i>', methods=['GET', 'POST'])
def submit_text(i):
    global activities
    data=[]
    #print("reached submit route,id=", id)
    edit = request.get_json() 
    #print(edit)
    for activity in activities:
        #print("activity id",activity["id"])        
        if (i==str(activity["id"])):
            #print("match") 
            activity["text"]=edit["edits"]
            data=activity
            #print("activities",activities)
            #print("data",data)
    return jsonify(data=data)





if __name__ == '__main__':
   app.run(debug = True)




