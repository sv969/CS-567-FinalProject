class Pet:
    def __init__(self, pet_id, name, species, age, description, medical_record=None):
        self.pet_id = pet_id
        self.name = name
        self.species = species
        self.age = age
        self.description = description
        self.adopted = False
        self.medical_record = medical_record or {}

    def adopt(self):
        if not self.adopted:
            self.adopted = True
            return f"{self.name} has been adopted!"
        return f"{self.name} is already adopted."

    def update_medical_record(self, record):
        self.medical_record.update(record)
        return "Medical record updated."

    def get_medical_history(self):
        return self.medical_record

    def is_adoptable(self):
        return not self.adopted and 'health' in self.medical_record and self.medical_record['health'] == 'good'

    def age_up(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."

    def change_description(self, new_description):
        self.description = new_description
        return "Description updated."

    def __str__(self):
        adopt_status = "Adopted" if self.adopted else "Available"
        return f"{self.name} - {self.species}, Age: {self.age}, Status: {adopt_status}, Description: {self.description}"

class Volunteer:
    def __init__(self, volunteer_id, name):
        self.volunteer_id = volunteer_id
        self.name = name
        self.hours_logged = 0

    def log_hours(self, hours):
        self.hours_logged += hours
        return f"{hours} hours logged by {self.name}. Total hours: {self.hours_logged}."

    def __str__(self):
        return f"Volunteer: {self.name}, Total Hours: {self.hours_logged}"

class Event:
    def __init__(self, event_id, title, description, date):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.date = date
        self.participants = []

    def add_participant(self, participant):
        if participant not in self.participants:
            self.participants.append(participant)
            return f"{participant.name} has been added to the event {self.title}."
        return f"{participant.name} is already registered for {self.title}."

    def list_participants(self):
        return "\n".join(participant.name for participant in self.participants)

    def __str__(self):
        return f"Event: {self.title} on {self.date}, Description: {self.description}"

class AdoptionCenter:
    def __init__(self):
        self.pets = {}
        self.inquiries = {}
        self.volunteers = {}
        self.events = {}

    def add_volunteer(self, volunteer_id, name):
        if volunteer_id not in self.volunteers:
            new_volunteer = Volunteer(volunteer_id, name)
            self.volunteers[volunteer_id] = new_volunteer
            return f"Volunteer {name} added."
        return "Volunteer already exists."

    def organize_event(self, event_id, title, description, date):
        if event_id not in self.events:
            new_event = Event(event_id, title, description, date)
            self.events[event_id] = new_event
            return f""
        return "Event already exists."

    def register_for_event(self, event_id, volunteer_id):
        if event_id in self.events and volunteer_id in self.volunteers:
            return self.events[event_id].add_participant(self.volunteers[volunteer_id])
        return "Event or volunteer not found."

    def list_all_events(self):
        return "\n".join(str(event) for event in self.events.values())

    def list_all_volunteers(self):
        return "\n".join(str(volunteer) for volunteer in self.volunteers.values())

    def assign_pet_to_volunteer(self, pet_id, volunteer_id):
        if pet_id in self.pets and volunteer_id in self.volunteers:
            return f"{self.volunteers[volunteer_id].name} assigned to take care of {self.pets[pet_id].name}."
        return "Pet or volunteer not found."

class PetAdoptionApp:
    def __init__(self):
        self.adoption_center = AdoptionCenter()

    def run(self):
        pass