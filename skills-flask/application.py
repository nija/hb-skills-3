from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = "dfgnjnvfdjn"

'''
Part 1
Write a small Flask app in application.py that does the following:

* Serves the the template application-form.html at the route /application-form.
Use the application-form made in skills-html-css.

* Handles submission of a form in application-form.html to the route
/application.

    * Gets the first name, last name, salary, and job title from the form
    submission.

    * Returns a response that acknowledges their application. This should
    repeat their name, title, and salary requirement, like:

        Thank you, Jessica McHackbright, for applying to be a QA Engineer. Your
        minimum salary requirement is 89000 dollars.

    You should do this by using a Jinja template.
'''
'''
Part 2
Create a new template called base.html. Have your other two templates inherit
from base.html using Jinja's {% extends %} and {% block %} syntax.
'''



@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application-form")
def application_form():
    '''Serves the form data - woo, templates!'''

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application_process():
    '''Processes the form data'''

    # Nom nom eat the form data yum yum
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    salary = request.form.get('salary')
    job = request.form.get('job')

    # print "\n\n\t{}\t{}\n\t{}\t{}\n\n".format(
    #     first_name,
    #     last_name,
    #     salary,
    #     job)
#    import pdb; pdb.set_trace()

    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           salary=salary,
                           job=job)



if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run()






















