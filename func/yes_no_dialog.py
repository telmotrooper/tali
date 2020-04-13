def yes_no_dialog(text):
  answer = "hello"

  while (answer.lower() != "y" and answer.lower() != "n" and answer != ""):
    answer = input(f"{text} (Y/n) ")
    if (answer.lower() != "y" and answer.lower() != "n" and answer != ""):
      print("Invalid input")

  return answer.lower() == "y" or answer == ""
