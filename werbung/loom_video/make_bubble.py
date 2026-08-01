from PIL import Image, ImageDraw

src_path = r"C:\users\ASUS Zenbook\Desktop\me.jpg"
out_path = r"C:\Claude\Franz\MyTM\loom_video\webcam_bubble.png"

SIZE = 320
RING = 8
CANVAS = SIZE + RING * 2

img = Image.open(src_path).convert("RGB")

w, h = img.size
side = min(w, h)
left = (w - side) // 2
top = (h - side) // 2
img = img.crop((left, top, left + side, top + side))
img = img.resize((SIZE, SIZE), Image.LANCZOS)

mask = Image.new("L", (SIZE, SIZE), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, SIZE, SIZE), fill=255)

circle_img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
circle_img.paste(img, (0, 0), mask)

canvas = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
ring_draw = ImageDraw.Draw(canvas)
ring_draw.ellipse((0, 0, CANVAS, CANVAS), fill=(255, 255, 255, 255))
canvas.paste(circle_img, (RING, RING), circle_img)

canvas.save(out_path)
print("saved", out_path, canvas.size)
