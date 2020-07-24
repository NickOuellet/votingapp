#Import civic info API
import urllib.request
import json

#DO NOT SHARE API KEY, IT NEEDS TO REMAIN CONFIDENTIAL
API_KEY = "AIzaSyDjXuTevzuE_i73cb99McIvHwr-bIBJaUU" #DO NOT HARDCODE IN FINAL PRODUCT

def voteInfoQuery(): #returns information relevant to a voter based on the voter's registered address
    voteInfoURL = "https://www.googleapis.com/civicinfo/v2/voterinfo" #location for google api query
    API_KEY_URL = "&key=" + API_KEY #puts key into a useful URL format

    address = input("Which address are you registered to vote with? (MSG from dev: Only New York addresses currently work, try 200 Park Ave): ").replace(" ", "+") #essential to replace spaces with '+' so that URL works properly
    addressUrl = "?address=" + address #puts address into a useful URL format

    TEST_ELECTION_ID = "2000" #only data that currently works with this API (not election season so no elections), must include or it breaks
    TEST_ELECTION_ID_URL = "&electionId=" + TEST_ELECTION_ID #puts into useful URL format

    requestURL = voteInfoURL + addressUrl + TEST_ELECTION_ID_URL + API_KEY_URL #creates complete URL

    voterRequest = urllib.request.urlopen(requestURL).read() #opens and loads site information into variable 'voterRequest'
    voterAnswer = json.loads(voterRequest) #parse json string into dictionary to make life easier

    return voterAnswer
    #end function

def electionQuery():#returns list of available elections to query
    electionQueryURL = "https://www.googleapis.com/civicinfo/v2/elections"
    API_KEY_URL = "?key=" + API_KEY

    requestURL = electionQueryURL + API_KEY_URL #creates unique URL

    electionRequest = urllib.request.urlopen(requestURL).read() #opens and loads site information into variable 'electionRequest'
    electionAnswer = json.loads(electionRequest) #parse json string into dictionary to make life easier

    return electionAnswer
    #end function

def unpackDictionary(d): #function that unpacks the nested dictionary that the api returns
    for key, value in d.items():
        if isinstance(value, list):#checks to see if the value of the first key is a list of dictionary entries
            print("This is a new list:")#used for testing
            for entry in value: #entry is a dictionary
                for k,v in entry.items():
                    print(k, ":", v)
                print("------------")#seperates each dictionary entry for neatness

        else: #NEED TO HANDLE NEXT CASE (CAN BE USED TO EXTRACT CANDIDATES LATER) UNFINIHSED
            pass
    #end function

#---------------------main------------------------#

            #uncomment to use functions, using both at same time is ugly
#unpackDictionary(voteInfoQuery())#ORGANIZES AND SENDS POLL LOCATIONS, REFERENDUMS, AND ELECTIONS (AND ALL OF THOSE RUNNING FOR OFFICE FOR EACH) TO STDOUT
#unpackDictionary(electionQuery())#ORGANIZES AND SENDS ALL THE KNOWN U.S. ELECTIONS TO STDOUT
