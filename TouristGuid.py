import TGModulesDef as md
import TGWebsite as webb

#0 
def yesno(str):
    print("\nDo You Want More Info:\n1.Yes\n2.No")
    str1=input()

    if str1.lower()=="yes":
        print(webb.web(str))
    else:
        print("Thank You For Using Our Service. ")

#1
def ttype():
    print("\nEnter The Type Of Trip U Want:")
    print("\n1.Family trip \n2.Friend trip \n3.Bussiness Trip \n4.Couples Trip \n5.Religious Trip \n6.Solo Trip\n")
    n = int(input())
    print()

    return ttype
#2
def tseason():
    m = int(input("\nEnter The Season: \n1.Summer \n2.Winter \n3.Rainy \n"))
    if(m == 1):
        print("\n1.Temple \n2.Garden \n3.Industrial Factory \n4.Hill Station \n5.Forts/palace")
        p = int(input("Enter The Type Of Station U Want: \n"))

        
        if(p == 1):#temple
            print(("\n1.ISKON NVCC \n2.Tulsi Baug Ganpati Temple \n3.Shreemant Dagdusheth Halwai Ganpati \n4.Balaji Temple \n5.Shri Omkareshwar Temple \n6.Alandi Devsthan"))
            px = int(input("Choose Station U Want: \n"))
    
             
            if (px==1):
                str = "ISKON Temple"
                md.ISKONtemple()
        

            elif (px==2):
                str = "Tulsi Baug Ganpati Temple"
                md.tulsibaugganpati()
        

            elif (px==3):
                str = "Shreemant Dagdusheth Halwai Ganpati"
                md.sdshgmandir()
        

            elif (px==4):
                str = "Balaji Temple"
                md.balajimandir()
        

            elif (px==5):
                str = "Shri Omkareshwar Temple"
                md.shreeomkareshwartemple()
        

            else:
                str = "Alandi Devsthan"
                md.alanditemple()
        

    


        elif(p == 2):#garden
            print("\n1.Okayama Friendship Garden \n2.Osho Garden \n3.Bund Garden \n4.Yashwantrao Chavan Garden \n5.Chatrapati Shivaji Maharaj Garden")
            px = int(input("Choose Station U Want: \n"))
    
                       
            if (px==1):
                str = "Okayama Friendship Garden"
                md.ofgarden()
        
                    
            elif (px==2):
                str = "Osho Garden"
                md.oshogardenn()
        

            elif (px==3):
                str = "Bund Garden"
                md.bundgarden()
        

            elif (px==4):
                str = "Yashwantrao Chavan Garden"
                md.ycgaraden()
        

            else:
                str = "Chatrapati Shivaji Maharaj Garden"
                md.csmudhyan()
        
                
                

        elif(p == 3):#industrial
            print("\n1.BAJAJ Auto \n2.Bharat Forge \n3.Century Enka \n4.Finolex Cables")
            px = int(input("Choose Station U Want: \n"))
    
            
            if (px==1):
                str = "BAJAJ Auto Pvt Ltd"
                md.bajaj()
        

            elif (px==2):
                str = "Bharat Forge Pvt Ltd"
                md.bharatforge()
        

            elif (px==3):
                str = "Century Enka Ltd"
                md.centuryenkaltd()
        

            else:
                str = "Finolex Cables Ltd"
                md.finolexcltd()
        
    

        elif(p == 4):#hill station
            print("\n1.Mahabaleshwar \n2.Lonavala/Khandala Hills Series \n3.Matheran \n4.Panchagani \n5.Bhandardara")
            px = int(input("Choose Station U Want: \n"))
    

            if (px==1):
                str = "Mahabaleshwar"
                md.mahabaleshwarhillstation()
        
                
            elif (px==2):
                str = "Lonavala/Khandala Hills Series"
                md.lonavla()
        

            elif (px==3):
                str = "Matheran"
                md.matheran()
        

            elif (px==4):
                str = "Panchagani"
                md.panchgani()
        

            else:
                str = "Bhandardara"
                md.bhandardara()
        
                

        else:#forts/palace
            print("\n1.Lal Mahal \n2.Aga Khan Palace \n3.Carla Caves \n4.Lohagad fort")
            px = int(input("Choose Station U Want: \n"))
    
            
            if (px==1):
                str = "Lal Mahal"
                md.lalmahal()
        
                    
            elif (px==2):
                str = "Aga Khan Palace"
                md.agakhanpalace()
        

            elif (px==3):
                str = "Carla Caves"
                md.karlacaves()
        

            else:
                str = "Lohagad fort"
                md.lohagadfort()
        

                  
    elif(m == 2):
        print("\n1.Industrial Factory \n2.Hill Station \n3.Forts/palace")
        p = int(input("Enter The Type Of Station U Want: \n"))

       
        if(p == 1):#Industrial Factory
            print(("1.BAJAJ Auto \n2.Bharat Forge \n3.Century Enka \n4.Finolex Cables"))
            px = int(input("Choose Station U Want: \n"))
    
            
            if (px==1):
                str = "BAJAJ Auto Pvt Ltd"
                md.bajaj()
        

            elif (px==2):
                str = "Bharat Forge Pvt Ltd"
                md.bharatforge()
        

            elif (px==3):
                str = "Century Enka Ltd"
                md.centuryenkaltd()
        

            else:
                str = "Finolex Cables Ltd"
                md.finolexcltd()
        
                

        elif(p == 2):#Hill Station
            print("\n1.Mahabaleshwar \n2.Lonavala/Khandala Hills Series \n3.Matheran \n4.Panchagani \n5.Bhandardara")
            px = int(input("Choose Station U Want: \n"))
    
            
            if (px==1):
                str = "Mahabaleshwar"
                md.mahabaleshwarhillstation()
        
                
            elif (px==2):
                str = "Lonavala/Khandala Hills Series"
                md.lonavla()
        

            elif (px==3):
                str = "Matheran"
                md.matheran()
        

            elif (px==4):
                str = "Panchagani"
                md.panchgani()
        

            else:
                str = "Bhandardara"
                md.bhandardara()
        
                

        else:#Forts/palace
            print("\n1.Shanivar Wada \n2.Lal Mahal \n3.Aga Khan Palace \n4.Carla Caves \n5.Lohagad fort")
            px = int(input("Choose Station U Want: \n"))
    

            if (px==2):
                str = "Lal Mahal"
                md.lalmahal()
        
                    
            elif (px==3):
                str = "Aga Khan Palace"
                md.agakhanpalace()
        

            elif (px==4):
                str = "Carla Caves"
                md.karlacaves()
        

            else:
                str = "Lohagad fort"
                md.lohagadfort()
        
                

    else :
        print("\n1.Garden \n2.Waterfall \n3.Dam/Lake")
        p = int(input("Enter The Type Of Station U Want: \n"))


        if(p == 1):#Garden
            print(("1.Okayama Friendship Garden \n2.Osho Garden \n3.Bund Garden \n4.Yashwantrao Chavan Garden \n5.Chatrapati Shivaji Maharaj Garden"))
            px = int(input("Choose Station U Want: \n"))
    
                   
            if (px==1):
                str = "Okayama Friendship Garden"
                md.ofgarden()
        
                    
            elif (px==2):
                str = "Osho Garden"
                md.oshogardenn()
        

            elif (px==3):
                str = "Bund Garden"
                md.bundgarden()
        

            elif (px==4):
                str = "Yashwantrao Chavan Garden"
                md.ycgaraden()
        

            else:
                str = "Chatrapati Shivaji Maharaj Garden"
                md.csmudhyan()
        
                

        elif(p == 2):#Waterfall
            print("\n1.Kune Falls \n2.Tamhini Falls \n3.Devkund Falls \n4.Bendewadi Falls")
            px = int(input("Choose Station U Want: \n"))
    

            if (px==1):
                str = "Kune Falls"
                md.kunafalls()
        

            elif (px==2):
                str = "Tamhini Falls"
                md.tamhinifalls()
        

            elif (px==3):
                str = "Devkund Falls"
                md.devkundfalls()
        

            else:
                str = "Bendewadi Falls"
                md.bendewadifall()
        
                
        else:#Dam/Lake
            print("\n1.Khadakwasla Dam \n2.Bhusi dam \n3.Mulshi dam \n4.Panshet Dam \n5.Hadshi dam \n6.Peshave Park Lake")
            px = int(input("Choose Station U Want: \n"))
    
            
            if (px==1):
                str = "Khadakwasla Dam"
                md.khadakwasladam()
        
        
            elif (px==2):
                str = "Bhusi dam"
                md.bhushidam()
        

            elif (px==3):
                str = "Mulshi dam"
                md.mulshidam()
        
            

            elif (px==4):
                str = "Panshet Dam"
                md.panshetdam()
        

            elif (px==5):
                str = "Hadshi dam"
                md.hadshidam()
        

            else:
                str = "Peshave Park Lake"
                md.peshaveparklake()
        
    yesno(str)  

    return tseason

#3
def tarea():
    print("\nOnly Pune Area Is Available Now")
    print()

    return tarea

#4
def tmaindetails(): 

    naav=input("\nEnter Your Good Name (First Middle Last) : ")
    patta=input("Enter Your Full Address : ")
    vay=float(input("Enter Your Age : "))
    aadhar=int(input(("Enter Your Aadhar Card No : ")))
    print()

    return tmaindetails
    

#5
def tsubdetails():
    
    n=int(input(("\nExcept You How Many Members are with You...? \n")))

    for sub in range (1,n+1):
        print("\nCandidate No.",sub,"\n")
        naav1=input("Enter Your Good Name (First Middle Last) : ")
        patta=input("Enter Your Full Address : ")
        vay=int(input("Enter Your Age : "))
        print()

    return tsubdetails
























# def ttypestation():
#     o = int((print("Enter The Type Of Station U Want: \n",
#             "1.Temple \n2.Garden \n3.Industrial Factory \n4.Hill Station \n5.Waterfall \n6.Dam/Lake"))
#     if(o == 1):

#     elif(o == 2):
        
#     elif(o == 3):

#     elif(o == 4):

#     elif(o == 5):  

#     else:



# def tstation():
#     p = int((print("Enter The Type Of Station U Want: \n",
#             "1.Temple \n2.Garden \n3.Industrial Factory \n4.Hill Station \n5.Waterfall \n6.Dam/Lake \n7.Forts/palace"))
#     if(p == n):
#         px = int((print("Choose Station U Want: \n",
#             "1.ISKON NVCC \n2.Tulsi Baug Ganpati Temple \n3.shreemant dagdusheth halwai ganpati \n4. \n5. \n6."))

#     elif(p == n):
#         px = int((print("Choose Station U Want: \n",
#             "1.Okayama Friendship Garden \n2.Empress Botanical Garden \n3.Osho Garden \n4.Bund Garden \n5. \n6."))

#     elif(p == n):
#         px = int((print("Choose Station U Want: \n",
#             "1. \n2. \n3. \n4. \n5. \n6."))

#     elif(p == n):
#         px = int((print("Choose Station U Want: \n",
#             "1. \n2. \n3. \n4. \n5. \n6."))

#     elif(p == n):
#         px = int((print("Choose Station U Want: \n",
#             "1. \n2. \n3. \n4. \n5. \n6."))

#     elif(p == n):
#         px = int((print("Choose Station U Want: \n",
#             "1.Shanivar Wada \n2.Lal Mahal \n3.Aga Khan Palace \n4.Shri Mahalaxmi Mandir  \n5. \n6."))
#     else:



