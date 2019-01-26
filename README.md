# Meet with friends app

This is simple app to manage your meetings with friends. 
Scope and ideas are currently in progress.

```
If you have something to add - feel free
```


#Endpoint list
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