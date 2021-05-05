Title_Image = Image.new("RGBA", (10000,) * 2, (0,) * 4)
Title_Text = "\n".join(wrap(Config()["Content"]["Title"], 20))

if len(Title_Text) == 0: Title_Text = " "

__Font = "{0}\\Times New Roman.ttf".format(os.getcwd())

if system() != "Windows":
	__Font = __Font.replace("\\", "/")

__Font = ImageFont.truetype(__Font, Config()["Title_Size"] * 3)
Draw_Title_Image = ImageDraw.Draw(Title_Image)
Draw_Title_Image.text(
	xy = (0, 0),
	text = Title_Text,
	fill = (255,) * 3,
	font = __Font,
	align = "center"
	)

Title_Image = Title_Image.crop(Title_Image.getbbox())