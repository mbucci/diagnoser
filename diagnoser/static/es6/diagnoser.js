'use_strict';

import $ from 'jquery';
import React from 'react';
import ReactDOM from 'react-dom';

import SymptomChecker from './react-elements/symptom_checker';


$(() => {
  let container = $('#diagnoser-container');
  let app_name = container.data('app-name');
  let symptoms = container.data('symptoms');

  ReactDOM.render(<SymptomChecker app_name={app_name}
                                  symptoms={symptoms}/>, container[0]);
});



