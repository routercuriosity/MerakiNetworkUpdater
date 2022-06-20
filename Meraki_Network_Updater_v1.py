#███╗   ███╗███████╗██████╗  █████╗ ██╗  ██╗██╗    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗
#████╗ ████║██╔════╝██╔══██╗██╔══██╗██║ ██╔╝██║    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
#██╔████╔██║█████╗  ██████╔╝███████║█████╔╝ ██║    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
#██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║██╔═██╗ ██║    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗     ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
#██║ ╚═╝ ██║███████╗██║  ██║██║  ██║██║  ██╗██║    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
#╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
#This is version1 of the Meraki Network Updater. An interactive python script framework that allows you
#to input your Meraki networks and update settings via menu options.

import meraki
import os
import xlrd


#Meraki Organization Information
#Step1. Add API Key to Server Environment. See https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html
#Step2. Add API variable and point dashboard variable to API_KEY.

API_Key = os.environ['MERAKI_DASHBOARD_API_KEY']
dashboard = meraki.DashboardAPI(API_Key)

#Step3. Create a dictionary for all networks in the origanization, preferrably in a xls document,
# #Dictionary of all Networks in Organization. Used to pair Network name to Network ID.
# Network Dictionary file location
loc = (r"path of file")

#Open and read Dictionary File
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
#Dictionary Var that points to Excel file
NetDict = {}
#Build Dictionary
for rownum in range(sheet.nrows):
    NetDict[sheet.cell(rownum, 0).value] = [sheet.cell(rownum, 1).value]


#Menu Steps - Create a multi-layered Menu for selecting the network and inplmenting changes.
#Step 1. Main Menu - define the Top-Level Menu Selections for what changes you want in your network(s). Utilize the [0] option as selecting a new network or exiting the program.
#Main Menu
def UpdateMenu():
    print("[1] Option Change 1")
    print("[2] Option Change 2")
    print("[0] Choose a Network or Exit")


#Step 2. Select what appliances you would like to update. Depending on the network, you may have to add options for multiple (working on a checkbox style code). Utilize the [0] option to return to previous menu.
#Menu for choosing what appliances are in a network
def NetDevMenu():
    print("[1] Appliance")
    print("[2] Appliance & Switch")
    print("[3] Appliance & AP")
    print("[4] Appliance, Switch & AP")
    print("[5] Example 5...")
    print("[0] Return to previous menu")

#Define PUT variables that correlate with the Meraki Python Library. Examples include and PUT command; updating syslogs, firewall rules, etc.
# Step1. Create the action variables.
#Syslog Updates for each network device combo selection. Syslog server is <Syslog Server>. Makes sure to verify all Syslog roles as this could change based on applliances in network.
MXSyslog = [{'host': '<Syslog Server>', 'port': '514', 'roles': ['<Syslog Roles>']}]

#Build Program to interact with Networks, Menus, and Actions.
#Step1. Build While True Loop
while True:
    #Program to select a valid network and update the Selected Network.
    print("Hello and welcome to the Meraki network updater.")
    NetName = input('What Network would you like to update:')
#Step2. Build Menu Interaction Ifs. Input your network and if valid network, you will select options from the action menu.
    #In the submenu you will select what appliances are in the network. Based on that input, the program will update what you selected.
    #Once completed, it will print out the PUT action you selected for verification. If you enter an option that doesn't exist, the program will kick you back to the previous menu.
    #Menu on what to update.
    #1st - Verifies that the Network Name submited is listed in the dictionary by checking the name with the license. Replace Var removes brackets and single quotes from dictionary Value.
    if NetName in NetDict:
        print("The Network ID is:", NetDict[NetName])
        NetID = (str(NetDict[NetName]).replace("[", "").replace("]", "").replace("'", ""))
    #2nd  - Select the option from the UpdateMenu Menu created previously. Once Selected, it will direct to the NetDevMenu
    #Application is wrapped in While True function to allow it to repeat process until no longer required. Followed my an If/elif statements to select the correct menu. If invalid NetID is submitted it will break menu and restart the change request.
    #Fisrt Option From Top Menu
        UpdateMenu()
        UpdateOption = int(input("Enter your option:"))
        while UpdateOption != 0:
            if UpdateOption == 1:
               print("Menu Option 1 - What devices are in this network?")
                NetDevMenu()
                NetDevOption = int(input("Device(s) Option:"))
                while NetDevOption != 0:
                    if NetDevOption == 1:
                       print("Let's Do SubOption Change 1!")
                       UpdateOp1 = dashboard.networks.update...(NetID, MXSyslog)
                       print(UpdateOp1)
                    elif NetDevOption == 2:
                       print("Let's Do SubOption Change 2!")
                       UpdateOp2 = dashboard.networks.update...(NetID, MXSyslog)
                       print(UpdateOp2)
                    else:
                        print("That doesn't work!")
                    print()
                    break
    Second Option from Top menu
            elif UpdateOption == 2:
                print("Option Change 2")
                TopMenuOption2 = dashboard.appliance...(NetID, MXSyslog)
                print(TopMenuOption2)
            else:
                print("Invalid Option.")
            print()
            break
    # Once finished, it and you select, it will thank you for changes and return to ask if you want to make more changes.
        print("Thanks for making changes.")
#Step 3 - If you enter an invalid network, it will exit to the top menu.
    else:
        print('That network does not exist in database.')


#Final Step it will restart the loop to start on the next network or exit the program.
    restart = input("Do you want to update to another network [y]/n:")
    if restart.lower() == 'n':
        print('Thank you for using the network updater')
        break


