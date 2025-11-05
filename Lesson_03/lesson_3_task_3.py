from address import Address
from mailing import Mailing

# Создаём адреса
from_addr = Address("634351", "Качканар", "Свердлова", "10", "178")
to_addr = Address("634000", "Екатеринбург", "Черепанова", "20", "12")

# Создаём экземпляр Mailing
mailing = Mailing(to_addr, from_addr, 250, "RU123456789")

# Выводим в формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")