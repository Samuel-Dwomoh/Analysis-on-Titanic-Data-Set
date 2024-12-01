# Libraries needed for this project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading the data set
dataSet = pd.read_csv("DataSets/train.csv").fillna("0")
print(dataSet.head())

# Comparing the survival rate by gender
Males_survived = dataSet[(dataSet["Survived"] == 1) & (dataSet["Sex"] == "male")] #.drop(columns = ["PassengerId","PassengerId","Name","SibSp","Parch","Ticket","Fare","Cabin","Embarked"])
No_of_male_survivors=Males_survived.shape[0]
print(Males_survived)

Females_survived = dataSet[(dataSet["Sex"] == "female") & (dataSet["Survived"] == 1)]
No_of_female_survivors = Females_survived.shape[0]

Total_no_of_males = dataSet[dataSet["Sex"] == "male"].shape[0]
print("The total number of males in the Titanic were =", Total_no_of_males)

Total_no_of_females = dataSet[dataSet["Sex"] == "female"].shape[0]
print("The total number of females in the Titanic were =", Total_no_of_females)

Male_survival_rate = (No_of_male_survivors / Total_no_of_males) * 100
Female_survival_rate = round((No_of_female_survivors / Total_no_of_females) * 100, 1)

Male_survival_rate_str = f"{Male_survival_rate:.1f}%"
Female_survival_rate_str = f"{Female_survival_rate:.1f}%"

No_of_survivors = {
   "Total": ["Male_survivors", "Female_survivors", "Male_survival_Rate", "Female_survival_rate"],
   "Sum": [No_of_male_survivors, No_of_female_survivors, Male_survival_rate_str, Female_survival_rate_str]
}

Total_No_of_survivors = pd.DataFrame(No_of_survivors)
print(Total_No_of_survivors.to_string(index=False))

pie = [No_of_male_survivors, No_of_female_survivors]
labels = ["Male survivors","Female survivors"]
colors = ['#94d2bd', '#ee9b00']
plt.pie(pie, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("Survival Distribution By Gender")
plt.legend(loc="lower center")
plt.show()

# Comparing the survival rate by class
pass_class1_survived = dataSet[(dataSet["Pclass"] == 1) & (dataSet["Survived"] == 1)].shape[0]
pass_class2_survived = dataSet[(dataSet["Pclass"] == 2) & (dataSet["Survived"] == 1)].shape[0]
pass_class3_survived = dataSet[(dataSet["Pclass"] == 3) & (dataSet["Survived"] == 1)].shape[0]

Total_pass_class1 = dataSet[(dataSet["Pclass"] == 1)].shape[0]
Total_pass_class2 = dataSet[(dataSet["Pclass"] == 2)].shape[0]
Total_pass_class3 = dataSet[(dataSet["Pclass"] == 3)].shape[0]
Total_pass = Total_no_of_males + Total_no_of_females

pass_class1_survival_rate = round((pass_class1_survived/Total_pass_class1)*100, 1)
pass_class2_survival_rate = round((pass_class2_survived/Total_pass_class2)*100, 1)
pass_class3_survival_rate = round((pass_class3_survived/Total_pass_class3)*100, 1)
pie = [pass_class1_survival_rate,pass_class2_survival_rate,pass_class3_survival_rate]
labels = ["First class", "Second class", "Third class"]
colors = ["#c0504d", "#8064a2", "#00baff"]
plt.pie(pie, labels=labels, colors=colors, autopct='%1.1f%%')
plt.legend(loc="lower center")
plt.title("Survival Rate by Passenger Class")
plt.show()

# Comparing death across age range
dataSet['Age'] = pd.to_numeric(dataSet['Age'], errors='coerce')
Children_death = dataSet[(dataSet["Age"] >= 0) & (dataSet["Age"] <=12 ) & (dataSet["Survived"] == 0)].shape[0]
Teenagers_death = dataSet[(dataSet["Age"] >= 13) & (dataSet["Age"] <=19 ) & (dataSet["Survived"] == 0)].shape[0]
Young_Adults_death = dataSet[(dataSet["Age"] >= 20) & (dataSet["Age"] <=35 ) & (dataSet["Survived"] == 0)].shape[0]
Adults_death = dataSet[(dataSet["Age"] >= 36) & (dataSet["Age"] <=55 ) & (dataSet["Survived"] == 0)].shape[0]
Elderly = dataSet[(dataSet["Age"] >= 56) & (dataSet["Survived"] == 0)].shape[0]
Labels = ["Children (0-12)", "Teenagers(13-19)", 'Young Adults(20-35)', 'Adults death(36-55)', 'Elderly(56 and Above)']
Categories =[ Children_death, Teenagers_death, Young_Adults_death, Adults_death, Elderly]
colors = colors = ['lightblue', 'orange', 'green', 'blue', 'gray']
plt.bar(Labels, Categories, color=colors)
plt.title("Total Death Across Age groups")
plt.xlabel("Age groupings")
plt.ylabel("Total number of deaths recorded")
plt.tight_layout()
plt.show()

# Fare ranges over survival
Low_Fare = dataSet[(dataSet["Fare"] >= 0 ) & (dataSet["Fare"] <= 10) & (dataSet["Survived"] == 0)].shape[0]
Lower_Medium_Fare = dataSet[(dataSet["Fare"] >= 10) & (dataSet["Fare"] <= 30) & (dataSet["Survived"] == 0)].shape[0]
Upper_Medim_Fare = dataSet[(dataSet["Fare"] >= 30) & (dataSet["Fare"] <= 100) & (dataSet["Survived"] == 0)].shape[0]
High_Fare = dataSet[(dataSet["Fare"] >= 100) & (dataSet["Fare"] <= 200) & (dataSet["Survived"] == 0)].shape[0]
Very_High_Fare = dataSet[(dataSet["Fare"] >= 200) & (dataSet["Survived"] == 0)].shape[0]
Labels = ["Low Fare", "Lower Medium", "Upper Medium", "High Fare", "Very High"]
Survival_by_fare = [Low_Fare, Lower_Medium_Fare, Upper_Medim_Fare, High_Fare, Very_High_Fare]
plt.bar(Labels, Survival_by_fare)
plt.xlabel("Fare Distribution")
plt.ylabel("Number of Deaths Recorded")
plt.title("Fare Ranges With Respect To Death")
plt.show()

# Counting the number of people who survived by place of embarkment
placeS = dataSet[(dataSet["Embarked"] == "S") & (dataSet["Survived"] == 1)].shape[0]
placeC = dataSet[(dataSet["Embarked"] == "C") & (dataSet["Survived"] == 1)].shape[0]
placeQ = dataSet[(dataSet["Embarked"] == "Q") & (dataSet["Survived"] == 1)].shape[0]
x = [placeS, placeC, placeQ]
labels = ["S", "C", "Q"]

# Plotting using a pie chart
plt.pie(x, labels=labels, autopct='%1.1f%%')
plt.title("Number Of People Who Survived By Place Of Embarkment")
plt.legend(loc="lower center")
plt.show()

# The number of