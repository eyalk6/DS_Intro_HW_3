def read_line(num, file):
    try:
        file = open(file)
        count = 0
        if type(num)!=int:
            return "invalid input detected"
        for line in file:
            count = count + 1
            if count == num:
                return line
        if num > count:
            return "line " + str(num) + " doesn't exist"
    except:
        return "file not found"

def longet_words(file):
  try:
    mylist = []
    data = open(file)
    data = data.read()
    data = data.replace('.', ' ')
    data = data.replace('-', ' ')
    data = data.replace(',', ' ')
    cline = data.split()
    cline = sorted(cline, key=len, reverse = True)
    mylist = cline[0:5]
    return mylist
  except:
    return "file not found"

