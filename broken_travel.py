# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) # AR has fixed '==' to '=' and 'int.input to 'int(intput'

if year < 1900: # AR has changed 'year <=1900 tp 'year < 1900'
    print ("Woah, that's the past!")  # AR has fixed single quote to double quote(") print statement
elif 1900 <= year <= 2020: # AR has fixed 'year > 1900 && year < 2020' to '1900 <= year <=2020'
    print ("That's totally the present!")
else:             # AR has replaced 'elif:' with 'else'
    print ("Far out, that's the future!!")

# Edited by Abdul Rahman