import React, { Component } from 'react';
import Header from './components/Header';
import Inventory from './components/Inventory';
import DeviceDetails from './components/DeviceDetails';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      inventoryView: true,
      item: {},
      devices: [],
      models: [],
      customer: [],
    }
  }

  toggleDetailsView = (item) => {
    this.setState({inventoryView: !this.state.inventoryView, item});
  }

  async componentDidMount() {
    const headers = {
      'Content-Type': 'application/json', 
    }
    const method = 'GET';
    const myInit = {
      method,
      headers,
    }
    let deviceResponse = await fetch('http://localhost:8000/inventory/devices/listdevices/', myInit);
    let devices = await deviceResponse.json();

    let modelResponse = await fetch('http://localhost:8000/inventory/device_models/listmodels/all/', myInit);
    let models = await modelResponse.json();

    let customerResponse = await fetch('http://localhost:8000/inventory/customers/listcustomers/', myInit);
    let customers = await customerResponse.json();

    this.setState({devices, models, customers});
  }

  render() {
    return (
      <div className='App'>
      {
        this.state.inventoryView ?
          <div className='inventory-container'>
            <Header title='Device inventory' />
            <Inventory 
              toggleDetailsView={ this.toggleDetailsView }
              devices = { this.state.devices }
              models = { this.state.models }
              customers = { this.state.customers }
            />
          </div>
        :
          <div className='device-details-container'>
            <Header title='Device details' />
            <DeviceDetails 
              item={ this.state.item }
              toggleDetailsView={ this.toggleDetailsView }
              models={ this.state.models }
              customers={ this.state.customers }
            />
          </div>
      }
        
      </div>
    );
  }
}

export default App;
