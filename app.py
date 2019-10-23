from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from random import randint #debug

app = Flask(__name__)
Bootstrap(app)

websiteTitle = "Connor Parrish's Portfolio"
address = "Networking, Gameplay, and Tools Engineer"

# This random int is used to debug in chrome without worrying about the browser's cache.
random_debug = randint(0, 100000000)

project_count = 0

@app.route('/')
def index():
    name = ["Connor", "Parrish"]
    bio = "I am studying for my Bachelors degree in Computer Science at the University of Utah with an emphasis in" \
          " Entertainment Arts & Engineering. I aspire to be a prominent developer in the interactive entertainment " \
          "industry. <br><br> As an aspiring developer I have spent my time at the University of Utah familiarizing " \
          "myself with technology found within industry standards as well as innovating on what has been made. " \
          "Through projects in mobile development, VR, UWP, and general game development, I have found a place I " \
          "truly belong! My goal is to enrich other people's lives with the experiences I help to create."
    fb_link = "http://facebook.com/ConnorParrish"
    linkedin_link = "http://linkedin.com/in/connor-parrish"
    git_link = "http://github.com/ConnorParrish"

    experience = fill_in_experience()
    games = fill_in_games()
    tools = fill_in_tools()
    software = fill_in_software()
    education = fill_in_education()
    workflow = fill_in_workflow()
    leaderboard = fill_in_leaderboard()

    return render_template('index.html', rand_debugging=random_debug, first_name=name[0], last_name=name[1],
                           website_title=websiteTitle, address=address, phone_number="(317)501-4121",
                           email="me@connorparrish.net", bio=bio, linkedin_link=linkedin_link,
                           git_link=git_link, experience_block=experience, game_block=games, tools_block=tools,
                           software_block=software, education_block=education, workflow_block=workflow,
                           leaderboard_block=leaderboard)


def fill_in_experience():
<<<<<<< HEAD
    experience = experience_builder("IX Engineering Intern", "Roblox", "May 2018 - Present", "Created a tutorial for " +
                                    "creating Top-Down Twinstick Shooters in <b>Roblox Studio</b> for Roblox's " +
                                    "Education materials. Also added new content creation features for the IX " +
                                    "Documentation team for their new documentation website to enhance article " +
                                    "content.")

    # experience += experience_builder("Gameplay Systems Engineer", "Studio 73", "August 2018 - Present", "Developed " +
    #                                  "core time travel mechanic to Chronoraptor with <b>Unreal Engine 4</b> and the " +
    #                                  "timer system that designers and other programmers used to add features. " +
    #                                  "Character movement was stored as Vector3 arrays for velocity and position. " +
    #                                  "Character animations were Animation Snapshots saved as an array of integers.")

=======
    experience = experience_builder("IX Engineering Intern", "Roblox", "May 2018 - August 2018",
                                     "Created a tutorial for creating Top-Down Twinstick Shooters in <b>Roblox " +
                                     "Studio</b> for Roblox's Education materials. Also added new content creation " +
                                     "features for the IX Documentation team for their new documentation website " +
                                     "to enhance article content.")
>>>>>>> 3d97c9e0779e23408e9460918275a423eb4a51ff
    experience += experience_builder("Gameplay Engineer", "Stratus Softworks", "February 2018 - Present",
                                     "Working with a subteam of 8 programmers to develop gameplay features from " +
                                     "documentation within <b>Unity 3D</b>")
    experience += experience_builder("Networking Engineer", "Clever Girl LLC", "February 2018 - Present",
                                     "Developing a dedicated server for a multiplayer survival looter-shooter within " +
                                     "<b>Unreal Engine 4.</b>")
    return experience


def fill_in_games():
    games = games_builder("Chronoraptor", "Unreal Engine 4", "Gameplay Systems Engineer", "13", "Chronoraptor is a " +
                          "Game where the player needs to use time travel to solve puzzles with past versions of " +
                          "themselves in order to put an end to a time travelling raptor's thieving escapades. By " +
                          "rewinding time, players can replicate their actions in the exact moments they happen. " +
                          "My job in this project was to create the time travel system the game uses all the time. " +
                          "Using timers and events in Unreal Engine 4, I created a game loop that would poll the " +
                          "player, antagonist, and any other specified object in the scene and gather the object's " +
                          "position and velocity. The animated objects would also capture Snapshots of the animation " +
                          "pose and save them to an integer array. All animations and movement are able to be " +
                          "rewound or fast-forwarded. I also implemented a material that would display the outline " +
                          "of players, keycards, and artifacts when a part of them is behind the environment",
                          "Chronoraptor has been my favorite project to date in my experience. Building large systems " +
                          "is something that I enjoy participating on. The only thing that wasn't done was " +
                          "overflow protection for players who let the timer run on for too long. The best way to do " +
                          "this would be to create a failstate that triggers when the in-game stopwatch gets too high.",
                            ["https://steamcdn-a.akamaihd.net/steam/apps/1049000/ss_80ccf71a828a8aa30fecb676e21975466bd3550c.1920x1080.jpg?t=1557442133",
                             "https://steamcdn-a.akamaihd.net/steam/apps/1049000/ss_e49191b87f0d41eb5bead4bc27efb77cff37031f.1920x1080.jpg?t=1557442133",
                             "https://steamcdn-a.akamaihd.net/steam/apps/1049000/ss_9c511faf4bd3609ec06589e918e0db75a0e959b1.1920x1080.jpg?t=1557442133",
                             "https://steamcdn-a.akamaihd.net/steam/apps/1049000/ss_693ff848a4d5d8f7c143d1be69efc57c19dce59c.1920x1080.jpg?t=1557442133"])

    games += games_builder("Toggle", "Unity 3D", "Gameplay, UI, Animation", "5", "Run through the courses of a " +
                                "middle school student's composition notebook doodles. In this runner inspired by The " +
                                "Impossible Game, players are tasked to find a way to the end of the level. Along the " +
                                "way, they’ll face bricks, spikes, and an occasional coin!", "Toggle had been the " +
                                "first project I was able to dedicate serious time to. Through it I learned a lot " +
                                "about the Unity engine and developing for mobile games. I learned how to read " +
                                "serialized data, work with Unity’s UI, develop a game as a team, help manage a team, " +
                                "and publish a game on the Google Play Store.",
                            ["http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/TogglePlayStore.png",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/Toggle-LevelSelect.jpg",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/ToggleGameplay1.jpg"])
    games += games_builder("Drifer: The Game", "Unity 3D", "Gameplay, UI, Animation", "5", "Drifter is an " +
                                 "alternative game placing the player in the body of a homeless man in a city. The " +
                                 "player needs to rely on panhandling and scrounging for items around the world in " +
                                 "order to make a living enough to survive. If everything goes according to plan, " +
                                 "the player will gather enough money to be able to begin renting in an Income " +
                                 "Restricted apartment complex.", "This project was significantly more ambitious " +
                                 "than previous titles I have worked on and the team experienced feature creep " +
                                 "quickly through the 5 months it was developed. Difficulties aroused when team member's availablility fluctuated mid-project and my workload nearly doubled. " +
                                 "All of the tasks were completed by deadlines, however, even after taking on " +
                                 "the majority of programming tasks for a few weeks. This project taught me how to stay accountable " +
                                 "for other people’s work as Lead Programmer as well as how to structure large " +
                                 "gameplay systems, such as inventory management, survival-esque stat systems, and " +
                                 "in-game economies on a small scale.",
                            ["http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/01/Drifter-1.png",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/01/Drifter-5.png",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/01/Drifter-6.png"])
    games += games_builder("Cubed", "Unity 3D", "Gameplay, Design, UI", "1", "An isometric puzzle platformer " +
                                 "with inspiration from Portal and M.C. Escher's 'Ascending and Descending.' " +
                                 "Original game created for Ludum Dare 37 in a weekend. In that amount of time, " +
                                 "I developed moving platforms, character controls, interactive environments, and " +
                                 "the puzzles playable on Itch.io", "",
                            ["http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/Cubed-Gameplay1.png",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/Cubed-Gameplay3.jpg",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/Cubed-Gameplay2.jpg",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/Cubed-Gameplay4.gif",
                             "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2017/04/Cubed-Gameplay5.jpg"])
    return games


def fill_in_tools():
    tools = tools_builder("NPC Dialogue System", "Unity 3D", "Designers are able to use this tool to create spanning " +
                          "dialogue options for NPCs. Customization includes NPC names, sprite, and an endless number " +
                          "of responses dependant on the player's dialogue selections. This was originally programmed " +
                          "to use JSON instead of Unity 3D's ScriptableObjects for portability's sake, but modified " +
                          "to match the requests of designers.", [
                              "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/04/Unity-DialogueSystem.png"])
    tools += tools_builder("NPC Builder", "Unity 3D", "Level designers can use this tool to create custom NPC's to " +
                           "fill their worlds. The 'Wealth Level,' 'Hat type,' and 'Lefthand Accessory' were the " +
                           "only assets I recieved for the project, so I build the wizard around that. The script " +
                           "will spawn the selected items on the bones of the newly created NPC. Since our NPC's " +
                           "were not high-fidelity models, artists could get away with the rigid animations in these " +
                           "spawned items would create.",
                           ["http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/04/drifter-npcbuilder.png"])
    return tools


def fill_in_software():
    software = tools_builder("App Pinner", "Windows 10", "Tired of your bland Windows 10 Start Menu? Pick and choose " +
                             "your own images to represent files, folders, programs, websites, or games on your PC. " +
                             "The program can automatically find your installed Steam, GOG, and Origin games (Uplay " +
                             "coming soon). Along with finding your games for you, App Pinner can also grab " +
                             "high-resolution images from the web to match your games!\n\nI built App Pinner because " +
                             "I wasn't happy with the tools other developers have already created for Windows 10.",
                             ["http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/04/apppinner.png",
                              "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/04/apppinner-full.png",
                              "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/04/apppinner-gamepicker.png",
                              "http://connorparrish.portfolio.s3.amazonaws.com/wp‑content/2018/04/apppinner-settings.png"])

    return software


def fill_in_education():
    education = education_builder("University of Utah", "Bachelor of Computer Science", "Emphasis in Entertainment " +
                                   "Arts and Engineering", "Graduating: May 2019")

    return education


def fill_in_workflow():
    workflow = workflow_builder(["Agile/Scrum Development", "Clearly documented, easily maintainable code",
                                 "Develop tools to make work easier, not harder", "Develop in osmosis"])
    return workflow


def fill_in_leaderboard():
    leaderboard = leaderboard_builder("All-Stars", ["Dark Souls", "The Witcher 3", "Assassins Creed: 2"])
    leaderboard += leaderboard_builder("Roleplaying Games", ["The Witcher 3", "Dark Souls", "Tombraider (2013)"])
    leaderboard += leaderboard_builder("First-Person Shooter", ["Destiny", "Halo: Reach", "Overwatch"])
    leaderboard += leaderboard_builder("Competitive Games", ["League of Legends", "Overwatch", "PlayerUnknown's Battlegrounds"])
    return leaderboard


def experience_builder(title, company, date_range, summary):
    experience_block = '''<div class="resume-item d-flex flex-column flex-md-row mb-5">
            <div class="resume-content mr-auto">
              <h3 class="mb-0">%s</h3>
              <div class="subheading mb-3">%s</div>
              <p>%s</p>
            </div>
            <div class="resume-date text-md-right">
              <span class="text-primary">%s</span>
            </div>
          </div>
          ''' % (title, company, summary, date_range)

    return experience_block


def games_builder(gameTitle, engine, roles, teamSize, description, post_mortem, image_urls, captions=[]):
    game_block = '''<div class="resume-item">
            <div class="row">
              <div class="resume-content col-lg-8">
                <h3 class="mb-0">{0} - {1}</h3>
                <article>
                  <h2 class="subheading mb-3">
                    <p>Roles: {2} <br>Team size: {3}</p>
                  </h2>
                  <p>{4}</p>
                  <p>{5}</p>
              
                </article>
              </div>
              <div class="resume-slides col-lg-4" style="margin-bottom:40px;">
                {6}
              </div>
            </div>
          </div>
          '''.format(gameTitle, engine, roles, teamSize, description, post_mortem, slideshow_builder(image_urls, captions))

    return game_block


def tools_builder(title, platform, description, image_urls, captions=[]):
    tools_block = '''<div class="resume-item">
                <div class="row">
                  <div class="resume-content col-lg-8">
                    <h3 class="mb-0">{0}</h3>
                    <article>
                      <h2 class="subheading mb-3">
                        <p>{1}</p>
                      </h2>
                      <p>{2}</p>
                    </article>
                  </div>
                  <div class="resume-date col-lg-4" style="margin-bottom:40px">
                    {3}
                  </div>
                </div>
              </div>
              '''.format(title, platform, description, slideshow_builder(image_urls))

    return tools_block


# TODO: Modals for closer look
# TODO: Set the image's size correctly
def slideshow_builder(image_urls, captions=[]):
    slide_container = '''<div class="container">
                           <div id="myCarousel" class="carousel slide" data-ride="carousel">
                             <!-- Indicators -->
                             <ol class="carousel-indicators">
                               {0}
                             </ol>
                             <!-- Wrapper for the slides -->
                             <div class="carousel-inner">
                               {1}
                             </div>
                           </div>
                         </div>
                         '''
    indicators = '''<li data-target="#myCarousel" data-slide-to="{0}"{1}></li>
                    '''
    slides = '''<div class="carousel-item{0}">
        <img class="img-fluid" src="{1}" alt="{2}">
      </div>
      '''

    indicators_block = ''''''
    slides_block = ''''''

    for i in range(0, len(image_urls)):
        if i == 0:
            slides_block += slides.format(" active", image_urls[i], i)
            indicators_block += indicators.format(i, ' class="active"')
        else:
            slides_block += slides.format("", image_urls[i], i)
            indicators_block += indicators.format(i, "")

    slide_container = slide_container.format(indicators_block, slides_block)

    return slide_container


def education_builder(school, degree, information, graduation_date):
    education_block = '''<div class="resume-item d-flex flex-column flex-md-row mb-5">
            <article>
              <div class="resume-content mr-auto">
                <h3 class="mb-0">%s</h3>
                <div class="subheading mb-3">%s</div>
                <div>%s</div>
              </div>
            </article>
            <div class="resume-date text-md-right">
              <span class="text-primary">%s</span>
            </div>
          </div>
          ''' % (school, degree, information, graduation_date)

    return education_block


def workflow_builder(workflow_elements):
    workflow_template = '''<li>
              <i class="fa-li fa fa-check"></i>
              {0}</li>'''
    workflow_block = ''''''

    for element in workflow_elements:
        workflow_block += workflow_template.format(element)

    return workflow_block


def leaderboard_builder(category, games):
    leaderboard_block = '''<h3 class="mb-0">{0}</h3>
                           <ul class="fa-ul mb-0">
                             {1}
                           </ul>
                           <br>
                           '''#.format("1", "5")

    leaderboards = '''<li>
                        <i class="fa-li fa fa-trophy" style="color:#ffc107"></i>{0}</li>
                      <li>  
                        <i class="fa-li fa fa-trophy" style="color:#979590"></i>{1}</li>
                      <li>  
                        <i class="fa-li fa fa-trophy" style="color:#886533"></i>{2}</li>
                      '''.format(games[0], games[1], games[2])

    return leaderboard_block.format(category, leaderboards)


if __name__ == '__main__':
    app.run()
