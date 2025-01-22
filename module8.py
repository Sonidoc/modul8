import os
os.system('cls')

def my_function():
     return "you're funny"

def my_name():
    print(my_name)

def my_function():
    print("hello from my function!")

def add(a,b):
    return a + b

#NAMNLISTA

def add_name(name_list, name):
    """Lägg till ett namn i listan."""
    name_list.append(name)

def remove_name(name_list, name):
    """Ta bort ett namn från listan om det finns."""
    if name in name_list:
        name_list.pop(name)

def update_name(name_list, old_name, new_name):
    """Ändra ett namn i listan om det finns."""
    if old_name in name_list:
        index = name_list.index(old_name)
        name_list[index] = new_name


names = []
os.system('cls')



while True:
    
    print("\nAktuell lista:", names)
    print("1: Lägg till namn")
    print("2: Ta bort namn")
    print("3: Ändra namn")
    print("4: Avsluta")

    try:
        choice = int(input("Välj ett alternativ: "))
    except ValueError:
        print("Vänligen ange ett giltigt nummer!")
        continue

    if choice == 1:
        new_name = input("Ange namn att lägga till: ").strip()
        add_name(names, new_name)
    elif choice == 2:
        remove_name_input = input("Ange namn att ta bort: ").strip()
        remove_name(names, remove_name_input)
    elif choice == 3:
        old_name = input("Ange namnet som ska ändras: ").strip()
        new_name = input("Ange det nya namnet: ").strip()
        update_name(names, old_name, new_name)
    elif choice == 4:
        again = input("Vill du fortsätta? (ja/n): ").strip().lower()
        if again == "n":
            print("Hej då!")
            exit()
        
        print("Avslutar programmet. Tack!")
        
    else:
            print("Ogiltigt val, försök igen.")
  




# 
# while True:
        
# ADDITIONSRÄKNARE!

#     a = int(input("Välkommen till addition! Skriv ett tal: "))
#     b = int(input("Ett annat: "))
#     print(add(a, b))



                  
#     again = input("Vill du fortsätta? (j/n): ").strip().lower()
#     if again == "n":
#         print("Hej då!")
#         break 

#MINIRÄKNARE
 #   def calculator(num1, num2, operation):
 #       if operation == "+":
 #           return num1 + num2 
 #       elif operation == "-":
 #           return num1 - num2 
 #       elif operation == "*":
 #           return num1 * num2
 #     elif operation == "/":
 #           if num2 != 0:                
 #               return num1 / num2
 #           else: 
 #               return "Division med noll kan du ej göra"
 #       else:
 #           return "Nej."

    
        
 #   print("Välkommen till miniräknare!")
 #   print("Skriv här!:")
 #   num1 = float(input("Ange det första numret:"))
 #   operation = input("Ange operation (+, -, *, /): ")
 #   num2 = float(input("Ange det andra numret: "))
   

   
 #   result = calculator(num1, num2, operation)
 #   print(f"Resultatet är: {result}")
