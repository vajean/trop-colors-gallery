from flask import Flask, render_template, request, render_template_string
from google.cloud import storage
from bucket import getFiles, getProjects

client = storage.Client()
bucket = client.get_bucket('projects-bucket')
blobs = bucket.list_blobs()
blobsList = list(blobs)
projects = getProjects(blobsList)
structure = getFiles(projects, blobsList)


app = Flask(__name__, static_folder='templates')


@app.route('/<path:path>', methods=['GET'])
def page(path):
    fullRequest = str(request.referrer).split('/')
    project = fullRequest.pop()
    if project != 'None' and project != '':
        file = path.split('/').pop()
        index = structure[project][file][1]
    else:
        if '/' in path:
            fullPath = path.split('/')
            file = fullPath.pop()
            path = fullPath.pop()
            project = fullPath.pop()
            index = structure[project][file][1]
        else:
            if '.' in path:
                return open('templates/projects/' + path, 'rb').read()
            else:
                index = structure[path]['index.html'][1]
                template = blobsList[index].download_as_string()
                return render_template_string(template.decode('utf-8'))

    return blobsList[index].download_as_string()


@app.route('/')
def root():

    client = storage.Client()
    bucket = client.get_bucket('projects-bucket')
    blobs = bucket.list_blobs()
    blobsList = list(blobs)
    projects = getProjects(blobsList)
    structure = getFiles(projects, blobsList)
    return render_template('index.html', structure=structure)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
