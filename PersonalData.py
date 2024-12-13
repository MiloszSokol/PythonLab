import json

class PersonalData:

    def __init__(self, name, surname, address, code, pesel):
        self.name = name
        self.surname = surname
        self.address = address
        self.code = code
        self.pesel = pesel

    def save_to_json(self, filename):
        if not filename.endswith('.json'):
            filename += '.json'

        data = {
            'name': self.name,
            'surname': self.surname,
            'address': self.address,
            'code': self.code,
            'pesel': self.pesel
        }

        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_json(self, filename):
        if not filename.endswith('.json'):
            filename += '.json'

        with open(filename) as f:
            data = json.load(f)

            self.name = data['name']
            self.surname = data['surname']
            self.address = data['address']
            self.code = data['code']
            self.pesel = data['pesel']

if __name__ == "__main__":

    person = PersonalData("Jadwiga", "Hymel", "Lipinki Luzyckie Laczna 43", "23-679", "89383928436")

    person.save_to_json("data")
    person.load_from_json("data")



