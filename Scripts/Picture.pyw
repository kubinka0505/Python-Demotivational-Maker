Picture = Image.open(get(Config()["Image"]["URL"], stream=True).raw)

__New_Width = Config()["Max_Width"]
Percent = (__New_Width / float(Picture.size[0]))
__New_Height = int((float(Picture.size[1]) * float(Percent)))

Picture = Picture.resize((__New_Width, __New_Height), Image.LANCZOS)

if Picture.size[0] > Picture.size[1]:
	Size = (Picture.size[0],) * 2

if Picture.size[0] < Picture.size[1]:
	Size = (Picture.size[1],) * 2

if Picture.size[0] == Picture.size[1]:
	Size = (Picture.size[0],) * 2

Border_Size = Percentage(Picture.size[1], 1) // 2

Picture_Border = ImageOps.expand(Picture.copy(), border = Border_Size, fill = (0,) * 4)
Picture_Border = ImageOps.expand(Picture_Border, border = Border_Size, fill = (213,) * 3)