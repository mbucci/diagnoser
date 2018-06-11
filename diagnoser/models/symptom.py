

class Symptom(object):

    def __init__(self, name, diagnoses, *args, **kwargs):
        self.name = name
        self.diagnoses = diagnoses

    def __repr__(self):
        return 'name: {name}, diagnoses: {diagnoses}'.format(name=self.name, diagnoses=self.diagnoses)

    def top_diagnosis(self):
        return self.diagnoses[0]
