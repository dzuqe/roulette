from web3 import Web3
import os
from web3.middleware import geth_poa_middleware

#web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/' + os.environ['INFURA_API_KEY']))
#web3 = Web3(Web3.HTTPProvider('https://speedy-nodes-nyc.moralis.io/09dd853d231566671a467e96/polygon/mainnet'))
#web3.middleware_onion.inject(geth_poa_middleware, layer=0)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

me = web3.eth.accounts[0]
#me = "0xc4192029059E1D3a522751cCFc3E2Bf7f3c1172e"

binary="608060405234801561001057600080fd5b506000805b600c8112156100875760005b60038112156100735782600080848152602001908152602001600020600083815260200190815260200160002081905550828061005d90610098565b935050808061006b90610098565b915050610021565b50808061007f90610098565b915050610015565b5050610110565b6000819050919050565b60006100a38261008e565b91507f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156100d6576100d56100e1565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6101c08061011f6000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063c2b962fc1461003b578063d31efe611461006b575b600080fd5b61005560048036038101906100509190610103565b61009b565b604051610062919061014e565b60405180910390f35b61008560048036038101906100809190610103565b6100c9565b604051610092919061014e565b60405180910390f35b6000806000848152602001908152602001600020600083815260200190815260200160002054905092915050565b6000602052816000526040600020602052806000526040600020600091509150505481565b6000813590506100fd81610173565b92915050565b6000806040838503121561011657600080fd5b6000610124858286016100ee565b9250506020610135858286016100ee565b9150509250929050565b61014881610169565b82525050565b6000602082019050610163600083018461013f565b92915050565b6000819050919050565b61017c81610169565b811461018757600080fd5b5056fea2646970667358221220a646008561dbf2c5efe5bb530bfe3aacacd01fa723b8f9623ae70589a116e05b64736f6c63430008000033"

abi='[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"int256","name":"","type":"int256"},{"internalType":"int256","name":"","type":"int256"}],"name":"board","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"x","type":"int256"},{"internalType":"int256","name":"y","type":"int256"}],"name":"getBoard","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"nonpayable","type":"function"}]'



game = web3.eth.contract(abi=abi, bytecode=binary)

dtx = game.constructor().buildTransaction({
    'gas': 2000000,
    'gasPrice': web3.toWei(50, 'gwei'),
    'nonce': web3.eth.getTransactionCount(me),
    'chainId': web3.eth.chainId
})

stx = web3.eth.account.signTransaction(dtx, private_key='0xd178895f7bd6578caa9bfa4182824796b19d936d5a006831257aa2632158dbbe') #os.environ['ETHEREUM_PRIVATE_KEY'])
ret = web3.eth.sendRawTransaction(stx.rawTransaction)

print("result: ", ret.hex())

#disp = web3.eth.contract(address="0x8512934aEC06ee5f53877532B845C3425a60932A", abi=abi)

#bob = "0x4d3218B23D4f383dA54df6dDFf4833a9d36F75c3"
#alice = "0x4CcB5406869C76B18FFf8Ad8e3C73551C6Ee9944"
#harry = "0x6Be02d1d3665660d22FF9624b7BE0551ee1Ac91b"

#addresses = [bob, alice, harry]
#amounts = [web3.toWei(1, 'ether'),web3.toWei(5, 'ether'),web3.toWei(10, 'ether')]
#etx = disp.functions.disperseEther(addresses, amounts).buildTransaction({
#    'gas': 1000000,
#    'value': web3.toWei(20, 'ether'),
#    'gasPrice': web3.toWei(1, 'gwei'),
#    'nonce': web3.eth.getTransactionCount(me),
#    'chainId': web3.eth.chainId
#})
#
#setx = web3.eth.account.signTransaction(etx, private_key=os.environ['ETHEREUM_PRIVATE_KEY'])
#retx = web3.eth.sendRawTransaction(setx.rawTransaction)
#
