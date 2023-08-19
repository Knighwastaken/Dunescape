# Knights Nick Name generator
def generate_nickname(name):
    # You can implement your own logic here to generate a nickname based on the user's name
    # For simplicity, let's just add "y" at the end of the name
    nickname = name + "y"
    return nickname

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    if age < 0 or age > 120:
        print("Invalid age entered!")
        return
    
    like_nickname = input("Do you like nicknames? (yes/no): ")
    
    if like_nickname.lower() == "yes":
        nickname = generate_nickname(name)
        print(f"Your nickname is: {nickname}")
    else:
        print("No problem! Have a great day!")

if __name__ == "__main__":
    main()

