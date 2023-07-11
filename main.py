import requests
import datetime

#creating a new account
pixela_endpoint = "https://pixe.la/v1/users"
user_data_to_post={
    "token": "somethingrandom",
    "username": "donasussan",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=pixela_endpoint, json=user_data_to_post)

USERNAME = "donasussan"
TOKEN =  "somethingrandom"

graph_config = {
    "id" : "graph1",
    "name" : "My Coding Graph",
    "unit" : "hr",
    "type": "float",
    "color": "ajisai"

}
header = {
    "X-USER-TOKEN" : TOKEN
}



#creating a new graph
graph_endpoint = "https://pixe.la/v1/users/donasussan/graphs"
#parameters for graph : id, name, unit(kg/calory, pages), data type, color of pixels in japanes
#response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
#print(response.text)
hours = input("How many hours did you spend to code?")
#marking a new pixel on pixela using http post request
today = datetime.datetime.now()
date = today.strftime("%Y""%m""%d")

pixel_posting_endpoint = "https://pixe.la/v1/users/donasussan/graphs/graph1"
pixel_params ={
    "date": date,
    "quantity": f"{hours}"
}
print("Added today's data!")

response = requests.post(url=pixel_posting_endpoint,json=pixel_params,headers=header)

print("Added today's data!")
#UPDATING A PIXEL
#pixel_UPDATE_endpoint = f"https://pixe.la/v1/users/donasussan/graphs/graph1/{date}"
#update_parameter ={
 #   "quantity": f"{hours}"
#}
#response = requests.put(url=pixel_UPDATE_endpoint,headers=header, json=update_parameter)


#DELETING A PIXEL
#pixel_delete_endpoint = f"https://pixe.la/v1/users/donasussan/graphs/graph1/{date}"
#response = requests.delete(url=pixel_delete_endpoint,headers=header)
