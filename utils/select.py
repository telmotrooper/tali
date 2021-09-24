def select(text: str, options: dict[str, str]) -> str:
  print(text)

  for i, option in enumerate(options):
    print(f"{i+1}. {option}")
  
  user_input = 0

  while(user_input < 1 or user_input > len(options)):
    try:
      user_input = input("Select option (default = 1): ")

      if(user_input == ""):
        user_input = 1
      else:
        user_input = int(user_input)
      
      if(user_input < 1 or user_input > len(options)):
        raise ValueError
    
    except ValueError:
      print("Invalid input")
      user_input = 0
      continue

  return list(options.values())[user_input - 1]
