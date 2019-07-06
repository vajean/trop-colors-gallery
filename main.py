import datetime
from flask import Flask, render_template, request
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
        'css': 'style/'
    }
    return ext.get(folder, 'other/')


app = Flask(__name__, static_folder='templates')


@app.route('/<file>', methods=['GET'])
def page(file):
    project = str(request.referrer).split('/').pop() + '/'
    folder = checkSubfolder(str(file).split('.').pop())

    try:
        return render_template('/projects/' + file + '/index.html')
    except:
        return render_template('/projects/' + project + folder + file)


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
