questions = [["The red sandalwood or red sanders trees, shown in the film “Pusha: The Rise”, are endemic to which region of India?",
             "Western Ghats","Sundarbans","Eastern Ghats","Doaba",3],
             ["What name has been given to the 216-feet statue of Sri Ramanujacharya, unveiled in Hyderabad in February 2022?",
              "Statue of Unity","Statue of Freedom","Statue of Fraternity","Statue of Equality",4],
             ["The 2022 Oscar-nominated Indian documentary “Writing With Fire” tells the story of the women journalists of which rural newspaper?",
              "Khabar Lahariya","Gaon Connection","Akhand Jyoti","Kadambini",1],
             ["The Australian spin legend Shane Warne captained which team to an IPL championship title?",
               "Rajasthan Royals","Deccan Chargers","Sunrisers Hyderabad","Kolkata Knight Riders",1],
             ["Which of these is common to the CEOs of Adobe, Google, IBM, Microsoft, and Twitter?",
               "Graduated from IITs","Persons of Indian Origin","Chess prodigies","Acted in movies",2],
             ["Built by the Border Roads Organization, which is the “highest altitude road” in the world, recognised by the Guinness World Records in 2021?",
              "Umling La Pass","Zoji La Tunnel","Rohtang Pass","Lipulekh Pass",1],
             [" Labels assigned by the World Health Organization for key variants of COVID 19 causing viruses, use letters of which alphabet?",
              "Chinese","Greek","Roman","Cyrillic",2],
             ["The first live performance by Lata Mangeshkar of which patriotic song in 1963 is said to have moved Pandit Jawaharlal Nehru to tears?",
              "Aye Mere Watan Ke Logon","Aisa Desh Hai Mera","Aye Mere Pyaare Watan","Mere Desh Ki Dharti",1],
             [" Who trapped Tasnim Beaumont leg before wicket to become the first woman to take 250 wickets in ODIs?",
              "Anisa Mohammed","Shabnim Ismail","Jhulan Goswami","Mithali Raj",3],
             ["What was the name of the operation carried out by the Government of India to safely bring back Indians from war-torn Ukraine?",
              "Operation Ganga","Operation Sukoon","Operation Kyiv","Operation Raahat",1],
             ["Which song by peanut seller Bhuban Badyakar went viral on social media in early 2022?",
              "Boring Day","Kacha Badam","Bachpan Ka Pyar","Dilon Ka Shooter",2],
             ["4th February 2022 marked 100 years of which event of the Indian Independence movement?",
              "Champaran Satyagraha","Jalianwala Bagh Massacre","Chauri Chaura Incident","Gandhiji’s return to India",3],
             ["Who is this beauty queen?","Manushi Chhillar","Harnaaz Sandhu","Shree Saini","Vartika Singh",2],
             ["What does the “A” stand for in the intergovernmental military alliance NATO?",
              "Atlantic","Army","America","Association",1],
             ["Which city is served by the newly named “Virangana Laxmibai” railway station?",
              "Gwalior","Jhansi","Indore","Itarsi",2]]


levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1200000,2500000,5000000,10000000]
money = 0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"A. {question[1]}               B. {question[2]}")
    print(f"C. {question[3]}               D. {question[4]}")
    reply = int(input("Enter your answer:"))
    if (reply==question[-1]):
        print(f"Correct answer,you have won Rs. {levels[i]}")
        if (reply ==0):
            money = levels[i-1]
            break
        if (i == 4):
            money = 10000
        elif (i ==9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break
print(f"Your home taken money is {money}")

