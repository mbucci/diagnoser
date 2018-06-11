# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import csv

from diagnoser.models.symptom import Symptom


class DiagnoserAPI(object):
    def __init__(self, symptoms_file, *args, **kwargs):
        self.symptoms = {}

        self.load_symptoms(symptoms_file)

    def load_symptoms(self, symptoms_file):
        csv_reader = csv.reader(symptoms_file)
        for row in csv_reader:
            symptom = Symptom(name=row[0], diagnoses=[d.strip() for d in row[1:]])
            self.symptoms[symptom.name] = symptom

    def get_symptom(self, symptom):
        if symptom not in self.symptoms:
            raise ValueError('Can not find any diagnoses for symptom: {symptom}'.format(symptom=symptom))

        return self.symptoms[symptom]

    def get_top_diagnosis_for_symptom(self, symptom):
        symptom_obj = self.get_symptom(symptom)
        return {'diagnosis': symptom_obj.top_diagnosis()}

    def get_all_diagnoses_for_symptom(self, symptom):
        symptom_obj = self.get_symptom(symptom)
        return {'diagnosis': symptom_obj.diagnoses}

    def get_all_symptoms(self):
        return {'symptoms': self.symptoms.keys()}
