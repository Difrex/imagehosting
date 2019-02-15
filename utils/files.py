"""Work with files"""
import os


def get_file_from_request(request, fieldname):
    """ Return file string and filename
    :param request:
    :param fieldname:
    :return:
    """
    file_l = ''
    for i in request.FILES[fieldname]:
        file_l = file_l + i

    return file_l, str(request.FILES[fieldname])


def write_to_shm(file, name):
    """ Write file to /dev/shm and return ar handler """
    f = open('/dev/shm/' + name, 'w')
    f.write(file)
    f.close()

    return '/dev/shm/' + name


def rm_from_shm(name):
    """ Remove file from /dev/shm """
    try:
        os.remove('/dev/shm/' + name)
        return True
    except Exception as e:
        return str(e)
