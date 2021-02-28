# PocketProfessor

### Inspiration
Scheduling can be difficult when there are so many classes and professor options available. Having all the information in one easily accessible location would make the process of selecting a class a lot simpler.

### What it does
PocketProfessor uses a discord bot to display the stats of a professor and their classes. Users pass a professor name and a desired class, and the bot will display the RateMyProfessor stats and the grade distribution of the class.

### How we built it
We used an API that holds data of RateMyProfessor and applied it for UTD professors. We used the API to access data that students typically look at such as overall rating and difficulty. To find grade distribution for classes, we used UTD-Grades json data available on the github https://github.com/bharatari/utd-grades. We used the json to compile all the sections of a specific course taught by a specific professor to find the grade distribution of all the classes.

### Challenges we ran into
webscraping vs finding and utilizing and API
understanding the process of discord bot and python (most members hadn't worked with either)
working with json data to narrow our searches further
debugging
Accomplishments that we're proud of
We were proud to create a working bot that accomplishes our desired functions.

### What we learned
We learned not only how to create a discord bot, but also gained an understanding of python and working with json data.

### What's next for PocketProfessor
We want to implement comparisons for PocketProfessor, so comparing two teacher stats will be a lot simpler

### Discord Link:
https://discord.gg/JcT3UyMj
