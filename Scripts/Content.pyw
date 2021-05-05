Content_Image = Image.new("RGBA", (10000,) * 2, (0,) * 4)
Content_Text = "\n".join(wrap(Config()["Content"]["Text"], 62))

if len(Content_Text) == 0: Content_Text = " "

__Font = "{0}\\Times New Roman.ttf".format(os.getcwd())

if system() != "Windows":
	__Font = __Font.replace("\\", "/")

__Font = ImageFont.truetype(__Font, Config()["Title_Size"])
Draw_Title_Image = ImageDraw.Draw(Content_Image)
Draw_Title_Image.text(
	xy = (0, 0),
	text = Content_Text,
	fill = (255,) * 3,
	font = __Font,
	align = "center"
	)

Content_Image = Content_Image.crop(Content_Image.getbbox())