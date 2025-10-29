print('--- User Input Form ---')
name = input('Enter your name: ').strip()

try:
    def get_dob_separate():
        print("Enter your date of birth:")
        day = input("DD: ").strip().zfill(2)    
        month = input("MM: ").strip().zfill(2)
        year = input("YYYY: ").strip()
        
        dob = f"{day}/{month}/{year}"
        print(f"Date of birth: {dob}")
        return dob
    
    date_of_birth = get_dob_separate()
    age = 2025 - int(date_of_birth[-4:])  
    
    while age < 0:
        print('Invalid year of birth. Please try again.')
        date_of_birth = get_dob_separate()  
        age = 2025 - int(date_of_birth[-4:])
    
    print(f'Age : {age}')

except ValueError:
    print('Invalid date format. Please enter in DD/MM/YYYY format.')

religion = input('Enter your religion: ').strip()
gender = input('Enter your gender (Male/Female): ').strip()
telephone = input('Enter your telephone number: ').strip()
email = input('Enter your email address: ').strip()

print('\n--- User Information ---')
print(f'Name          : {name.title():20}')   
print(f'Date of Birth : {date_of_birth:20}')  
print(f'Religion      : {religion.title():20}')
print(f'Gender        : {gender.title():20}')               
print(f'Telephone     : {telephone:20}')      
print(f'Email         : {email:20}')          
print('------------------------')