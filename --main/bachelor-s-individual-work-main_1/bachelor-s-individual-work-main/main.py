from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(str(value))


class Phone(Field):
    def __init__(self, value: str):
        value = str(value)
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        # Тести можуть передавати і str, і Name
        self.name = name if isinstance(name, Name) else Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Тести можуть передавати і str, і Phone
        phone_obj = phone if isinstance(phone, Phone) else Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        phone_str = phone.value if isinstance(phone, Phone) else str(phone)
        self.phones = [p for p in self.phones if p.value != phone_str]

    def edit_phone(self, old_phone, new_phone):
        old_str = old_phone.value if isinstance(old_phone, Phone) else str(old_phone)
        new_obj = new_phone if isinstance(new_phone, Phone) else Phone(new_phone)

        for i, p in enumerate(self.phones):
            if p.value == old_str:
                self.phones[i] = new_obj
                return

        # ВАЖЛИВО: якщо старого номера нема — має бути ValueError
        raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        phone_str = phone.value if isinstance(phone, Phone) else str(phone)
        for p in self.phones:
            if p.value == phone_str:
                return p
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        # record.name гарантовано Name, але лишимо захист
        key = record.name.value if isinstance(record.name, Name) else str(record.name)
        self.data[key] = record

    def find(self, name: str):
        return self.data.get(str(name))

    def delete(self, name: str):
        self.data.pop(str(name), None)
