

def json_struc(data, t = 0):
    if type(data) is dict:
        print(' '*t + '{')
        for key in data:
            print(' '*t + '  ' + key + ':')
            json_struc(data[key], t+2)
        print(' '*t + '}')
    elif type(data) is list and len(data) > 0:
        print(' '*t + '[')
        json_struc(data[0], t+2)
        print(' '*t + '  ...')
        print(' '*t + ']')
