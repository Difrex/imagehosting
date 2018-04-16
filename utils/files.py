import os


# Return file string and filename
def get_file_from_request(request, fieldname):
    file_l = ''
    for i in request.FILES[fieldname]:
        file_l = file_l + i

    return file_l, str(request.FILES[fieldname])


# Write file to /dev/shm and return ar handler
def write_to_shm(file, name):
    f = open('/dev/shm/' + name, 'w')
    f.write(file)
    f.close()

    return '/dev/shm/' + name


# Remove file from /dev/shm
def rm_from_shm(name):
    try:
        os.remove('/dev/shm/' + name)
        return True
    except Exception as e:
        return str(e)


# Split filename
def split_file(filename):
	pass
