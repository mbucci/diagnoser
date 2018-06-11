'use_strict';

import $ from 'jquery';
import React, { Component } from 'react';

import Utils from '../utils';
import { SymptomForm, DiagnosisForm } from './forms';


class SymptomChecker extends Component {
    constructor(props) {
        super(props);
        //this.get_diagnoses = this._get_diagnoses().bind(this);
        this.state = {
            symptom: '',
            diagnoses: [],
            loading: false
        }
    }

    //componentDidMount() {
    //    this.fetch_workflows();
    //}
    //
    //componentDidUpdate() {
    //    if (this.state.loading) {
    //        this.fetch_workflows();
    //    }
    //}

    _get_diagnoses(symptom) {

        $.ajax({
            url: Utils.buildUrl(['diagnoses', symptom]),
            type: 'GET',
            success: (data) => {
                this.setState({
                    diagnoses: data._result
                });
            },
            error: (event) => {
                console.log("Blah Blah Blah")
            }
        })
    }

    render() {
        return (
            <div className="diagnoser">
                <h1>
                    <i className="fa fa-user-md"></i>
                    <span className="title"> {this.props.app_name} </span>
                </h1>
                <SymptomForm symptoms={this.props.symptoms}
                             onSelectSymptom={this._get_diagnoses.bind(this)}/>
                <DiagnosisForm diagnoses={this.state.diagnoses}/>
            </div>
        );
    }
}

export default SymptomChecker