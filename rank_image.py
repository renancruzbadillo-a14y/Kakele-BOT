from PIL import Image, ImageDraw, ImageFont
import os

def criar_imagem_ranking(ranking, tipo="LEVEL"):
    os.makedirs("data", exist_ok=True)

    largura = 900
    linha_altura = 28
    top = 100
    max_linhas = 50
    altura = top + (linha_altura * max_linhas) + 40

    img = Image.new("RGB", (largura, altura), "#1e1e2e")
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arial.ttf", 38)
        font_text = ImageFont.truetype("arial.ttf", 22)
    except:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()

    draw.text((largura // 2 - 220, 30),
              f"🏆 RANKING {tipo} — TOP 50",
              fill="#f1c40f",
              font=font_title)

    y = top
    for i, line in enumerate(ranking[:50]):
        cor = "#ffffff"
        if i == 0:
            cor = "#ffd700"
        elif i == 1:
            cor = "#c0c0c0"
        elif i == 2:
            cor = "#cd7f32"

        draw.text((40, y), f"#{i+1:02}", fill=cor, font=font_text)
        draw.text((110, y), line, fill="white", font=font_text)
        y += linha_altura

    path = "data/ranking_top50.png"
    img.save(path)
    return path
