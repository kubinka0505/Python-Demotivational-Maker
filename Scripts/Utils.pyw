def Percentage(Percent: int, Whole: int) -> int:
	return (Percent * Whole) // 100

def Config() -> load:
	"""Loading values from JSON file."""
	__Path = "{0}\Config.json"
	#---#
	if system() != "Windows":
		__Path = __Path.replace("\\", "/")
	#---#
	return load(open(__Path.format(os.getcwd()), encoding = "utf-8"))

def Random_String(Length: int = 16) -> str:
	"""Random string creation used in saving files."""
	return "".join(choice(printable[0:62]) for String in range(Length))
