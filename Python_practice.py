#PRINT STATEMENT
# print ("Hello World")
# print("Your interest for the year is $" + str(interest))
##########################################################
#F STRING
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# #OR with F string
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# for county voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")


#MULTILINE F STRINGS
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")
# print(message_to_candidate)

##########################################################
#LISTS, adding removing
# countries=["Arapahoe", "Denver", "Jefferson"]
# print (countries)
# countries.append ("el paso")
# print (countries)
# countries.remove("el paso")
# print (countries)
# countries.insert (1, "El Paso")
# print (countries)
# countries.remove ("Arapahoe")
# print (countries)
# countries[1] ="Jefferson"
# print (countries)
# countries[2] ="Denver" and countries.append ("Arapahoe")
# print (countries)
# countries_dic={}
# countries_dic["Arapahoe"] = 422829
# print (countries_dic)
# countries_dic["Denver"]= 463353
# countries_dic["Jefferson"]= 432438
# print (countries_dic)
##########################################################
#DICTONARY
# voting_data=[]
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# print (voting_data)
# voting_data.append({"county":"El Paso", "registered_voters": 461149})
# print (voting_data)
##########################################################
# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
##########################################################
# What is the score?
# score = int(input("What is your test score? "))
# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')
# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
##########################################################
#LIST CREATION and IF ELSE condition with INPUT
# name=["Archana", "Nitin", "Avni", "Vani"]
# role=["mother", "father", "sister"]
# age=["40", "41","8", "2"]
# user_selection= input("Enter family member name:")
# user_age= int(input ("enter age:"))
# if user_selection in name[0] and user_age==40:
#    print ("you selected the mother " + user_selection)
# else:
#    print ("you made wrong choice")
##########################################################
#WHILE LOOPS with exit defined
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1
##########################################################
#FOR LOOPS-- also listing simply all items inside a List or Tuple in sequence
# counties = ["Arapahoe","Denver","Jefferson", "El-Paso"]
# # for county in counties:
# #     print(county)
# # for num in range(5):
# #     print(num)
# i=0
# for i in range(len(counties)):
#     print(counties[i])
##########################################################
# #ITERATE THROUGH A DICTONARY
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# # for county in counties_dict:
# #     print(county)
# # for county in counties_dict.keys():
# #     print(county)
# # for voters in counties_dict.values():
# #     print(voters)
# # for county in counties_dict:
# #     print(counties_dict.get(county))
# # for key, value in dictionary_name.items():
# #     print(key, value)
# for key, value in counties_dict.items():
#     print(key," couny has ", value, " registered voters ")
############################################################
#importing libraries
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)