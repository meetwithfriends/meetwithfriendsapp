# Meet with friends app

This is simple app to manage your meetings with friends. 
Scope and ideas are currently in progress.

```
If you have something to add - feel free
```


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
> POST [YOUR_SERVER_ADDRESS/groups]

> Should contain "token" in header 
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
    "number_of_users": 2,
    "avatar": "https://{YOUR_SERVER_ADDRESS}/img/dummy.png"
}
]
```

### Create friends group
#### **POST** Create group metod call example:
> POST [YOUR_SERVER_ADDRESS/create_group]

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
    "groupId": "05043a00-018a-46a8-be79-74b3c992c790",
    "name": "Awesome group",
    "creatorId": "e1469ce8-8d85-471f-b4ca-6925b418f34b",
    "note": "For awesome friends",
    "number_of_users": 1,
    "avatar": "https://{YOUR_SERVER_ADDRESS}/img/dummy.png" //Filled with dummy image if no avatar selected
}
```



## Requires:

```buildoutcfg
pip install Flask
pip install PyJWT
pip install mysql
pip install markdown
pip install uuid
```