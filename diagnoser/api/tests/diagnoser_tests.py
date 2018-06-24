# -*- coding: utf-8 -*-

from diagnoser.core.tests.utils import BaseTestCase

from mock import patch


class DiagnoserTests(BaseTestCase):
    def setUp(self):
        super(DiagnoserTests, self).setUp()

    def test_load_symptoms(self):
        self.assertEqual(self.diagnoser_api.symptoms.keys(), ['symptom'])
        self.assertIn('diagnosis_1', self.diagnoser_api.symptoms['symptom'].diagnoses.keys())
        self.assertIn('diagnosis_2', self.diagnoser_api.symptoms['symptom'].diagnoses.keys())
        self.assertIn('diagnosis_3', self.diagnoser_api.symptoms['symptom'].diagnoses.keys())
        self.assertDictEqual(self.diagnoser_api.symptoms['symptom'].diagnoses['diagnosis_1'].serialize(), {'seen': 0, 'rate': 0, 'name': 'diagnosis_1', 'diagnosed': 0})

    def test_get_symptoms(self):
        symptoms = self.diagnoser_api.get_symptoms()
        self.assertEqual(symptoms[0].name, 'symptom')

        symptoms_serialize = self.diagnoser_api.get_symptoms(serialize=True)
        self.assertEqual(symptoms_serialize['symptoms'][0]['name'], 'symptom')

    def test_get_symptom(self):
        symptom = self.diagnoser_api.get_symptom('symptom')
        self.assertEqual(symptom.name, 'symptom')

        symptom_serialize = self.diagnoser_api.get_symptom('symptom', serialize=True)
        self.assertEqual(symptom_serialize['symptom']['name'], 'symptom')

        with self.assertRaises(ValueError):
            self.diagnoser_api.get_symptom('no symptom')

    def test_get_all_diagnoses_for_symptom(self):
        diagnoses = self.diagnoser_api.get_all_diagnoses_for_symptom('symptom')
        self.assertIn(diagnoses[0].name, ['diagnosis_1', 'diagnosis_2', 'diagnosis_3'])
        self.assertIn(diagnoses[1].name, ['diagnosis_1', 'diagnosis_2', 'diagnosis_3'])
        self.assertIn(diagnoses[2].name, ['diagnosis_1', 'diagnosis_2', 'diagnosis_3'])

        diagnoses_serialize = self.diagnoser_api.get_all_diagnoses_for_symptom('symptom', serialize=True)
        self.assertIn(diagnoses_serialize['diagnoses'][0]['name'], ['diagnosis_1', 'diagnosis_2', 'diagnosis_3'])
        self.assertIn(diagnoses_serialize['diagnoses'][1]['name'], ['diagnosis_1', 'diagnosis_2', 'diagnosis_3'])
        self.assertIn(diagnoses_serialize['diagnoses'][2]['name'], ['diagnosis_1', 'diagnosis_2', 'diagnosis_3'])

    def test_get_diagnosis_for_symptom(self):
        diagnosis = self.diagnoser_api.get_diagnosis_for_symptom('symptom', 'diagnosis_1')
        self.assertEqual(diagnosis.name, 'diagnosis_1')
        # getting a specific diagnosis should increment the seen count
        self.assertEqual(diagnosis.seen, 1)
        self.assertEqual(diagnosis.diagnosed, 0)
        self.assertEqual(diagnosis.diagnosis_rate, 0)

        diagnosis_serialize = self.diagnoser_api.get_diagnosis_for_symptom('symptom', 'diagnosis_1', serialize=True)
        self.assertEqual(diagnosis_serialize['diagnosis']['name'], 'diagnosis_1')
        self.assertEqual(diagnosis_serialize['diagnosis']['seen'], 2)
        self.assertEqual(diagnosis_serialize['diagnosis']['diagnosed'], 0)
        self.assertEqual(diagnosis_serialize['diagnosis']['rate'], 0)

        with self.assertRaises(ValueError):
            self.diagnoser_api.get_diagnosis_for_symptom('symptom', 'no_diagnosis')

    @patch('diagnoser.models.symptom.random.randint')
    def test_get_top_diagnosis_for_symptom(self, mock_random):
        mock_random.return_value = 1
        top_diagnosis = self.diagnoser_api.get_top_diagnosis_for_symptom('symptom')
        self.assertEqual(top_diagnosis.name, 'diagnosis_3')
        # getting top_diagnosis should not increment the seen count, as it is a property
        self.assertEqual(top_diagnosis.seen, 0)

        mock_random.return_value = 2
        top_diagnosis_serialized = self.diagnoser_api.get_top_diagnosis_for_symptom('symptom', serialize=True)
        self.assertEqual(top_diagnosis_serialized['diagnosis']['name'], 'diagnosis_2')
        self.assertEqual(top_diagnosis_serialized['diagnosis']['seen'], 0)

    @patch('diagnoser.models.symptom.random.randint')
    def test_handle_diagnosis_response(self, mock_random):
        mock_random.return_value = 1
        top_diagnosis = self.diagnoser_api.get_top_diagnosis_for_symptom('symptom')
        self.assertEqual(top_diagnosis.name, 'diagnosis_3')
        self.assertEqual(top_diagnosis.seen, 0)

        confirmed_diagnosis = self.diagnoser_api.handle_diagnosis_response('symptom', 'diagnosis_1', True)
        self.assertEqual(confirmed_diagnosis.name, 'diagnosis_1')
        self.assertEqual(confirmed_diagnosis.seen, 1)
        self.assertEqual(confirmed_diagnosis.diagnosed, 1)
        self.assertEqual(confirmed_diagnosis.diagnosis_rate, 1.0)

        rejected_diagnosis = self.diagnoser_api.handle_diagnosis_response('symptom', 'diagnosis_1', False, serialize=True)
        self.assertEqual(rejected_diagnosis['diagnosis']['name'], 'diagnosis_1')
        self.assertEqual(rejected_diagnosis['diagnosis']['seen'], 2)
        self.assertEqual(rejected_diagnosis['diagnosis']['diagnosed'], 1)
        self.assertEqual(rejected_diagnosis['diagnosis']['rate'], 0.5)

        top_diagnosis = self.diagnoser_api.get_top_diagnosis_for_symptom('symptom')
        self.assertEqual(top_diagnosis.name, 'diagnosis_1')
        self.assertEqual(top_diagnosis.seen, 2)


