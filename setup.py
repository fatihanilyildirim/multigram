import subprocess
import sys

required_packages = [
    "PyQt5>=5.15.0",
    "qtawesome>=1.1.0",
    "requests>=2.25.0",
    "beautifulsoup4>=4.9.0",
    "firebase-admin>=6.0.0",
    "pytz>=2020.1",
    "apscheduler>=3.6.0",
    "instagrapi>=1.15.0",
    "cryptography>=3.4.0",
    "opencv-python>=4.5.0"
]

def install_packages():
    for package in required_packages:
        print(f"📦 Yükleniyor: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages()
    print("\n✅ Tüm kütüphaneler başarıyla yüklendi.")
