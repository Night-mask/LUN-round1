const { ethers } = require('ethers');

// Create a new random wallet
const wallet = ethers.Wallet.createRandom();

// Display the address and private key
console.log('Address:', wallet.address);
console.log('Private Key:', wallet.privateKey);

