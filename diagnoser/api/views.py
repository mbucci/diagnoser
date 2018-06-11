# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from __future__ import print_function

import json
import flask

from flask import current_app, jsonify, request


API = flask.Blueprint('api', __name__, url_prefix='/api')


@API.route('/symptoms', methods=['GET'])
def get_all_symptoms():
    """
    Get all symptoms configured in the API

    :return:
    """
    symptoms = current_app.diagnoser_api.get_symptoms()
    return jsonify({'symptoms': [s.serialize() for s in symptoms]})


@API.route('/symptoms/<symptom>', methods=['GET'])
def get_symptom(symptom):
    """
    Get a symptom

    :param symptom:
    :return:
    """
    return jsonify({'symptom': current_app.diagnoser_api.get_symptom(symptom).serialize()})


@API.route('/symptoms/<symptom>/diagnoses', methods=['GET'])
def get_all_symptom_diagnosis(symptom):
    """
    Get a symptom

    :param symptom:
    :return:
    """
    diagnoses = current_app.diagnoser_api.get_all_diagnoses_for_symptom(symptom)
    return jsonify({'diagnoses': [d.serialize() for d in diagnoses]})


@API.route('/symptoms/<symptom>/diagnoses/top', methods=['GET'])
def get_top_diagnosis(symptom):
    """
    Get top diagnosis for a symptom

    :param symptom:
    :return:
    """
    return jsonify({'diagnosis': current_app.diagnoser_api.get_top_diagnosis_for_symptom(symptom).serialize()})


@API.route('/symptoms/<symptom>/diagnoses/<diagnosis>', methods=['GET'])
def get_symptom_diagnosis(symptom, diagnosis):
    """
    Get a symptom

    :param symptom:
    :param diagnosis:
    :return:
    """
    symptom_obj = current_app.diagnoser_api.get_symptom(symptom)
    return jsonify({'diagnosis': symptom_obj.get_diagnosis(diagnosis).serialize()})


@API.route('/symptoms/<symptom>/diagnoses/<diagnosis>', methods=['POST'])
def handle_symptom_diagnosis_response(symptom, diagnosis):
    """
    handles a response from the front end, confirming or denying in a diagnosis is correct

    :param symptom:
    :param diagnosis:
    :return:
    """

    data = json.loads(request.data)
    response = current_app.diagnoser_api.handle_diagnosis_response(symptom, diagnosis, data.get('response'))
    return jsonify(response.serialize())

