# multi-connection-socket-communication

### Requirements
Python 3 

### Default Server Configuration
The default configuration is for a LAN enviornment<br />
The server is automatically set to be run off of the IP address of the system it is being ran on<br />
The default port which the application is being ran on is 33000<br /><br />

### Custom Server Configuration
If you wish to broaden the scope of acceptible connections to go beyond your LAN, please change line 62, the HOST variable, of server.py to be the systems PUBLIC IP address. This will allow the application to be connected to from any system who has access to the internet. Note: Issues may occur depending on the configuration of the networks firewall.<br />
If you wish to change the port number the server is being ran off, change line 63, the PORT variable, in server.py to the available port number. Note: Ensure the port number isn't being used for another service being ran on your machine as it may cause issues.<br /><br />

### Start Server 
python server.py<br />

### Start Client(s)
python client.py<br />

#### Client Flow
###### Server Selection
Once the client script is running, you will be prompted to either select:<br />
1. Lan Server<br />
2. Public Server<br />

Your choice will be decided on where you chose to run the server.<br />
If option (1) is selected, then the IP address will automatically be filled.<br />
If option (2) is selected, then you will be prompted to provide the PUBLIC IP address of the server you are wishing to connect too.<br />

###### Port Selection
Once your server options are chosen, you will be prompted to input the PORT number the server is listening on.<br />
The server by default is running on PORT 33000, so input 33000, or whatever port the server is listening too. <br />

###### Username
You will be welcomed and prompted to input your name.<br />
Note: only the messages being transmitted are encrypted, not your username.<br />

###### Messaging
You will be shown all messages being sent within the chatroom, and alerts to clients entering and leaving aswell. <br />

###### Private Message
If you wish to private message someone then write:<br />
/msg TargetUser YourMessage<br />and the message will not be broadcast, but sent to only the target user.<br />

###### Leaving Chatroom
To leave the chatroom, simply type {quit} and it will terminate your connection.<br />

#### Encrption / Decryption
We used a basic Caesar Cipher to encrypt and decrypt the data before and after transmission clientside.<br />
