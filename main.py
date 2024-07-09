from tkinter import *
import requests

FONT = ("Times", 20, "normal")
API_KEY = "please add your api_key"

window = Tk()
window.title("Akdeniz Hava Durumu")
window.config(padx=30, pady=30)
'''
def print_window_size():
    window.update_idletasks()  # Pencere öğelerinin tam olarak yerleşmesini sağlar
    width = window.winfo_width()
    height = window.winfo_height()
    print(f"Pencere boyutları: {width}x{height}")

# Pencere açıldığında boyutları yazdır
window.after(100, print_window_size)
'''
window.maxsize(781, 500)
window.minsize(781, 500)

weather_translation = {
    "clear sky": "açık",
    "few clouds": "az bulutlu",
    "scattered clouds": "parçalı bulutlu",
    "broken clouds": "çok bulutlu",
    "overcast clouds": "kapalı",
    "shower rain": "sağanak yağmurlu",
    "light rain": "hafif yağmurlu",
    "moderate rain": "orta şiddetli yağmurlu",
    "heavy rain": "yoğun yağmurlu",
    "thunderstorm": "fırtınalı",
    "snow": "karlı",
    "mist": "sisli",
    "haze": "puslu",
    "fog": "sis",
    "smoke": "dumanlı",
    "dust": "tozlu",
    "sand": "kum fırtınası",
    "squalls": "ani fırtına",
    "tornado": "kasırga",
    "drizzle": "çiseleme",
    "light intensity drizzle": "hafif çiseleme",
    "heavy intensity drizzle": "yoğun çiseleme",
    "light snow": "hafif kar",
    "heavy snow": "yoğun kar",
    "sleet": "sulu kar",
    "light shower sleet": "hafif sağanak sulu kar",
    "shower sleet": "sağanak sulu kar",
    "light rain and snow": "hafif yağmur ve kar",
    "rain and snow": "yağmur ve kar",
    "light shower snow": "hafif sağanak kar",
    "shower snow": "sağanak kar",
    "heavy shower snow": "yoğun sağanak kar",
    "rain": "yağmurlu",
    "heavy intensity rain": "yoğun yağmur"
}

photo = PhotoImage(file="akdeniziller.png")
photo_label = Label(image=photo)
photo_label.pack()


def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temp = weather_data['main']['temp']
        weather = weather_data['weather'][0]['description']
        weather_in_turkish = weather_translation.get(weather, weather)
        current_weather_label.config(text=f"{city_name} - Sıcaklık: {temp}°C, Durum: {weather_in_turkish}")
    else:
        current_weather_label.config(text="Hava durumu bilgisi alınamadı.")


isparta_button = Button(text="Isparta", relief="flat", borderwidth=0, bg="#fe80c0", command=lambda: get_weather("Isparta"))
isparta_button.place(x=120, y=70)

burdur_button = Button(text="Burdur", relief="flat", borderwidth=0, bg="#fe936c", command=lambda: get_weather("Burdur"))
burdur_button.place(x=55, y=115)

antalya_button = Button(text="Antalya", relief="flat", borderwidth=0, bg="#ffff91", command=lambda: get_weather("Antalya"))
antalya_button.place(x=120, y=155)

mersin_button = Button(text="Mersin", relief="flat", borderwidth=0, bg="#00f0ef", command=lambda: get_weather("Mersin"))
mersin_button.place(x=365, y=195)

adana_button = Button(text="Adana", relief="flat", borderwidth=0, bg="#ff9fa0", command=lambda: get_weather("Adana"))
adana_button.place(x=495, y=140)

hatay_button = Button(text="Hatay", relief="flat", borderwidth=0, bg="#6f9efe", command=lambda: get_weather("Hatay"))
hatay_button.place(x=560, y=235)

osmaniye_button = Button(text="Osmaniye", relief="flat", borderwidth=0, bg="#febd01", font=("Times", 8, "normal"), command=lambda: get_weather("Osmaniye"))
osmaniye_button.place(x=555, y=140)

maras_button = Button(text="Kahramanmaraş", relief="flat", borderwidth=0, bg="#b3fe3f", command=lambda: get_weather("Kahramanmaraş"))
maras_button.place(x=595, y=70)

info_label = Label(text="Hava durumu bilgisi almak istediğiniz şehrin ismine tıklayınız", font=FONT)
info_label.pack()

current_weather_label = Label(text="", font=("Times", 15, "normal"))
current_weather_label.pack()

window.mainloop()
