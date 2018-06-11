# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import csv

from diagnoser.models.symptom import Symptom, Diagnosis


class DiagnoserAPI(object):
    def __init__(self, symptoms_file, *args, **kwargs):
        self.symptoms = {}

        self.load_symptoms(symptoms_file)

    def load_symptoms(self, symptoms_file):
        csv_reader = csv.reader(symptoms_file)
        for row in csv_reader:
            symptom = Symptom(name=row[0])
            diagnoses = [Diagnosis(name=d) for d in row[1:]]
            symptom.diagnoses = {d.name: d for d in diagnoses}
            self.symptoms[symptom.name] = symptom

    def get_symptoms(self, serialize=False):
        symptoms = self.symptoms.values()
        if serialize:
            return {'symptoms': [s.serialize() for s in symptoms]}

        return symptoms

    def get_symptom(self, symptom, serialize=False):
        if symptom not in self.symptoms:
            raise ValueError('Can not find any diagnoses for symptom: {symptom}'.format(sym=symptom))

        symptom_obj = self.symptoms[symptom]
        if serialize:
            return {'symptom': symptom_obj.serialize()}

        return symptom_obj

    def get_all_diagnoses_for_symptom(self, symptom, serialize=False):
        symptom_obj = self.get_symptom(symptom)

        diagnoses = symptom_obj.dianoses.values()
        if serialize:
            return {'diagnoses': [d.serialize() for d in diagnoses]}

        return diagnoses

    def get_diagnosis_for_symptom(self, symptom, diagnosis, serialize=False):
        symptom_obj = self.get_symptom(symptom)
        diagnosis_obj = symptom_obj.get_diagnosis(diagnosis)
        if serialize:
            return {'diagnosis': diagnosis_obj.serialize()}

        return diagnosis_obj

    def get_top_diagnosis_for_symptom(self, symptom, serialize=False):
        symptom_obj = self.get_symptom(symptom)

        top_diagnosis = symptom_obj.top_diagnosis
        if serialize:
            return {'diagnosis': top_diagnosis.serialize()}

        return top_diagnosis

    def handle_diagnosis_response(self, symptom, diagnosis, response, serialize=False):
        symptom_obj = self.get_symptom(symptom)
        handle_response = symptom_obj.handle_diagnosis(diagnosis, response=response)
        if serialize:
            return {'diagnosis': handle_response.serialize()}

        return handle_response
