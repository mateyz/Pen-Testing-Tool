# PenTesting_Tool
 A tool drafted and designed during my final project for penetration testing in my Msc Cyber Security, allowing for the scan-detect-alert and execution of scripta against network  devices.
 
 The tool was split into four of what I believed to be the stages of identification, extraction and attack.
 
 
 ### Network Probing
 The tool has a built in network scanner, allowing for the initial stage of attack- identifying targets on the Network by simply asking them for a return ping. If the IP address returns a valid ping signal back we can assume that they're online.
 
 
 ### Banner Grabbing
 After an inital scan, the program will grab the banners of the selected devices. 
 
 This essentially asks them for service versions for specific ports that they're running. Banner grabbing is entirely legal if used to simply ask whether or not a service is running a specific version of said service, because a program **needs to be able to verify** versions for communication. 
 
 We can use this however for our next stage. 
 
 
 ### Vulnerability Database
 Using these Bannergrabbed service versions, we're capable of matching them against currently known and working exploits for each of the services that are running.
 
 If a vulnerable version is running on the host device, we'll add it to an array for the final stage.
 
 
 ### Exploitation
 The final stage of the attack presents you with a list of devices with vulnerabilities, alongside which services are vulnerable and which exploits are running - along with their damage level. It's worth reading up on what the exploit does with the link provided on the final sheet.


##### Disclaimer
 **This tool is released for educational purposes- any malicious activity is not permitted nor encouraged.**
 **The vulnerability database was localized during the Viva for the project, meaning this won't work unless you import and update a live vulnerability database.**
