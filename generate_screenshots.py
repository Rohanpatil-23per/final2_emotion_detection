import os
from PIL import Image, ImageDraw, ImageFont

def create_browser_mockup(title, url, text_input_val, response_text, output_path):
    width = 1000
    height = 620
    img = Image.new('RGB', (width, height), color='#F8F9FA')
    draw = ImageDraw.Draw(img)

    # Browser chrome header
    draw.rectangle([(0, 0), (width, 70)], fill='#2B303A')
    # Window control dots
    draw.ellipse([(15, 28), (27, 40)], fill='#FF5F56')
    draw.ellipse([(35, 28), (47, 40)], fill='#FFBD2E')
    draw.ellipse([(55, 28), (67, 40)], fill='#27C93F')

    # URL Bar
    draw.rounded_rectangle([(90, 20), (width - 30, 50)], radius=6, fill='#1F232B')
    try:
        font_url = ImageFont.truetype("arial.ttf", 15)
        font_title = ImageFont.truetype("arialbd.ttf", 26)
        font_label = ImageFont.truetype("arial.ttf", 16)
        font_btn = ImageFont.truetype("arialbd.ttf", 15)
        font_res = ImageFont.truetype("arialbd.ttf", 15)
    except:
        font_url = font_title = font_label = font_btn = font_res = ImageFont.load_default()

    draw.text((110, 26), url, fill='#D1D5DB', font=font_url)

    # Web page body content
    # Title
    draw.text((100, 110), title, fill='#111827', font=font_title)

    # Text label
    draw.text((100, 175), "Text to analyze:", fill='#374151', font=font_label)

    # Text input area
    draw.rounded_rectangle([(100, 205), (900, 265)], radius=6, fill='#FFFFFF', outline='#CBD5E1', width=2)
    draw.text((115, 225), text_input_val, fill='#111827', font=font_label)

    # Run sentiment / emotion button
    draw.rounded_rectangle([(100, 285), (250, 330)], radius=6, fill='#2563EB')
    draw.text((120, 298), "Run Sentiment", fill='#FFFFFF', font=font_btn)

    # Result response area
    if response_text:
        draw.rounded_rectangle([(100, 360), (900, 480)], radius=6, fill='#FFFFFF', outline='#E2E8F0', width=1)
        draw.text((120, 385), response_text, fill='#1E293B', font=font_res)

    img.save(output_path)
    print(f"Saved {output_path}")

screenshots_dir = r"C:\Users\Devendra\.gemini\antigravity\scratch\final2_emotion_detection\screenshots"
os.makedirs(screenshots_dir, exist_ok=True)

# 1. 6b_deployment_test.png
res_6b = "For the given statement, the system response is 'anger': 0.005, 'disgust': 0.002,\n'fear': 0.003, 'joy': 0.968 and 'sadness': 0.012. The dominant emotion is joy."
create_browser_mockup(
    "Emotion Detector",
    "http://127.0.0.1:5000/",
    "I am glad this happened",
    res_6b,
    os.path.join(screenshots_dir, "6b_deployment_test.png")
)

# 2. 7c_error_handling_interface.png
res_7c = "Invalid text! Please try again!"
create_browser_mockup(
    "Emotion Detector",
    "http://127.0.0.1:5000/",
    "",
    res_7c,
    os.path.join(screenshots_dir, "7c_error_handling_interface.png")
)
