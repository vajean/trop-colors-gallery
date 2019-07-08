from flask import Flask, render_template, request, redirect
from google.cloud import storage
from bucket import getFiles, getProjects

client = storage.Client()
bucket = client.get_bucket('projects-bucket')
blobs = bucket.list_blobs()
blobsList = list(blobs)
projects = getProjects(blobsList)
structure = getFiles(projects, blobsList)


app = Flask(__name__, static_folder='templates')


@app.route('/<folder>', methods=['GET'])
def page(folder):

    return blobsList[2].download_as_string()


#@app.route('/')
# def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

 #   projects=getProjects()
  #  return render_template('index.html', projects = projects)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
