def color_total():
    from IPython.core.display import HTML
    from IPython.display import Image
    from collections import Counter
    import json

    from plotly.offline import init_notebook_mode, iplot
    import matplotlib.pyplot as plt
    import plotly.graph_objs as go

    from plotly import tools
    from PIL import Image
    from PIL import ImageEnhance

    import tensorflow as tf
    import numpy as np
    #import css

    img = Image.open('camera.png')
    enhancer = img.getdata()
    enhancer = ImageEnhance.Brightness(img)
    enhancer.enhance(1.5).save('camera.png', "PNG")

    img = Image.open('camera.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    cutOff = 255

    for item in datas:
        if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
            newData.append((255, 255, 255, 0))  # 배경제거
        else:
            newData.append(item)

    img.putdata(newData)
    img.save('camera.png', "PNG")  # 배경제거 이미지 저장

    from PIL import Image

    im = Image.open('camera.png')
    im2 = im.crop((530, 200, 700, 400))
    im2.save('sample.png')

    from PIL import Image
    import urllib
    from io import StringIO

    img = Image.open('sample.png')

    rgbimg = img.convert('RGB')
    average_colors = {}

    def compute_average_image_color(img):
        rgbimg = img.convert('RGB')
        width, height = img.size
        count, r_total, g_total, b_total = 0, 0, 0, 0
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = rgbimg.getpixel((x, y))
                r_total += r
                g_total += g
                b_total += b
                count += 1
        return (r_total / count, g_total / count, b_total / count)

    from IPython.core.display import HTML
    # from IPython.display import Image

    img = Image.open('sample.png')

    average_color = compute_average_image_color(img)
    if average_color not in average_colors:
        average_colors[average_color] = 0
    average_colors[average_color] += 1

    for average_color in average_colors:
        average_color1 = (int(average_color[0]), int(average_color[1]), int(average_color[2]))
        image_url = "<span style='display:inline-block; min-width:200px; background-color:rgb" + str(
            average_color1) + ";padding:10px 10px;'>" + str(average_color1) + "</span>"
        #     print (image_url)
        #display(HTML(image_url))

    import webcolors

    def closest_colour(requested_colour):
        min_colours = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def get_colour_name(requested_colour):
        try:
            closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
        except ValueError:
            closest_name = closest_colour(requested_colour)
            actual_name = None
        return actual_name, closest_name

    requested_colour = (average_color1)
    actual_name, closest_name = get_colour_name(requested_colour)
    if actual_name==None:
       # print("이 옷의 색상은",closest_name)
        return closest_name
    else:
       # print("이 옷의 색상은",actual_name)
        return actual_name

color_total()
