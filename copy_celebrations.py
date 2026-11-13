import shutil

img1 = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\celebration_reception_empty_stage_1794579216383.jpg"
img2 = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\celebration_housewarming_illuminated_exterior_1794579246578.jpg"
img3 = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\silver_jubilee_anniversary_stage_1794571037049.jpg"

shutil.copyfile(img1, "assets/images/celebration_reception_empty_stage.jpg")
shutil.copyfile(img2, "assets/images/celebration_housewarming_illuminated_exterior.jpg")
shutil.copyfile(img3, "assets/images/celebration_silver_jubilee_stage.jpg")

print("All 3 celebration images copied to assets/images successfully!")
