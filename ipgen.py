import random
import requests
from faker import Faker
from fake_useragent import UserAgent

"""
WoxicDEV - 2024 
Instagram - mertt.js_
LinkedIn : Mert Ali Kaya
chiefdelphi : mrtalikyaa
medium : mrtalikyaa
İlk sürüm olduğundan arayüz eklemedim ikinci sürümde yeni seçimler ile beraber getireceğim.
Aklınıza eklenebilecek herhangi bir şey gelirse belirttiğim sosyal medya hesaplarından bana ulaşabilirsiniz.
Kütüphane bilgisi ReadMe dosyasında belirtilmiştir.

"""
fake = Faker()
ua = UserAgent()

print(" __      __        .__   __                 ")
print("/  \    /  \___.__.|  |_/  |_  ____ ___  ___")
print("\   \/\/   <   |  ||  |\   __\/ __ \\  \/  /")
print(" \        / \___  ||  |_|  | \  ___/ >    < ")
print("  \__/\  /  / ____||____/__|  \___  >__/\_ \ ")
print("       \/   \/                    \/      \/")
print("                              -Fake IP Log Generator              ")

# Para birimini ülkeye göre belirlemek için basit bir harita
country_currency_map = {
    "United States": "USD",
    "Turkey": "TRY",
    "Germany": "EUR",
    "Japan": "JPY",
    "United Kingdom": "GBP",
    "Canada": "CAD",
    "Australia": "AUD",
    "Switzerland": "CHF",
    "Russia": "RUB",
    "China": "CNY",
    "India": "INR",
    "Brazil": "BRL",
    "Mexico": "MXN",
    "South Africa": "ZAR",
    "South Korea": "KRW",
    "Argentina": "ARS",
    "New Zealand": "NZD",
    "Sweden": "SEK",
    "Norway": "NOK",
    "Denmark": "DKK",
    "Singapore": "SGD",
    "Malaysia": "MYR",
    "Thailand": "THB",
    "Indonesia": "IDR",
    "Philippines": "PHP",
    "Vietnam": "VND",
    "Israel": "ILS",
    "Saudi Arabia": "SAR",
    "United Arab Emirates": "AED",
    "Egypt": "EGP",
    "Pakistan": "PKR",
    "Bangladesh": "BDT",
    "Nigeria": "NGN",
    "Kenya": "KES",
    "Ghana": "GHS",
    "Colombia": "COP",
    "Chile": "CLP",
    "Venezuela": "VES",
    "Peru": "PEN",
    "Poland": "PLN",
    "Czech Republic": "CZK",
    "Hungary": "HUF",
    "Romania": "RON",
    "Bulgaria": "BGN",
    "Croatia": "HRK",
    "Iceland": "ISK",
    "Ukraine": "UAH",
    "Kazakhstan": "KZT",
    "Uzbekistan": "UZS",
    "Morocco": "MAD",
    "Tunisia": "TND",
    "Algeria": "DZD",
    "Qatar": "QAR",
    "Kuwait": "KWD",
    "Bahrain": "BHD",
    "Oman": "OMR",
    "Sri Lanka": "LKR",
    "Nepal": "NPR",
    "Bhutan": "BTN",
    "Myanmar": "MMK",
    "Cambodia": "KHR",
    "Laos": "LAK",
    "Mongolia": "MNT",
    "Maldives": "MVR",
    "Seychelles": "SCR",
    "Mauritius": "MUR",
    "Botswana": "BWP",
    "Zambia": "ZMW",
    "Zimbabwe": "ZWL",
    "Sudan": "SDG",
    "Iraq": "IQD",
    "Lebanon": "LBP",
    "Jordan": "JOD",
    "Syria": "SYP",
    "Libya": "LYD",
    "Somalia": "SOS",
    "Ethiopia": "ETB",
    "Tanzania": "TZS",
    "Uganda": "UGX",
    "Ivory Coast": "XOF",
    "Senegal": "XOF",
    "Mali": "XOF",
    "Niger": "XOF",
    "Burkina Faso": "XOF",
    "Togo": "XOF",
    "Benin": "XOF",
    "Guinea": "GNF",
    "Sierra Leone": "SLL",
    "Liberia": "LRD",
    "Fiji": "FJD",
    "Papua New Guinea": "PGK",
    "Solomon Islands": "SBD",
    "Samoa": "WST",
    "Vanuatu": "VUV"
    # Daha fazla ülke ekleneybilirsiniz
}

# Konuma göre para birimi belirleme fonksiyonu
def get_currency_by_country(country):
    return country_currency_map.get(country, "Unknown")

# IP'ye göre konum bilgisi almak için fonksiyon (ip-api kullanıyorum değiştirebilirsiniz)
def get_location_data(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Hata: {e}")
    return None

# Rastgele cihaz ve işletim sistemi bilgileri üretme(bazen çelişki oluyor v2 gelirse düzelteceğim)
def generate_device_info():
    devices = ['Mobile', 'Tablet', 'Desktop', 'Laptop']
    operating_systems = ['Android', 'iOS', 'Windows', 'macOS', 'Linux']
    device = random.choice(devices)
    os = random.choice(operating_systems)
    return device, os

# Sahte bilgi üretme fonksiyonları
def generate_fake_info():
    ip = fake.ipv4_public()
    location_data = get_location_data(ip)
    if location_data:
        country = location_data.get('country', 'Unknown')
        city = location_data.get('city', 'Unknown')
        latitude = location_data.get('lat', 0)
        longitude = location_data.get('lon', 0)
        currency = get_currency_by_country(country)
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    else:
        country, city, latitude, longitude, currency, google_maps_link = 'Unknown', 'Unknown', 0, 0, 'Unknown', 'Unknown'
    
    # Tarayıcı bilgisi (User Agent)
    user_agent = ua.random

    # Cihaz ve OS bilgisi
    device, os = generate_device_info()

    # Sonuçları ekrana yazdırma
    print(f"IP Adresi: {ip}")
    print(f"Ülke: {country}")
    print(f"Şehir: {city}")
    print(f"Enlem: {latitude}")
    print(f"Boylam: {longitude}")
    print(f"Para Birimi: {currency}")
    print(f"Google Maps Linki: {google_maps_link}")
    print(f"Tarayıcı (User Agent): {user_agent}")
    print(f"Cihaz: {device}")
    print(f"İşletim Sistemi: {os}")
    print("-" * 50)

# Kaç adet sahte bilgi üretilecek onu belirleme
def main():
    try:
        num_of_entries = int(input("Kaç adet sahte bilgi üretmek istiyorsunuz? "))
        for _ in range(num_of_entries):
            generate_fake_info()
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
