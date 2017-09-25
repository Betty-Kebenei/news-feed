from urllib.request import urlopen
import json

def get_data():

    Post_Id = input("Enter Post Id:")
    post = input("Comment on Post: ")
    request_data = {"Post Id", Post_Id, "Post", post}
    url='http://34.207.10.230:3000/comments'
    req = request.Request(url,data=request_data)
   
    data=req.read().decode('utf')
    json_parse=json.loads(data)[0]
  

    print((post))

get_data()