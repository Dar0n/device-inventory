import React, { Component } from 'react';
import './style.css';

export default class DeviceItem extends Component {

  handleClick = (e) => {
    this.props.handleClick(this.props.deviceInfo);
  }

  render() {
    return (
      <tr onClick={ this.handleClick } className='inventory-table-row'>
        {
          this.props.deviceInfo === '' ?
          null 
          : Object.values(this.props.tableFields).map(tableField => {
            let currentFieldValue;
            if (this.props.deviceInfo[tableField]) {
              if (tableField === 'customer'){
                const customerID = this.props.deviceInfo[tableField];
                currentFieldValue = this.props.customers.filter(customer => customer.id === customerID)[0].name;
              }
              else if (tableField === 'device_model') {
                const modelID = this.props.deviceInfo[tableField];
                currentFieldValue = this.props.models.filter(model => model.id === modelID)[0].name;
              }
              else {
                currentFieldValue = this.props.deviceInfo[tableField];
              }
            }
            return <td key={ tableField + ' ' + this.props.deviceInfo[tableField] } className='inventory-table-cell'>{currentFieldValue ? currentFieldValue : ''}</td>
          })
        }
      </tr>
    )
  }
}
