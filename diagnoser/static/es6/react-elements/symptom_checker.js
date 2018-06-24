'use_strict';

import $ from 'jquery';
import React, { Component } from 'react';

import Utils from '../utils';
import { SymptomForm, DiagnosisForm, FollowupForm } from './forms';


class SymptomChecker extends Component {
    constructor(props) {
        super(props);
        this.state = {
            symptom_obj: null,
            current_step: 'diagnose',
            current_diagnosis: null
        };

        this.get_symptom = this._get_symptom.bind(this);
        this.submit_diagnosis = this._submit_diagnosis.bind(this);
    }

    _startOver() {
        this.setState({
            symptom_obj: null,
            current_step: 'diagnose',
            currrent_diagnosis: null
        })
    }

    _move_to_confirm(symptom) {
        this.setState({ current_step: 'confirm' });
        this.get_symptom(symptom);
    }

    _move_to_followup(user_response, diagnosis) {
        let next_step = 'followup-reject';
        if (user_response) {
            next_step = 'followup-confirm'
        }
        this.setState({
            current_step: next_step,
            current_diagnosis: diagnosis
        });
        this.submit_diagnosis(user_response, diagnosis.name);

    }

    _get_symptom(symptom) {
        $.ajax({
            url: Utils.buildUrl(['symptoms', symptom]),
            type: 'GET',
            success: (data) => {
                this.setState({
                    symptom_obj: data.symptom
                });
            },
            error: (event) => {
                console.error("Failed to retrieve symptom")
            }
        });
    }

    _submit_diagnosis(user_response, diagnosis) {
        let data = {
            response: user_response
        };

        $.ajax({
            url: Utils.buildUrl(['symptoms', this.state.symptom_obj.name, 'diagnoses', diagnosis ]),
            type: 'POST',
            data: JSON.stringify(data),
            dataType: 'json',
            contentType: 'application/json',
            success: (data) => {
                this.setState({});
            },
            error: (event) => {
                console.error("Failed to submit diagnosis")
            }
        });
    }

    render() {
        let form = null;
        if (this.state.current_step == 'diagnose') {
            form = <SymptomForm symptoms={this.props.symptoms}
                                submitSymptom={this._move_to_confirm.bind(this)}/>

        } else if (this.state.current_step == 'confirm') {
            form = <DiagnosisForm symptom={this.state.symptom_obj}
                                  submitDiagnosis={this._move_to_followup.bind(this)}/>

        } else if (this.state.current_step == 'followup-confirm' || this.state.current_step == 'followup-reject') {
            form = <FollowupForm symptom={this.state.symptom_obj}
                                 kind={this.state.current_step}
                                 diagnosis={this.state.current_diagnosis}
                                 submitDiagnosis={this._move_to_followup.bind(this)}/>
        }

        return (
            <div className="diagnoser">
                <h1>
                    <span className="title"> {this.props.app_name} </span>
                </h1>
                {form}
                <button id="reset" onClick={this._startOver.bind(this)}>
                    Start Over>
                </button>
            </div>
        );
    }
}

export default SymptomChecker