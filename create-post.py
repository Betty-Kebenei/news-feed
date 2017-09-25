from urllib import request, parse
import json

def create_post():
    url = 'http://34.207.10.230:3000/posts'
    message = input("Enter message\n")
    sender = input("Enter sender\n")
    receiver = input("Enter receiver\n")
    request_data = {'message': message, 'sender': sender, "receiver": receiver}
    data = parse.urlencode(request_data).encode()
    req = request.Request(url, data=data)
    resp = request.urlopen(req)
    print(resp.__dict__)
