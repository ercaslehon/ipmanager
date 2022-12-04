============
IpManager
============

Introduction
============

This small utility is my test project.

It is essentially a tool for recording and storing data about IP addresses and networks. In theory it could be useful for network administrators working with large numbers of networks, but it could be useful in other areas with a little tweaking)

Several Python modules serve as the basis here:

FastAPI - handy for accepting requests and passing correct responses from executable functions. 

Tortoise - a module for interacting with the database. Despite its name it's considered almost the fastest ORM, so I took it. In fact, the main work is done with it, but about this later, when I will go directly to the allowed methods.

LogBook - If we are talking about an accounting system, I think it would be correct to track changes in the database tables. 

Actually, apart from the database with two tables described in app/modules.py, that's pretty much all there is to it. 

Functionality
============

Now for the most interesting part. There are 10 methods available to use, 5 for each of the tables. You can check them out below or with the default FastAPI query /docs

Method №1 SEARCH
---------------------------
The search method is called by the links /ip/search and /net/search
This method does not take any values at all and shows all values of the corresponding table. 

Method №2 SHOW
---------------------------
The search method for a specific value is called by /ip/show?ip={ip} and /net/show?net={net}

Unlike the previous method, this one is needed to find and display information about a particular IP or network. It takes an IP or network value as input, respectively.

The method can respond with the following response codes:

With 200 response code you will see a message with IP\network information. It means that the function worked correctly.

If you get a 404 response code as an answer, you will see a message saying that you passed a valid IP/network but it does not exist in the database. Expectedly.

Also the method expects a 400 response code with the message that the method received an invalid IP/network. 


Method №3 ADD
---------------------------
A method to add a record to the database. Called by /ip/add and /net/add. Input requires three parameters: 

ip/net - specifying the desired IP or network with mask.
Used/active - used for IP, active for network - boolean values True/False. Actually you need to specify the status of IP or network.
comment - arbitrary comment for the entry. 

The final request link will look like this:

/ip/add?ip=127.0.0.1&used=True&comment=something special
/net/add?net=192.168.0.0/24&active=False&comment=who did this?

The method can respond with the following response codes:

With response code 200, the desired IP\network will be added to the database. It means that the function worked correctly and you will be offered to use the show method to verify if the data was added to the database correctly.

If the response code you get is 412, you will see a message saying that you have passed a valid IP/network but it already exists in the database. It wouldn't be right if we could multiply records about the same IP/network, would it?

Also the method expects a 400 response code with the message that the method received an invalid IP/network. 

Method №4 DEL
---------------------------
The method of removing a record from the database. Called by /ip/del and /net/del. Requires only the IP address to enter:

/ip/del?ip=127.0.0.1&used
/net/del?net=192.168.0.0/24

The method can respond with the following response codes:

With response code 200, the desired IP\network will be removed from the database. This means that the function worked correctly.

If you get response code 412 as a response, you will see a message that you have passed a valid IP/network but it does not exist in the database.

Also, the method expects a 400 response code with the message that the method received an invalid IP/network. 

Method #5 MOD
---------------------------
A method to modify records in the database. Called by /ip/mod and /net/mod. It again requires three parameters to enter: 

ip/net - specifies the desired IP or network with mask. It is not possible to change IP address, here it is used only for searching the right string in the database. 
Used/active - used for IP, active for network - boolean values True/False. Actually you should specify the status of IP or network.
Comment - any arbitrary comment on the entry. 

The final request link will look like this:

/ip/mod?ip=127.0.0.1&used=True&comment=something special
/net/mod?net=192.168.0.0/24&active=False&comment=It Was Me, Dio!

The method can respond with the following response codes:

With response code 200, the desired IP\network will be changed as requested. This means that the function worked correctly and you will be offered to use the show method to check if the data was added to the database correctly.

If the response code received is 404, you will see a message saying that you passed a valid IP\network but it is not in the database. You can't modify something that doesn't exist)

Also, the method expects a 400 response code with the message that the method received an invalid IP/network. 


Endpoint
============
I think I've described everything you need to know. I may have missed something, of course, but the essentials are there.

I have a diagram of how the tool works, but it's only in Russian so far, and I'm not sure I'll rewrite it into English: https://miro.com/app/board/uXjVPBZ7BJo=/?share_link_id=939878736574

Maybe later I'll wrap it up in a docker and make ansible playbook. 
