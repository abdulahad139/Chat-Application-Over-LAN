# Chat-Application-Over-LAN
This is a GUI Chat application built using Python.<br/>
# How to use this?
There are two folders in this repository<br>
One folder is for Client and the other is for Server.<br>
You can make one laptop as Server and place the Server folder in it. <br>
Consider any other laptop or PC as Client. Place the client folder in that PC/Laptop. You can also place the Client folder in the same laptop which you have opted as Server. <br>

# Necessary Changes in the files.
You have to change the Server IP in the server.py and client.py file. Remember the server IP should be same in both files.

# How to get Server IP?
1. Open command prompt (cmd)
2. type ipconfig
3. check for ipv4 address LAN
4. copy that address and place in both server.py and client.py file

# How to make new rules for SERVER_PORT 12345?
1. Open Windows Security:
  Press Win + I to open Settings.<br>
  Go to Update & Security > Windows Security > Firewall & network protection. <br>
2. Advanced Settings:
  Scroll down and click Advanced settings. This will open the Windows Defender Firewall with Advanced Security window.
3. Inbound Rules:
In the left panel, select Inbound Rules. This section manages rules for incoming connections to your computer.
4. Create a New Rule:
In the right panel, click New Rule....
In the New Inbound Rule Wizard, select Port and click Next.
5. Specify Port and Protocol:
Choose TCP and Specific local ports.
Enter 12345 in the port box (or the port number you’re using in your code).
Click Next.
6. Allow the Connection:
Choose Allow the connection and click Next.
7. Select Profile:
Choose when this rule should apply. It’s safest to check Private only, assuming this is a secure local network. Leave Domain and Public unchecked unless needed.
Click Next.
8. Name the Rule:
Give the rule a name, like “Chat Application Port 12345.”
Click Finish.
9. Repeat for Outbound Rules:
To ensure your computer can also send data on this port, go back to the main Windows Defender Firewall with Advanced Security window.
Select Outbound Rules in the left panel and repeat the above steps to create a rule for Outbound connections on port 12345.
