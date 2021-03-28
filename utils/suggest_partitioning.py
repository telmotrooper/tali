def suggest_partitioning():
  print("\nPlease, set your partitions now, format and mount them on " + yellow("/mnt") + ".")
  print("If all you want to do is to wipe all partitions and install " + cyan("Arch Linux") + ", you can run " + green("tali/quick_partitioning.py") + ".")
  print("Otherwise, you can format your partitions yourself with " + green("parted") + " or a similar tool.")
  print("\nWhen you're done, run " + green("tali/install.py") + " again.\n")
