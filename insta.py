from instagramy import InstagramUser as IU
# import json

givenUI = input("Enter a valid and existing instagram username: ")
unInstance = IU(givenUI)
instaBioDesc = unInstance.biography
instaBioFb_Page = unInstance.connected_fb_page
instaBioLinks = unInstance.website
instaBioJson = unInstance.get_json()

print("Description: ", instaBioDesc)
print("Facebook_Page: ", instaBioFb_Page)
print("Links: ", instaBioLinks)
print("Json: ", instaBioJson)

#TO get the .json file
# with open('you_ig_handle.json', 'r') as json_file:
#     json_loads = json.load(json_file)
    
# for x in json_loads:
#     print("%s: %s" %(x, json_loads[x]))
    
# with open('file.txt', 'w') as file:
#     file = file.write(json_loads[x])

# print(json_loads['username'][:100])
# print(json_loads['id'][:100]) 
# print(json_loads['edge_felix_video_timeline'])   
# print(json_loads['fbid'][:100])
# print(json_loads['edge_owner_to_timeline_media']['video_url'])

