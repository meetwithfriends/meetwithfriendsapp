
# Endpoint list
> All calls except **signin** and **signup** should contain "token" parameter in header. 
> "token" value received in **signin** call response

### Sign-in
#### **POST** Sign in metod call example: 
>POST [YOUR_SERVER_ADDRESS/signin]
```JSON
Request:
{
    "email": "AwesomeUser@mail.com",
    "pass": "AwesomePass"
}
Response: 200 OK
{
    "email": "AwesomeUser@mail.com",
    "token": "F2D052C796A264A666EE76B5350EB7BE"
}
```
### Sign-Up
#### **POST** Sign up metod call example:
>POST [YOUR_SERVER_ADDRESS/signup]
```JSON
Request:
{
    "email": "AwesomeUser@mail.com",
    "pass": "AwesomePass"
}
Response: 200 OK
{
}
```
### Get current user's groups
#### **GET** groups metod call example:
> GET [YOUR_SERVER_ADDRESS/groups]

> Should contain "token" in header

>todo: add number of user in response, add avatar storage 
```JSON
Request:
{
}
Response: 200 OK
[
{   
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Awesome group",
    "creator_id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "note": "For awesome friends",
    "avatar": "https://{YOUR_SERVER_ADDRESS}/img/dummy.png"
}
]
```

### Create friends group
#### **POST** Create group metod call example:
> POST [YOUR_SERVER_ADDRESS/group]

> Should contain "token" in header 
```JSON
Request:
{
    "name": "Awesome group",
    "note": "For awesome friends",
    "avatar": ""
}
Response: 200 OK
{
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Awesome group",
    "creator_id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "note": "For awesome friends",
    "avatar": "https://{YOUR_SERVER_ADDRESS}/img/dummy.png"
}
```

### Get group's places
#### **GET** places metod call example:
> GET [YOUR_SERVER_ADDRESS/places/<group_id>]

> Should contain "token" in header

```JSON
Request:
{
}
Response: 200 OK
[
{   
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Dominos Pizza",
    "place_id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "address": "ukraine, Kyiv, 25 some str, ",
    "site": "www.dominos.com"
},
{   
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Some place",
    "place_id": "5b5a80f7-a66f-4733-999a-61630b49cfc9",
    "address": "ukraine, Kyiv, 11 High str, 24th floor",
    "site": "www.someplace.com"
}
]
```

### Add new place
#### **POST** place metod call example:
> POST [YOUR_SERVER_ADDRESS/place]

> Should contain "token" in header

```JSON
Request:
{
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Dominos Pizza",
    "address": "ukraine, Kyiv, 25 some str, ",
    "site": "www.dominos.com"
}
Response: 200 OK
{   
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Dominos Pizza",
    "place_id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "address": "ukraine, Kyiv, 25 some str, ",
    "site": "www.dominos.com"
}
```


### Get group's meal provider
#### **GET** provider metod call example:
> GET [YOUR_SERVER_ADDRESS/meal_providers/<group_id>]

> Should contain "token" in header

```JSON
Request:
{
}
Response: 200 OK
[
{   
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Dominos Pizza",
    "id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "address": "ukraine, Kyiv, 25 some str",
    "site": "www.dominos.com"
},
{   
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Some place",
    "id": "5b5a80f7-a66f-4733-999a-61630b49cfc9",
    "address": "ukraine, Kyiv, 11 High str, 24th floor",
    "site": "www.someplace.com"
}
]
```

### Add new provider
#### **POST** meal_provider metod call example:
> POST [YOUR_SERVER_ADDRESS/meal_provider]

> Should contain "token" in header

```JSON
Request:
{
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Dominos Pizza",
    "address": "ukraine, Kyiv, 25 some str, ",
    "note": "Always bring some sweets",
    "site": "www.dominos.com"
}
Response: 200 OK
{   
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Dominos Pizza",
    "id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "address": "ukraine, Kyiv, 25 some str",
    "note": "Always bring some sweets",
    "site": "www.dominos.com"
}
```


### Get group's meals
#### **GET** meals metod call example:
> GET [YOUR_SERVER_ADDRESS/meals/<group_id>]

> Should contain "token" in header

```JSON
Request:
{
}
Response: 200 OK
[
{   
    "id": "1cca84d6-3833-4854-bb80-3d06a342180e",
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Pizza with peperonni",
    "meal_provider_id": "b987d0ff-5edf-46dd-8c1a-e4511916d464",
    "img": ""
},
{   
    "id": "2767f978-7e48-4e41-b9da-982106d29c55",
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Pizza with cheese",
    "meal_provider_id": "b987d0ff-5edf-46dd-8c1a-e4511916d464",
    "img": ""
}
]
```

### Add new meal
#### **POST** meal metod call example:
> POST [YOUR_SERVER_ADDRESS/meal]

> Should contain "token" in header

```JSON
Request:
{
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Pizza with peperonni",
    "meal_provider_id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "img": ""
}
Response: 200 OK
{   
    "id": "1cca84d6-3833-4854-bb80-3d06a342180e",
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Pizza with peperonni",
    "meal_provider_id": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "img": ""
}
```

### Invite user to group
#### **POST** invite metod call example:
> POST [YOUR_SERVER_ADDRESS/invite]

> Should contain "token" in header

```JSON
Request:
{
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "email": "friend@gmail.com",
    "message": "Join our group to hang out together!"
}
Response: 200 OK
{   
    "id": "1cca84d6-3833-4854-bb80-3d06a342180e",
    "invitee_email": "friend@gmail.com",
    "group_name": "Awesome friends",
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "message": "Join our group to hang out together!"
}
```


### Get user's invitations
#### **GET** invite metod call example:
> GET [YOUR_SERVER_ADDRESS/invitations]

> Should contain "token" in header

```JSON
Request:
{
}
Response: 200 OK
[
{   
    "id": "1cca84d6-3833-4854-bb80-3d06a342180e",
    "invitee_id": "c7413dde-5c9c-493b-9afe-8c1edb153626",
    "group_name": "Awesome friends",
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "invitator_name": "John Smith",
    "invitator_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "message": "Join our group to hang out together!"
},
{   
    "id": "6767f978-7e48-4e41-b9da-982106d29c55",
    "invitee_id": "d8322cc4-479c-48c5-af1d-21748da01460",
    "group_name": "Even more awesome friends",
    "group_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "invitator_name": "Jane Doe",
    "invitator_id": "05043a00-018a-46a8-be79-74b3c992c790",
    "message": "Join our group to hang out together!"
},
]
```

## TODO:
- send invite email
- restore password
- Create meeting
- Voting system
- divide auth.py into different modules.

## Requires:

```
pip install Flask
pip install PyJWT
pip install mysql
pip install markdown
pip install uuid
```