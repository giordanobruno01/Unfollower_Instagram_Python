import json
class unfollower:
    def loadJson(self):
        
        self.followers = json.load(open("followers_1.json"))
        self.following = json.load(open("following.json"))
        # print(self.followers)
    
    def extractFollowers(self):
        self.followersList =[]
        self.f1 = []
        for i in self.followers:
            self.followersDic = i #storing each dictionary item from the main list of the dictionary file
            self.followersDic = self.followersDic["string_list_data"]#selecting string list data from dictionary of three items
            self.followersDic = self.followersDic[0]#inside string list data there is one dictionary so 0 is used to get the single dictionary
            self.followersDic = self.followersDic["value"]#inside the dictionary the value contain the user name
            self.f1.append(self.followersDic)
            # print(self.followersDic)

    def extractFollowing(self):
        self.f2 = []
        self.followingList = self.following["relationships_following"]
        
        for i in self.followingList:
            self.followingList = i["string_list_data"]
            self.followingList = self.followingList[0]
            self.followingList = self.followingList["value"]
            self.f2.append(self.followingList)
        # print(self.f2)
            
    def compare(self):
        notFollowingBack =[]
    
        for i in range(len(self.f2)):
            if self.f2[i] not in self.f1:
                notFollowingBack.append(self.f2[i]) 
        for i in range(len(notFollowingBack)):    
            print(notFollowingBack[i], " is not following you back")   


obj = unfollower()
obj.loadJson()
obj.extractFollowers()
obj.extractFollowing()
obj.compare()
