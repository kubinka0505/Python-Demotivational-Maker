Demotivational = Image.new("RGBA", (
	Percentage(
		Picture_Border.size[0], 125
		),
	Percentage(
		Picture_Border.size[1] + \
		Title_Image.size[1] + \
		Content_Image.size[1], 125
		)),
	(0,) * 4
	)

LINE_OFFSET = Config()["Title_Size"] // 2

Demotivational.paste(Picture_Border, ((Demotivational.size[0] - Picture_Border.size[0]) // 2, LINE_OFFSET))
if Config()["Content"]["Title"] == "":
	Demotivational.paste(Content_Image, ((Demotivational.size[0] - Content_Image.size[0]) // 2, Picture_Border.size[1] + LINE_OFFSET * 3), Content_Image)
if Config()["Content"]["Title"] != "":
	Demotivational.paste(Title_Image, ((Demotivational.size[0] - Title_Image.size[0]) // 2, Picture_Border.size[1] + LINE_OFFSET * 3), Title_Image)
	Demotivational.paste(Content_Image, ((Demotivational.size[0] - Content_Image.size[0]) // 2, Picture_Border.size[1] + LINE_OFFSET * 6 + Title_Image.size[1]), Content_Image)
Demotivational = Demotivational.crop(Demotivational.getbbox())

Demotivational_Crop = Image.new("RGB", (Demotivational.size[0] + LINE_OFFSET * 3, Demotivational.size[1] + LINE_OFFSET * 4), (0,) * 3)
Demotivational_Crop.paste(Demotivational, ((Demotivational_Crop.size[0] - Demotivational.size[0]) // 2,(Demotivational_Crop.size[1] - Demotivational.size[1]) // 2), Demotivational)
