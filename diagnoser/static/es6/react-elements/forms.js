'use strict';

import $ from 'jquery';
import React, { Component } from 'react';

import Utils from '../utils';


export class SymptomForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            disabled:false,
            curr_value: null,
            symptom_value: null
        };
    }

    _handleChange(event) {
        this.setState({curr_value: event.target.value});
    }

    _handleSubmit(event) {
        this.setState({
            disabled: true,
            symptom_value: this.state.curr_value
        });

        this.props.onSelectSymptom(this.state.curr_value);

    }

    render() {
        let optionTemplate = this.props.symptoms.symptoms.map(v => (
          <option key={v} value={v}>{v}</option>
        ));
        return (
            <form onSubmit={this._handleSubmit.bind(this)}>
                <label>
                    Are you currently experiencing any of the following symptoms?:
                    <select value={this.state.curr_value}
                            disabled={this.state.disabled}
                            onChange={this._handleChange.bind(this)}>
                        {optionTemplate}
                    </select>
                </label>
                <input type="submit" value="Submit" />
            </form>
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

    render() {
        debugger;

        return (
            <p>{this.props.diagnoses.diagnosis}</p>
        );
    }
}