
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    def set_wife(self, wife: dict) -> None:
        """Присваиваем жену"""
        self.wife = wife
        wife.husband = self

    def set_husband(self, husband: dict) -> None:
        """Присваиваем мужа"""
        self.husband = husband
        husband.wife = self


def create_person_list(person_data: list) -> list:
    """Создает список из всех элементов словаря"""
    person_list = []
    for data in person_data:
        person = Person(data["name"], data["age"])
        person_list.append(person)

        # Присваиваем супругов
        if "wife" in data and data["wife"]:
            wife = next(
                (p for p in person_list if p.name == data["wife"]), None
            )
            if wife:
                person.set_wife(wife)

        if "husband" in data and data["husband"]:
            husband = next(
                (p for p in person_list if p.name == data["husband"]), None
            )
            if husband:
                person.set_husband(husband)

    return person_list
