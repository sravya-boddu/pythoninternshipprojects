import random
import string

class UsernameGenerator:
    def __init__(self):

        self.adjectives = [
            "Cool", "Happy", "Brave", "Swift", "Clever", "Bright",
            "Wild", "Silent", "Magic", "Royal", "Golden", "Silver"
        ]
        
        self.nouns = [
            "Tiger", "Dragon", "Warrior", "Phoenix", "Eagle", "Wolf",
            "Ninja", "Wizard", "Knight", "Falcon", "Lion", "Dolphin"
        ]
        
    def generate_basic_username(self):
    
        adj = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        return f"{adj}{noun}"
    
    def add_numbers(self, username, length=2):
        
        numbers = ''.join(random.choices(string.digits, k=length))
        return f"{username}{numbers}"
    
    def add_special_chars(self, username):
        
        special_chars = "!@#$%^&*"
        char = random.choice(special_chars)
        return f"{username}{char}"
    
    def generate_custom_username(self, include_numbers=True, include_special=False):
       
        username = self.generate_basic_username()
        
        if include_numbers:
            username = self.add_numbers(username)
        
        if include_special:
            username = self.add_special_chars(username)
        
        return username
    
    def save_to_file(self, usernames, filename="usernames.txt"):
        
        try:
            with open(filename, 'w') as file:
                for username in usernames:
                    file.write(username + '\n')
            print(f"Usernames have been saved to '{filename}'")
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

def main():
    
    generator = UsernameGenerator()
    
    
    print("Welcome to the Username Generator!")
    print("----------------------------------")
    
    try:
        
        num_usernames = int(input("How many usernames would you like to generate? "))
        include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
        
        
        usernames = []
        for _ in range(num_usernames):
            username = generator.generate_custom_username(
                include_numbers=include_numbers,
                include_special=include_special
            )
            usernames.append(username)
        
        
        print("\nGenerated Usernames:")
        print("-------------------")
        for username in usernames:
            print(username)
        
        
        save_to_file = input("\nWould you like to save these usernames to a file? (yes/no): ").lower() == 'yes'
        if save_to_file:
            generator.save_to_file(usernames)
        else:
            print("Failed to save files - User chose not to save")
                
    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
