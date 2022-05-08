import json
from pathlib import Path
import os


dir = os.path.join(Path(__file__).parent, 'database')


if not os.path.exists(dir + '\data.json'):
    with open(dir + '\data.json', 'w') as file:
        json.dump([], file, indent=True)



if not os.path.exists(dir + '\\auth.json'):
    with open(dir + '\\auth.json', 'w') as file:
        json.dump({}, file, indent=True)


def setMaster(username, password):

    with open(dir + '\\auth.json', 'r') as file:
        data = json.load(file)

        if data == {}:
            data["username"] = username
            data["password"] = password
            data["username"] = "out"

            with open(dir + '\\auth.json', 'w') as file:
                json.dump(data, file, indent=True)

        else:

            return "err1"

def checkPassword(username, password):

    with open(dir + '\\auth.json', 'r') as file:
        data = json.load(file)

        if data["username"] == username and data["password"] == password:
            return True

        return False



class Task(object):

    def __init__(self,name, tag, deadline, importance):
        self.name = name
        self.tag = tag
        self.deadline = deadline
        self.importance = importance

    def rep(self):
        return {
            "name":self.name,
            "tag":self.tag,
            "deadline":self.deadline,
            "importance":self.importance

        }

def checkTaskExists(task: Task):
    mytask = task.rep()

    with open(dir + "\data.json", "r") as file:
        data = json.load(file)

        for i in data:
            if i == mytask:
                return True

        return False

def createTask(name, tag, deadline, importance):

    task = Task(name, tag, deadline, importance)

    with open(dir + "\data.json", "r") as file:
        data = json.load(file)
    
    if not checkTaskExists(task):
        with open(dir + "\data.json", "w") as file:
            data.append(task.rep())
            json.dump(data, file, indent=4)

        return "yes"
    else:
        return "err2"

def done(name):

    with open(dir + "\data.json", "r") as file:
        data = json.load(file)

        for i in data:
            if i['name'] == name:
                index = data.index(i)
                
                with open(dir + '\completed.json', 'r') as file:
                    data2 = json.load(file)

                    data2.append(i)

                    with open(dir + '\completed.json', 'w') as file:
                        json.dump(data2, file, indent=True)

                data.remove(data[index])

                with open(dir + "\data.json", "w") as file:
                    json.dump(data, file, indent=True)

                return "yes"
            else:
                return "err3"

def Return(taskname = None):

    with open(dir + "\data.json", "r") as file:
        data = json.load(file)

    if taskname == None:
        return data

    elif taskname != None:
        for i in data:
            if i['name'] == taskname:
                return i

def returnCompleted():
    
    with open(dir + '\completed.json', 'r') as file:
        data = json.load(file)

        return data

