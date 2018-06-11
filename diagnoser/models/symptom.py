import random


class Base(object):
    def __init__(self, *args, **kwargs):
        pass

    def serialize(self):
        raise NotImplementedError('serialize() not implemented for class: {class}'.format(self.__class__.__name__))


class Diagnosis(object):

    def __init__(self, name, *args, **kwargs):
        self.name = name.strip()
        self.seen = 0
        self.diagnosed = 0

    @property
    def diagnosis_rate(self):
        if not self.seen:
            return 0

        return self.diagnosed // self.seen

    def serialize(self):
        return {
            'name': self.name,
            'seen': self.seen,
            'diagnosed': self.diagnosed,
            'rate': self.diagnosis_rate
        }


class Symptom(object):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.diagnoses = {}
        self._top_diagnosis = None

    @property
    def top_diagnosis(self):
        if self._top_diagnosis and self._top_diagnosis.diagnosis_rate > 0:
            return self._top_diagnosis

        r = random.randint(0, len(self.diagnoses) - 1)
        self._top_diagnosis = self.diagnoses.values()[r]
        return self._top_diagnosis

    def serialize(self):
        return {
            'name': self.name,
            'top_diagnosis': self.top_diagnosis.serialize(),
            'diagnoses': [d.serialize() for d in self.diagnoses.values()]
        }

    def get_diagnosis(self, diagnosis):
        if diagnosis not in self.diagnoses:
            raise ValueError('Symptom: {sym} does not contain diagnosis: {diag}'.format(diag=diagnosis))

        diagnosis_obj = self.diagnoses[diagnosis]
        diagnosis_obj.seen += 1
        return diagnosis_obj

    def handle_diagnosis(self, diagnosis, response=False):
        diagnosis_obj = self.get_diagnosis(diagnosis)
        if response:
            diagnosis_obj.diagnosed += 1
            if diagnosis_obj.diagnosis_rate > self.top_diagnosis.diagnosis_rate:
                self._top_diagnosis = diagnosis_obj

        return diagnosis_obj
