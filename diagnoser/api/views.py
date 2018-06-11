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
    return jsonify(current_app.diagnoser_api.get_all_symptoms())


@API.route('/diagnoses/<symptom>', methods=['GET'])
def get_all_diagnoses(symptom):
    """
    Get all diagnoses for a symptom

    :param symptom:
    :return:
    """
    return jsonify(current_app.diagnoser_api.get_all_diagnoses_for_symptom(symptom))


@API.route('/diagnoses/<symptom>/top', methods=['GET'])
def get_top_diagnosis(symptom):
    """
    Get top diagnosis for a symptom

    :param symptom:
    :return:
    """
    return jsonify(current_app.diagnoser_api.get_top_diagnosis_for_symptom(symptom))

