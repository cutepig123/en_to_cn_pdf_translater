import requests, copy

KEYS = {'key':'d9230248e8ce1080674b9b3151f790df', 'token':'b9d9942f8f015cf24cfa7f5088efe40b1abeb17e8def5d139bc15c932aee4c50'}

########### Test only 
def getBoards():
	url = "https://api.trello.com/1/members/me/boards"

	querystring = KEYS

	response = requests.request("GET", url, params=querystring)

	print(response.text)

def getBoardsInfo():
	url = "https://api.trello.com/1/boards/5be98f6bcefb55177342f294"

	querystring = KEYS

	response = requests.request("GET", url, params=querystring)

	print(response.text)

def getBoardsCards():
	url = "https://api.trello.com/1/boards/5be98f6bcefb55177342f294/cards"

	querystring = KEYS

	response = requests.request("GET", url, params=querystring)

	print(response.text)

def getBoardsLists(): #name
	url = "https://api.trello.com/1/boards/5be98f6bcefb55177342f294/lists"

	querystring = KEYS

	response = requests.request("GET", url, params=querystring)
	print(response.text)

def createList():
	url = "https://api.trello.com/1/lists"

	querystring = copy.deepcopy(KEYS)
	querystring.update({'idBoard':'5be98f6bcefb55177342f294', 'name':'test'})
	response = requests.request("POST", url, params=querystring)

	print(response.text)
	print (response.json()['id'])
	
########################
	
def getBoardsListIdByName(name):
	url = "https://api.trello.com/1/boards/5be98f6bcefb55177342f294/lists"

	querystring = KEYS

	response = requests.request("GET", url, params=querystring)
	
	response_json = response.json()
	for list in response_json:
		if list['name'] == name:
			return list['id']
	return None
	
def getBoardsCardIdByNamePrefix(namePrefix):
	url = "https://api.trello.com/1/boards/5be98f6bcefb55177342f294/cards"

	querystring = KEYS

	response = requests.request("GET", url, params=querystring)

	response_json = response.json()
	for list in response_json:
		if list['name'].startswith(namePrefix):
			return list['id']
	return None
	

	
def createListByName(name):
	url = "https://api.trello.com/1/lists"

	querystring = copy.deepcopy(KEYS)
	querystring.update({'idBoard':'5be98f6bcefb55177342f294', 'name':name})
	response = requests.request("POST", url, params=querystring)
	#print(response.text)
	return(response.json()['id'])
	
def createCard(cardListId, name):
	url = "https://api.trello.com/1/cards"

	querystring = copy.deepcopy(KEYS)
	querystring.update({'idList':cardListId, 'name':name})
	response = requests.request("POST", url, params=querystring)
	#print(response.text)
	return(response.json()['id'])
	
def updateCard(id, attr):
	url = "https://api.trello.com/1/cards/%s"%id

	querystring = copy.deepcopy(KEYS)
	querystring.update(attr)
	response = requests.request("PUT", url, params=querystring)
	#print(response.text)
	return(response.json()['id'])
	
#getBoards()
#getBoardsInfo()
#getBoardsCards()
#getBoardsLists()
#print (getBoardsListIdByName('1'))
#createList()
#createCard('5be999ff98691217d9955098', 'name')

if 1:
	issue1 = {'id':'1', 'name':'issue1-new name', 'assignee':'He JS', 'status':'in progress'}
	issue2 = {'id':'2', 'name':'issue2', 'assignee':'He JS', 'status':'done'}
	issue3 = {'id':'3', 'name':'issue3', 'assignee':'He JS', 'status':'new'}
	issues = [issue1, issue2, issue3]

	for issue in issues:
		print ('-----------')
		print (issue)
		
		listName = (issue['assignee'] + ' ' + issue['status'])
		listID = getBoardsListIdByName(listName)
		bCreateList = False
		if listID is None:
			listID = createListByName(listName)
			bCreateList = True
		print('Issue belong to list ', listID, 'New list?', bCreateList)
		
		cardName = '#%s %s'%(issue['id'], issue['name'])
		cardPrefix = '#%s '%(issue['id'])
		cardId = getBoardsCardIdByNamePrefix(cardPrefix)
		bCreateCard = False
		if cardId is None:
			cardId = createCard(listID, cardName)
			bCreateCard = True
		
		print('Issue belong to card ', cardId, 'New card?', bCreateCard)
	
		updateCard(cardId, {'name':cardName, 'desc':'desc'})
		