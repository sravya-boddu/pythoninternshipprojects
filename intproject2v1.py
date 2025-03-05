# Functional Word Counter Project

def get_user_input():
    
    return input("Enter a sentence or paragraph (press Enter to quit): ").strip()

def count_words(text):
    
   
    if not text:
        return 0
    

    return len(text.split())

def display_word_count(count):
    
    print(f"\n--- Word Count: {count} words ---\n")

def word_counter_app():
    
    print("Welcome to the Functional Word Counter!")
    print("----------------------------------------")
    

    while True:
        try:
            
            user_text = get_user_input()
            
  
            if not user_text:
                print("Thank you for using Word Counter. Goodbye!")
                break
            
  
            word_count = count_words(user_text)
            display_word_count(word_count)
        
        except Exception as e:
   
            print(f"Oops! An error occurred: {e}")


if __name__ == "__main__":
    word_counter_app()
