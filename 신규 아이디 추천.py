import re

def solution(new_id):
    new_id=new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]',"",new_id)
    new_id = re.sub('(([.])\\2{1,})', ".", new_id)
    if (new_id == ""):
        new_id = "a"

    if(new_id[0] == '.'):
        new_id = new_id[1:]
    if (new_id == ""):
        new_id = "a"
    if(new_id[len(new_id)-1] == '.'):
        new_id = new_id[:-1]
    if (new_id == ""):
        new_id = "a"
    new_id = new_id[:15]
    if (new_id == ""):
        new_id = "a"
    if (new_id[0] == '.'):
        new_id = new_id[1:]
    if (new_id == ""):
        new_id = "a"
    if (new_id[len(new_id) - 1] == '.'):
        new_id = new_id[:-1]
    if (new_id == ""):
        new_id = "a"

    while(len(new_id)<3):
        new_id = new_id + new_id[len(new_id)-1]

    return new_id