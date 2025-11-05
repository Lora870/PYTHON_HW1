from smartphone import Smartphone

catalog = [
    Smartphone("Honor", "200Lite ", "+79123456789"),
    Smartphone("Apple", "iPhone 14", "+79223334455"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79335556677"),
    Smartphone("Huawei", "P60 Pro", "+79447778899"),
    Smartphone("Samsung", "Galaxy S21", "+79550001122")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")