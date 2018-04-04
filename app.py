from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from random import randint #debug

app = Flask(__name__)
Bootstrap(app)

websiteTitle = "Connor Parrish's Portfolio"
address = "Gameplay, Tools, and Networking Engineer "

# This random int is used to debug in chrome without worrying about the browser's cache.
random_debug = randint(0, 10000)


@app.route('/')
def index():
    name = ["Connor", "Parrish"]
    bio = "I am a programmer"
    fb_link = "http://facebook.com/ConnorParrish"
    linkedin_link = "http://linkedin.com/in/connor-parrish"
    git_link = "http://github.com/ConnorParrish"

    experience = fill_in_experience()
    projects = fill_in_projects()
    education = fill_in_education()

    return render_template('index.html', rand_debugging=random_debug, first_name=name[0], last_name=name[1],
                           website_title=websiteTitle, address=address, phone_number="(317)501-4121",
                           email="me@connorparrish.net", bio=bio, experience_block=experience, project_block=projects,
                           education_block=education, fb_link=fb_link, linkedin_link=linkedin_link, git_link=git_link)


def fill_in_experience():
    experience = experience_builder("Gameplay Engineer", "Stratus Softworks", "February 2018 - Present",
                                     "Working with a subteam of 8 programmers to develop gameplay features from " +
                                     "documentation within <b>Unity 3D</b>")
    experience += experience_builder("Networking Engineer", "Clever Girl LLC", "February 2018 - Present",
                                     "Developing a dedicated server for a multiplayer survival looter-shooter within " +
                                     "<b>Unreal Engine 4.</b>")
    return experience


def fill_in_projects():
    projects = projects_builder("Toggle", "Unity 3D", "Gameplay, UI, Animation", "5", "Challenging side-scroller " +
                                 "taking inspiration from The Impossible Game. I developed the logic for " +
                                 " save states, animation state-machines, and all gameplay mechanics. The team " +
                                 " consisted of 2 artists, 1 designer, and 1 other programmer. Available now on the " +
                                 "Google Play Store.")
    projects += projects_builder("Drifer: The Game", "Unity 3D", "Gameplay, UI, Animation", "5", "Top-down, point-n" +
                                 "-click survival alternative game, where the player lives the life of a homeless " +
                                 "man in Salt Lake City. I developed all gameplay mechanics, NPC interactions, " +
                                 "inventory system, vendor system, camera movement, stat system, and animation " +
                                 " programming. This team consisted of 2 artists, 1 producer, and 1 other " +
                                 "programmer")
    projects += projects_builder("Cubed", "Unity 3D", "Gameplay, Design, UI", "1", "An isometric puzzle platformer " +
                                 "with inspiration from Portal and M.C. Escher's 'Ascending and Descending.' " +
                                 "Original game created for Ludum Dare 37 in a weekend. In that amount of time, " +
                                 "I developed moving platforms, character controls, interactive environments, and " +
                                 "the puzzles playable on Itch.io")
    return projects


def fill_in_education():
    education = education_builder("University of Utah", "Bachelor of Computer Science", "Emphasis in Entertainment" +
                                   "Arts and Engineering", "Graduating: May 2019")

    return education

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


def projects_builder(gameTitle, engine, roles, teamSize, description):
    project_block = '''<div class="resume-item d-flex flex-column flex-md-row mb-5">
            <div class="resume-content mr-auto">
              <h3 class="mb-0">%s - %s</h3>
              <div class="subheading mb-3">Roles: %s</div>
              <div class="subheading mb-3">Team size: %s</div>
              <p>%s</p>
            </div>
            <div class="resume-date text-md-right">
              <span class="text-primary">%s</span>
            </div>
          </div>
          ''' % (gameTitle, engine, roles, teamSize, description, "")

    return project_block

def education_builder(school, degree, information, graduation_date):
    education_block = '''<div class="resume-item d-flex flex-column flex-md-row mb-5">
            <div class="resume-content mr-auto">
              <h3 class="mb-0">%s</h3>
              <div class="subheading mb-3">%s</div>
              <div>%s</div>
            </div>
            <div class="resume-date text-md-right">
              <span class="text-primary">%s</span>
            </div>
          </div>
          ''' % (school, degree, information, graduation_date)

    return education_block


if __name__ == '__main__':
    app.run()
