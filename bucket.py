def blobList(blob):

    blobstrign = blob.name
    indexL = blobstrign.find('/')
    indexR = blobstrign.rfind('/')
    project = blobstrign[0:indexL]
    file = blobstrign[indexR + 1:]
    path = blobstrign[indexL:indexR]

    return [file, path, project]


def getProjects(blobs):
    projects = []
    for blob in blobs:
        project = blobList(blob)[2]
        if project not in projects:
            projects.append(project)
    return projects


def getFiles(projects, blobs):
    structure = {}
    for blob in blobs:
        for project in projects:
            structure[project] = {}
            index = 0
            for blob in blobs:
                blob = blobList(blob)
                if blob[2] == project:
                    structure[project][blob[0]] = [blob[1], index]
                index += 1
    return structure
