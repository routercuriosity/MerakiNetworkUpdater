# MerakiNetworkUpdater
Python Script to Update Meraki Networks via a custom built menu.
An interactive python script framework that allows you to input your Meraki networks and update settings via menu options.

The first version provides the framework for the updater to be built. It points to a XLS document where Network Names and Network IDs are stored. a template is provide to build a set of menus and menu options of what you would like the Network Updater script to do to each network. Currently this only works with one network at a time, but in situations where you have to update 30+ networks, this saves you a lot of time and provides more granual control of changes. 

Steps from Script Comments:API, Dashboard, and Dictionary.

<ins>**#Environment Steps:**</ins>

**#Step1.** Add API Key to Server Environment. See https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

**#Step2.** Add API variable and point dashboard variable to API_KEY.

**#Step3.** Create a dictionary for all networks in the origanization, preferrably in a xls document. Dictionary of all Networks in Organization. Used to pair Network name  #        to Network ID.

<ins>**#Menu Steps**</ins> - Create a multi-layered Menu for selecting the network and inplmenting changes.

**#Step 1.** Main Menu - define the Top-Level Menu Selections for what changes you want in your network(s). Utilize the [0] option as selecting a new network or exiting the #        program.

**#Step 2.** Select what appliances you would like to update. Depending on the network, you may have to add options for multiple (working on a checkbox style code).       #            Utilize the [0] option to return to previous menu.


<ins>**#Put Steps:**</ins> Define PUT variables that correlate with the Meraki Python Library. Examples include and PUT command; updating syslogs, firewall rules, etc.

**#Step1.** Create the action variables.

<ins>**#Program Build Steps:**</ins> Build Program to interact with Networks, Menus, and Actions.
**#Step1.** Build While True Loop.
**#Step2.** Build Menu Interaction Ifs. Input your network and if valid network, you will select options from the action menu.
**#Step3** - If you enter an invalid network, it will exit to the top menu.
**#Final Step** - Will restart the loop to start on the next network or exit the program.
