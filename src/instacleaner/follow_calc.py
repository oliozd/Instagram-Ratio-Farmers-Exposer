# Following script includes: Reciprocracy Checker
import json

def follower_reciprocracy(data_dir):
  #Follower data
  with (data_dir / "followers_1.json").open(encoding="utf-8") as file:
    followers_data = json.load(file)
    
  #Following data
  with (data_dir / "following.json").open(encoding="utf-8") as file:
    following_data = json.load(file)

  followers = []
  following = []

  for entry in following_data["relationships_following"]:
    following.append(entry["title"])
  for entry in followers_data:
    followers.append(entry["string_list_data"][0]["value"])


  follower_set = set(followers)
  non_reciprocated = []

  #Check for non-reciprocations and isolate them
  for follow in following:
    if follow not in follower_set:
      non_reciprocated.append(follow)

  print("People who do not follow you back:")
  print("length: ", len(non_reciprocated))
  for nr in non_reciprocated:
    print(nr)