# Imports necessary libraries
import streamlit as st


# Sets a title "Wine Quality Predictor" for the web-application using streamlit
st.title("Wine Quality Predictor")

# Creates 10 objects with the same widths, where the individual variable-names indicate their position
row1_col1, row1_col2 = st.columns([1, 1])
row2_col1, row2_col2 = st.columns([1, 1])
row3_col1, row3_col2 = st.columns([1, 1])
row4_col1, row4_col2 = st.columns([1, 1])
row5_col1, row5_col2 = st.columns([1, 1])

# Sets individual titles for each variable
row1_col1.write("Wine type")
row1_col2.write("Fixed acidity")
row2_col1.write("Volatile acidity")
row2_col2.write("Citric acid")
row3_col1.write("Residual sugar")
row3_col2.write("Chlorides")
row4_col1.write("Free sulfur dioxide")
row4_col2.write("Total sulfur dioxide")
row5_col1.write("Sulphates ")
row5_col2.write("Alcohol")


# Displays a radio button widget for the user to enter the wine-type
Wine_type = row1_col1.radio(
    "Enter wine type:",
    options=['Red wine', 'White wine'], )
row1_col1.write(Wine_type)  # Shows the user the entered input

# Displays a slider widget for the user to enter float values from 0 to 16 for the fixed acidity
Fixed_acidity = row1_col2.slider(
    "Enter the amount of fixed acidity:",
    min_value=0.0,
    max_value=16.0,
    value=8.0)  # Sets a default value of 8
row1_col2.write(Fixed_acidity)  # Shows the user the entered input

# Displays a slider widget for the user to enter float values from 0 to 1 for the volatile acidity
Volatile_acidity = row2_col1.slider(
    "Enter the amount of volatile acidity:",
    min_value=0.0,
    max_value=1.0,
    value=0.5)  # Sets a default value of 0.5
row2_col1.write(Volatile_acidity)  # Shows the user the entered input

# Displays a slider widget for the user to enter float values from 0 to 2 for the citric acidity
Citric_acid = row2_col2.slider(
    "Enter the amount of citric acid:",
    min_value=0.0,
    max_value=2.0,
    value=1.0)  # Sets a default value of 1.0
row2_col2.write(Citric_acid)  # Shows the user the entered input

# Displays a slider widget for the user to enter integer values from 0 to 70 for the residual sugar
Residual_sugar = row3_col1.slider(
    "Enter the amount of residual sugar:",
    min_value=0,
    max_value=70,
    value=35)  # Sets a default value of 35
row3_col1.write(Residual_sugar)  # Shows the user the entered input

# Displays a slider widget for the user to enter float values from 0 to 0.4 for the amount of chlorides
Chlorides = row3_col2.slider(
    "Enter the amount of chlorides:",
    min_value=0.0,
    max_value=0.4,
    value=0.2)  # Sets a default value of 0.2
row3_col2.write(Chlorides)  # Shows the user the entered input

# Displays a slider widget for the user to enter integer values from 0 to 289 for the amount of free sulfur dioxide
Free_sulfur_dioxide = row4_col1.slider(
    "Enter the amount of free sulfur dioxide:",
    min_value=0,
    max_value=289,
    value=144)  # Sets a default value of 144
row4_col1.write(Free_sulfur_dioxide)  # Shows the user the entered input

# Displays a slider widget for the user to enter integer values from 0 to 450 for the amount of total sulfur dioxide
Total_sulfur_dioxide = row4_col2.slider(
    "Enter the amount of total sulfur dioxide:",
    min_value=0,
    max_value=450,
    value=225)  # Sets a default value of 225
row4_col2.write(Total_sulfur_dioxide)  # Shows the user the entered input

# Displays a slider widget for the user to enter float values from 0 to 1.2 for the amount of sulphates
Sulphates = row5_col1.slider(
    "Enter the amount of sulphates:",
    min_value=0.0,
    max_value=1.2,
    value=0.6)  # Sets a default value of 0.6
row5_col1.write(Sulphates)  # Shows the user the entered input

# Displays a slider widget for the user to enter float values from 0 to 1.2 for the amount of alcohol
Alcohol = row5_col2.slider(
    "Enter the amount of alcohol:",
    min_value=7.0,
    max_value=15.0,
    value=11.0)  # Sets a default value of 11.0
row5_col2.write(Alcohol)  # Shows the user the entered input


# Calculates the quality of red wine using the parameters of a OLS regression method trained on a training data set
Red_quality = 2.8245 + (0.0364*Fixed_acidity) - (1.1789*Volatile_acidity) - (0.0910*Citric_acid)
Red_quality += (0.0053*Residual_sugar) - (1.7123*Chlorides) + (0.0028*Free_sulfur_dioxide)
Red_quality += - (0.0026*Total_sulfur_dioxide) + (0.8231*Sulphates) + (0.2695*Alcohol)

# Calculates the quality of white wine using the parameters of a OLS regression method trained on a training data set
White_quality = 2.5787 - (0.0602*Fixed_acidity) - (1.9103*Volatile_acidity) - (0.0126*Citric_acid)
White_quality += (0.0238*Residual_sugar) - (1.7935*Chlorides) + (0.0047*Free_sulfur_dioxide)
White_quality += - (0.0005*Total_sulfur_dioxide) + (0.4161*Sulphates) + (0.3703*Alcohol)


# Returns a rounded quality-value for red wine if the entered wine-type is red
if Wine_type == "Red wine":
    st.write(f"Your red wine's quality is: {round(Red_quality,2)}")

# Returns a rounded quality-value for white wine if the entered wine-type is white
elif Wine_type == "White wine":
    st.write(f"Your white wine's quality is: {round(White_quality,2)}")

# Returns an error message in case the code doesn't work.
else:
    st.write("Excuse me, an error has occurred.")
