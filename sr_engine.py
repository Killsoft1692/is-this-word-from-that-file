import os

def get_doc(d, value):
    for k, v in d.items():
    	if value in v:
            return k

directory =os.listdir('./docs')
for file in directory:
    # print (file)
    path_to_file = os.path.join('./docs', file)
    data = open(path_to_file).read()
    word = data.split()
    words = str(word)
    d = {file:words}
    print d
    print get_doc(d, 'ipsun')
	