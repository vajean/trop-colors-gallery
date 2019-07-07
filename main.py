import datetime
from flask import Flask, render_template, request, url_for
import os


def getProjects():
    basepath = 'templates/projects/'
    projects = {}
    project = {}
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            for page in os.listdir(os.path.join(basepath, entry)):
                if page == 'index.html':
                    project = {
                        'link': '/' + entry,
                        'thumbSrc': '/templates/projects/' + entry + '/img/thumb.png'
                    }
                    projects[entry] = project
    return projects


def checkSubfolder(folder):
    ext = {
        'js': 'js/',
        'jpg': 'img/',
        'jpeg': 'img/',
        'png': 'img/',
        'css': 'style/',
        'ico': ''
    }
    return ext.get(folder, 'other/')


app = Flask(__name__, static_folder='templates')


@app.route('/<folder>', methods=['GET'])
def page(folder):
    project = str(request.referrer).split('/').pop()
    try:
        return render_template('/projects/' + folder + '/index.html')
    except:
        return open('templates/projects/' + project + '/' + folder, 'rb').read()


@app.route('/<folder>/<file>', methods=['GET'])
def resouce(folder, file):
    project = str(request.referrer).split('/').pop()
    if project:
        project = '/' + project
    if folder:
        folder = '/' + folder
    if file:
        file = '/' + file

    return open('templates/projects' + project + folder + file, 'rb').read()


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    projects = getProjects()
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
