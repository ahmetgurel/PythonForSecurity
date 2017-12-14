import hashlib

my_file = open("file.txt" , "r")

for line in my_file:
    try:
        hash_object = hashlib.md5(line.strip())
        print(hash_object.hexdigest())

    except:
        print "Error"

my_file.close()
