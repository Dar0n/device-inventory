import React, { Component } from 'react';
import DeviceItem from '../DeviceItem';
import './style.css'

class Inventory extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tableFields: {
        'Customer': 'customer', 
        'Date of delivery': 'date_of_delivery', 
        'Serial number': 'serial_number', 
        'Firmware version': 'firmware_version', 
        'Hardware version': 'hardware_version', 
        'Model': 'device_model'
      },
    }
  }

  handleInventoryClick = (item) => {
    this.props.toggleDetailsView(item);
  }

  render() {
    return (
      <div className='inventory'>
        
          <table>
            <thead>
              <tr>
                <th colSpan='6'></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                {Object.keys(this.state.tableFields).map(tableField => <td key={ 'table header ' + tableField } className='inventory-table-header-cell'>{tableField}</td>)}
              </tr>
              {
                this.props.devices.map(device => <DeviceItem 
                  key={ 'device ' + device.id } 
                  deviceInfo={this.props.devices.length ? device : ''} 
                  tableFields={ this.state.tableFields } 
                  customers={ this.props.customers }
                  models={ this.props.models }  
                  handleClick={ this.handleInventoryClick }
                />)
              }
            </tbody>
          </table>
        
        
      </div>
    )
  }
}

export default Inventory;