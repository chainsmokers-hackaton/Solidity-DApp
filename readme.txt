더미 계정1: "0x349192d70e0e82cde11b19b3bd54b564722be589" 1234
더미 계정2: "0xdef4a583d350170ddd6ec1ff56249c54c8d5e5a4" 1234

geth
----------------
java script api
soldity

geth -datadir ./datadir --rpcapi "db,eth,net,web3,personal,admin,miner,debug,txpool" --rpc --port "41960" --networkid 4015 &
geth --rpc --rpccorsdomain "*" --datadir ./datadir --rpcport "41960" --rpcaddr "0.0.0.0" --rpcapi "db,eth,net,web3,personal,admin,miner,debug,txpool" --networkid 4015 &

geth --rpc --rpccorsdomain "*" --datadir ./datadir --rpcport "41960" --rpcaddr "0.0.0.0" --rpcapi "db,eth,net,web3,personal,admin,miner,debug,txpool" --networkid 4015 --unlock "0xdef4a583d350170ddd6ec1ff56249c54c8d5e5a4" --password "./key" --port 41970 console


가상환경 접근
source solidity_venv/bin/activate
컨트랙트 주소
0xdef4a583d350170ddd6ec1ff56249c54c8d5e5a4
