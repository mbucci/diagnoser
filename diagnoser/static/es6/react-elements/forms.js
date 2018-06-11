'use strict';

import _ from 'lodash';
import $ from 'jquery';
import Select from 'react-select';
import React, { Component } from 'react';

import Utils from '../utils';


export class SymptomForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: null
        };
    }

    _handleChange(selected_option) {
        this.setState({ value: selected_option.value });
    }

    _handleSubmit() {
        this.props.submitSymptom(this.state.value);
    }

    render() {
        let options = this.props.symptoms.symptoms.map(v => ({value: v.name, label: v.name}));

        return (
            <div id="symptom-form">
                <label>
                    <h3>
                        <span>Are you currently experiencing any of the following symptoms?:</span>
                    </h3>
                    <Select name="symptom-select"
                            value={this.state.value}
                            options={options}
                            onChange={this._handleChange.bind(this)}
                      />
                </label>
                <button onClick={this._handleSubmit.bind(this)}>
                    Diagnose Me
                </button>
            </div>
        );
    }
}


export class DiagnosisForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: null
        }
    }

    _handleClick(event) {
        let value = false;
        if (event.target.value == 'true') {
            value = true;
        }

        this.props.submitDiagnosis(value, this.props.symptom.top_diagnosis);
    }

    render() {
        let top_diagnosis = null;
        if (this.props.symptom) {
            top_diagnosis = this.props.symptom.top_diagnosis.name;
        }

        return (
            <div id="diagnosis-form">
                <h3>
                    <span>
                        It looks like you might have {top_diagnosis}
                    </span>
                </h3>
                <div id="diagnosis-confirm">
                    <h4>
                        <span>Is this correct?</span>
                    </h4>
                    <button id="confirm-diagnosis"
                            value={true}
                            onClick={this._handleClick.bind(this)}>
                        Yes
                    </button>
                    <button id="reject-diagnosis"
                            value={false}
                            onClick={this._handleClick.bind(this)}>
                        No
                    </button>
                </div>
            </div>
        );
    }
}

export class FollowupForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: null
        }
    }

    _handleChange(selected_option) {
        this.setState({ value: selected_option.value });
    }

    _handleSubmit() {
        let diagnosis = _.find(this.props.symptom.diagnoses, {name: this.state.value});
        this.props.submitDiagnosis(true, diagnosis)
    }

    render() {
        if (this.props.kind == 'followup-confirm') {
            return (
                <div id="followup-form">
                    <h3>
                        <span>
                            Thank you for using Diagnoser!
                            I hope you find treatment for your {this.props.diagnosis.name}
                        </span>
                    </h3>
                </div>
            )
        } else if (this.props.kind == 'followup-reject') {
            let options = this.props.symptom.diagnoses.map(v => ({value: v.name, label: v.name}));
            options = _.reject(options, {value: this.props.diagnosis.name});

            return (
                <div id="followup-form">
                    <h3>
                        <span>
                            Do you have any of these other conditions?
                        </span>
                    </h3>
                    <Select name="diagnosis-select"
                            value={this.state.value}
                            options={options}
                            disabled={this.state.disabled}
                            onChange={this._handleChange.bind(this)}
                          />
                    <button id="confirm-secondary-diagnosis"
                            onClick={this._handleSubmit.bind(this)}>
                        Confirm Diagnosis
                    </button>
                </div>
            )
        }
    }
}