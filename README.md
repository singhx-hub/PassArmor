# PassArmor: Safeguarding Your Digital Identity

PassArmor is a password management tool that allows you to check the strength of your passwords and ensure they haven't been publicly leaked. With PassArmor, you can generate secure passwords, check their strength against various criteria, and verify if they have been exposed in public data breaches.

![PassArmor Logo](logo.png)

## Features

✅ Password Strength Check: PassArmor evaluates the strength of your passwords based on length, character diversity, and complexity. It ensures that your passwords meet the recommended criteria for robust security.

✅ Leakage Check: PassArmor scans your password against a comprehensive database of publicly leaked passwords. If your password is found in any known leaks, PassArmor will alert you, allowing you to take immediate action to safeguard your accounts.

✅ Auto-Generate Strong Passwords: PassArmor provides an auto-generate feature that creates strong, random passwords for you. These passwords are a combination of letters, numbers, and special characters, ensuring maximum security.

✅ User-Friendly Interface: PassArmor features an intuitive and user-friendly interface, making it easy for anyone to check password strength and leakage. The straightforward design allows you to quickly assess the security of your passwords.

✅ Real-Time Results: PassArmor provides instant feedback on the strength of your password and its leakage status. The results are displayed in a clear and concise manner, enabling you to make informed decisions about your password choices.


## Requirements

- Python 3
- tkinter (Python GUI package)

## Getting Started

Clone the repository:


       $ git clone https://github.com/your-username/PassArmor.git
       
       $ cd PassArmor

Install the required dependencies:

       $ pip install tkinter

Run the application:

       $ python passarmor.py

## Usage

    Enter a password in the Password field.
    Click the "Check" button to evaluate the strength and leakage status of the password.
    The result will be displayed in the Result label, indicating the strength and whether it is publicly leaked.
    Click the "Show" button to reveal the password in the Password field.
    Click the "Auto-Generate" button to generate a random password and populate it in the Password field.

## Screenshots:

![image](https://github.com/singhx-hub/PassArmor/assets/126919241/f139992e-701e-459d-a406-6c573ce8e5b4)

Checking for Leakage and password strength:

![image](https://github.com/singhx-hub/PassArmor/assets/126919241/ec1071eb-d7f4-4e42-b4fe-c9cf8fc6ce20)


Auto-Generate password checking:

![image](https://github.com/singhx-hub/PassArmor/assets/126919241/b6dc874c-c2bb-43e2-9ff7-bc593e15b809)



## Password Strength Criteria

    Minimum length: 8 characters
    Must contain at least one number
    Must contain at least one letter
    Must contain a mixture of letters, numbers, and special characters

## Password Leakage Check

PassArmor compares the entered password against a database of known leaked passwords. If the password is found in the database, it is flagged as publicly leaked.

## Note: 
The leakage check feature requires the file "leak.txt" to be present in the application directory. Ensure that the file is available and up to date for accurate results.

## Contributing

Contributions are welcome! If you have any ideas, enhancements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.


## Acknowledgements

PassArmor uses the following resources:

    Python
    tkinter
