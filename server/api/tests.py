from django.test import TestCase
from api.models import Record
from django.utils.timezone import now


class RecordTestCase(TestCase):
    def setUp(self) -> None:
        Record.objects.create(record_name="test-record", record_date=now())
        Record.objects.create(record_name="test-record2", record_date=now())
    def test_Records_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Record.objects.get(record_name="test-record")
        cat = Record.objects.get(record_name="test-record2")
        self.assertEqual(lion.record_name, 'test-record')
        self.assertEqual(cat.record_name, 'test-record2')
