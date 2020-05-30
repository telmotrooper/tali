def select_kernel() -> str:
  print("Which kernel do you want to install?")
  kernel_options = dict([
    ("Zen + Mainline (recommended)", "linux-zen linux-zen-headers linux linux-headers"),
    ("Zen", "linux-zen linux-zen-headers"),
    ("Mainline", "linux linux-headers")
  ])

  for i, disk in enumerate(kernel_options):
    print(f"{i+1}. {disk}")
  
  user_input = 0

  while(user_input < 1 or user_input > len(kernel_options)):
    try:
      user_input = input("Select option (default = 1): ")

      if(user_input == ""):
        user_input = 1
      else:
        user_input = int(user_input)
      
      if(user_input < 1 or user_input > len(kernel_options)):
        raise ValueError
    
    except ValueError:
      print("Invalid input")
      user_input = 0
      continue

  return list(kernel_options.values())[user_input - 1]
