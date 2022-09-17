import json
import list_bsc
from web3 import Web3



def getPrice(factory,pair):

	#####################################################################
	#####################################################################


	AMM = list_bsc.module['AMM'][factory]['Factory']
	x = pair.split('/')
	Tokens1 = list_bsc.module['Tokens'][x[0]]
	Tokens2 = list_bsc.module['Tokens'][x[1]]


	web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
	Tokens1 = web3.toChecksumAddress(Tokens1)
	Tokens2 = web3.toChecksumAddress(Tokens2)
	Factory_Address = web3.toChecksumAddress(AMM)


	#ABI Contract factory
	with open('src/factory.json', 'r') as abi_definition:
	    abi = json.load(abi_definition)


	#ABI Contract Pancake Pair
	with open('src/pair.json', 'r') as abi_definition:
	    parsed_pair = json.load(abi_definition)


	#####################################################################
	#####################################################################


	contract = web3.eth.contract(address=Factory_Address, abi=abi)
	pair_address = contract.functions.getPair(Tokens1,Tokens2).call()
	pair1 = web3.eth.contract(abi=parsed_pair, address=pair_address)


	reserves = pair1.functions.getReserves().call()
	reserve0 = reserves[0]
	reserve1  = reserves[1]


	print(f'The current {pair} price on {factory} is : ${reserve1/reserve0}')


	#####################################################################
	#####################################################################

getPrice(factory="Twindex",pair="DOP/BUSD")
getPrice(factory="Pancake",pair="DOP/BUSD")
print("hello?")