from urllib import request, parse
import json

def create_post():
   url = 'http://34.207.10.230:3000/comments'
   post_Id = input("Enter Post Id\n")
   comment = input("Enter Comment\n")
   request_data = {'post_Id': post_Id, 'comment': comment}
   data = parse.urlencode(request_data).encode()
   req = request.Request(url, data=data)
   resp = request.urlopen(req)
   print(resp.__dict__)
create_post()