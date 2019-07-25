def select_disk():
  fake_input ="""/dev/sda: 12 GiB,
/dev/loop0: 502.41 MiB,"""
  fake_input = fake_input.replace(': ', ' (').replace(',', ')')
  fake_input = fake_input.splitlines()

  for i, disk in enumerate(fake_input):
    print(f"{i+1}. {disk}")
  
  user_input = 0

  while(user_input < 1 or user_input > len(fake_input)):
    try:
      user_input = int(input("Select a disk: "))
    except ValueError:
      print("Invalid input")
      continue

select_disk()
