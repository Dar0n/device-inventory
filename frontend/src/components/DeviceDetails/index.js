import React, { Component } from 'react';
import { capitalize } from '../../helpers/capitalize';
import './style.css';

export default class DeviceDetails extends Component {
constructor(props) {
  super(props);
  this.state = {
    form: {},
    configurationFields: [],
  }
}

  async componentDidMount() {
    this.setState({form: this.props.item});
    // let newForm = Object.assign(this.props.item);

    // const headers = {
    //   'Content-Type': 'application/json', 
    // }
    // const method = 'GET';
    // const myInit = {
    //   method,
    //   headers,
    // }
    // const modelID = this.props.item.device_model;
    // const deviceID = this.props.item.id;
    // let configurationFieldResponse = await fetch(`http://localhost:8000/inventory/configuration_fields/listconfigurationfields/${modelID}/`, myInit);
    // let configurationFields = await configurationFieldResponse.json();

    // let attributeValuesResponse = await fetch(`http://localhost:8000/inventory/attributes_values/listattributevalues/${deviceID}/`, myInit);
    // let attributesValues = await attributeValuesResponse.json();

    // console.log(configurationFields, attributesValues);
    // configurationFields.map(field => {
    //   // newForm[field.name]
    //   return ;
    // })
    // this.setState({configurationFields});
  }

  handleChange = (e) => {
    let newForm = Object.assign(this.state.form);
    if (e.target.id === 'customer' || e.target.id === 'device_model') {
      newForm[e.target.id] = parseInt(e.target.value);
    }
    else {
      newForm[e.target.id] = e.target.value;
    }
    this.setState({form: newForm})
  }

  handleCancel = () => {
    this.props.toggleDetailsView({});
  }

  async handleSubmit(e) {
    e.preventDefault();
    const headers = {
      'Content-Type': 'application/json', 
    }
    const method = 'POST';
    let body = {};
    Object.keys(this.state.form).map(field => {
      body[field] = this.state.form[field];
      return undefined;
    });
    body = JSON.stringify(body);
    const myInit = {
      method,
      headers,
      body
    }
    await fetch(`http://localhost:8000/inventory/devices/device/${this.state.form['id']}/`, myInit);
    this.props.toggleDetailsView({});
  }

  render() {

    return (
      <form className='device-details-form' onSubmit={ (e) => this.handleSubmit(e) }>
        {
          Object.keys(this.state.form)
          .filter(field => field !== 'id' && field !== 'lorawan')
          .map(field => {
            return (
              <div className={ 'device-details-form-field-container' } key={ field }>
                <label htmlFor={ field }>{ capitalize(field) }</label>
                {
                  field === 'customer' ?
                  <select className='device-details-form-field' id={ field } onChange={ (e) => this.handleChange(e) } defaultValue={ this.state.form.customer } >
                    {
                      this.props.customers.map(customer => {
                        return <option key={ customer.id + ' ' + customer.name } value={ customer.id } >{ customer.name }</option>
                      })
                    }
                  </select>
                  :
                  field === 'device_model' ?
                  <select className='device-details-form-field' id={ field } onChange={ (e) => this.handleChange(e) } defaultValue={ this.state.form.device_model } >
                    {
                      this.props.models.map(model => {
                        return <option key={ model.id + ' ' + model.name } value={ model.id } >{ model.name }</option>
                      })
                    }
                  </select>
                  :
                  <input className='device-details-form-field' id={ field } value={ this.state.form[field] ? this.state.form[field] : '' } onChange={ (e) => this.handleChange(e) }/>
                }
              </div>
            )
          })
        }
        <div className='device-details-form__buttons-container'>
          <input className='device-details-form__button' type='button' value='Cancel' onClick={ this.handleCancel } />
          <input className='device-details-form__button' type='submit' value='Save' />
        </div>
      </form>
    )
  }
}
