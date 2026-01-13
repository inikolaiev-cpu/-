from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or (not value.isdigit()) or len(value) != 10:
            raise ValueError("Invalid phone number")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = name if isinstance(name, Name) else Name(str(name))
        self.phones = []

    def _to_phone(self, phone):
        return phone if isinstance(phone, Phone) else Phone(str(phone))

    def add_phone(self, phone):
        self.phones.append(self._to_phone(phone))

    def remove_phone(self, phone):
        phone = self._to_phone(phone)
        self.phones = [p for p in self.phones if p.value != phone.value]

    def edit_phone(self, old_phone, new_phone):
        old_phone = self._to_phone(old_phone)
        new_phone = self._to_phone(new_phone)
        for i, p in enumerate(self.phones):
            if p.value == old_phone.value:
                self.phones[i] = new_phone
                return
        raise ValueError("Phone not found")

    def find_phone(self, phone):
        phone = self._to_phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                return p
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        key = name.value if isinstance(name, Name) else str(name)
        return self.data.get(key)

    def delete(self, name):
        key = name.value if isinstance(name, Name) else str(name)
        if key in self.data:
            del self.data[key]
