# KotaniPay

This is a python wrapper for the KotaniPay API available at [KotaniDocs](https://docs.kotanipay.com/) . It currently supports the following features:

## Features

1. **Customer Manager**

- Bank Customer

- Mobile Money Customer

- KYC Management

2. **Wallet Management**

- FiatWallet

- Crypto Wallet

3. **Transaction Management**

- Deposits

- Withdraw

- Rates

- OnRamp and OffRamp Transactions

4. **System Health**

  

## Get Started

### Setup
To get access to KotaniPay dashboard, visit the website and contact the company directly. You will be provided with an administrator email address or access tokens that you may use with your API.

### Installing
To install the python package, run the command below. 

    pip install kotanipay
You can test the installation by importing the Base class onto python as shown below

    from kotanipay import KotaniPay

## Usage
### Authentication

    from  kotanipay_sdk  import  KotaniPay
    
    access_key  =  ""
    
    k  =  KotaniPay(accessToken=access_key, debug=False)

### Customers
### Wallets
### Transact
### System Health

  

# Contributing

# Todo

 - [ ] Deploy Package
 - [ ] Unit Tests
 - [ ] Inbuilt Support for environment variables for the access_key
 - [ ] Input Validation
 - [ ] Improved Error Handling
 - [ ] In class documentation
 - [ ] Convert request responses into objects

# Authors

> Built with ❤️ by [David Marko](https://davemarko.com)

# Licence