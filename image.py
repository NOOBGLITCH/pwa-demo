import os
from PIL import Image

def build_browserplay_assets(input_img="image.png"):
    # Define directory structure
    directories = ['icons', 'images']
    for folder in directories:
        os.makedirs(folder, exist_ok=True)
    
    if not os.path.exists(input_img):
        print(f"Error: {input_img} not found. Please place your logo as {input_img} in this folder.")
        return

    try:
        with Image.open(input_img) as img:
            print("Processing BrowserPlay assets...")

            # --- ICONS (Lossless PNG) ---
            # Standard PWA Icons
            img.resize((192, 192), Image.Resampling.LANCZOS).save("icons/icon-192x192.png", "PNG")
            img.resize((512, 512), Image.Resampling.LANCZOS).save("icons/icon-512x512.png", "PNG")
            
            # Shortcut Icon (96x96 as requested in manifest)
            img.resize((96, 96), Image.Resampling.LANCZOS).save("icons/icon-96x96.png", "PNG")

            # --- FAVICON (Standard Browser .ico) ---
            # Creates a multi-resolution .ico for standard browser tabs
            img.resize((32, 32), Image.Resampling.LANCZOS).save("favicon.ico", format='ICO', sizes=[(32, 32)])

            # --- SCREENSHOTS ---
            # Mobile Home Screen (Narrow)
            img.resize((540, 720), Image.Resampling.LANCZOS).save("images/screenshot1.png", "PNG")
            
            # Desktop Home Screen (Wide)
            # JPG conversion requires RGB mode
            if img.mode in ("RGBA", "P"):
                img_rgb = img.convert("RGB")
                img_rgb.resize((720, 540), Image.Resampling.LANCZOS).save("images/screenshot2.jpg", "JPEG", quality=95)
            else:
                img.resize((720, 540), Image.Resampling.LANCZOS).save("images/screenshot2.jpg", "JPEG", quality=95)

            print("✅ All directories created.")
            print("✅ Lossless icons and high-quality screenshots generated.")
            print("✅ favicon.ico created for browser tabs.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    build_browserplay_assets()