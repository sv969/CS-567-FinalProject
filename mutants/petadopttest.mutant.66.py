import unittest
from petadoptionplatform import *

class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet(pet_id=1, name="Buddy", species="Dog", age=3, description="Friendly and energetic.")

    def test_adopt(self):
        self.assertFalse(self.pet.adopted)
        self.pet.adopt()
        self.assertTrue(self.pet.adopted)
        self.assertEqual(self.pet.adopt(), "Buddy is already adopted.")

    def test_update_medical_record(self):
        self.pet.update_medical_record({'vaccinated': True})
        self.assertIn('vaccinated', self.pet.medical_record)
        self.assertTrue(self.pet.medical_record['vaccinated'])

    def test_is_adoptable(self):
        self.pet.update_medical_record({'health': 'good'})
        self.assertTrue(self.pet.is_adoptable())

    def test_age_up(self):
        old_age = self.pet.age
        self.pet.age_up()
        self.assertEqual(self.pet.age, old_age + 1)

    def test_change_description(self):
        new_description = "Calm and loving."
        self.pet.change_description(new_description)
        self.assertEqual(self.pet.description, new_description)
    
    def test_get_medical_history(self):
        self.pet.update_medical_record({'vaccination': 'Rabies'})
        medical_history = self.pet.get_medical_history()
        self.assertIn('vaccination', medical_history)
        self.assertEqual(medical_history['vaccination'], 'Rabies')

    def test_invalid_adopt(self):
        self.pet.adopt()
        result = self.pet.adopt()
        self.assertEqual( "Buddy is already adopted.",result)

class TestVolunteer(unittest.TestCase):
    def setUp(self):
        self.volunteer = Volunteer(volunteer_id=1, name="Alice")

    def test_log_hours(self):
        self.volunteer.log_hours(5)
        self.assertEqual(self.volunteer.hours_logged, 5)

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.event = Event(event_id=1, title="Adoption Day", description="Adopt your new best friend!", date="2021-08-30")
        self.volunteer = Volunteer(volunteer_id=1, name="Alice")

    def test_add_participant(self):
        self.event.add_participant(self.volunteer)
        self.assertIn(self.volunteer, self.event.participants)

    def test_list_participants(self):
        self.event.add_participant(self.volunteer)
        participant_list = self.event.list_participants()
        self.assertIn("Alice", participant_list)

class TestAdoptionCenter(unittest.TestCase):
    def setUp(self):
        self.center = AdoptionCenter()
        self.pet = Pet(pet_id=1, name="Buddy", species="Dog", age=3, description="Friendly and energetic.")
        self.volunteer = Volunteer(volunteer_id=1, name="Alice")
        self.event = Event(event_id=1, title="Adoption Day", description="Adopt your new best friend!", date="2021-08-30")

    def test_add_volunteer(self):
        result = self.center.add_volunteer(volunteer_id=1, name="Alice")
        self.assertIn("Volunteer Alice added", result)
        self.assertIn(self.volunteer.volunteer_id, self.center.volunteers)

    def test_organize_event(self):
        result = self.center.organize_event(event_id=1, title="Adoption Day", description="Adopt your new best friend!", date="2021-08-30")
        self.assertIn("Event Adoption Day created", result)
        self.assertIn(self.event.event_id, self.center.events)

    def test_register_for_event(self):
        self.center.add_volunteer(volunteer_id=1, name="Alice")
        self.center.organize_event(event_id=1, title="Adoption Day", description="Adopt your new best friend!", date="2021-08-30")
        result = self.center.register_for_event(event_id=1, volunteer_id=1)
        self.assertIn("has been added to the event", result)

class TestPetAdoptionApp(unittest.TestCase):
    def setUp(self):
        self.app = PetAdoptionApp()

    def test_run_app(self):
        self.assertIsInstance(self.app.adoption_center, AdoptionCenter)

if __name__ == '__main__':
    unittest.main()
