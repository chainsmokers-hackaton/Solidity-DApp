from web3 import Web3, HTTPProvider
rpc_url = "http://127.0.0.1:41960"
w3 = Web3(HTTPProvider(rpc_url))
from solc import compile_source
# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.8;
contract ChainSmokers{
    struct Subnet{
        Ap[] aps;
        uint node_num;
        mapping(address=>uint) index;
    }
    struct Ap{//subnet id 
        uint id;
        bytes32 original_hash;
        bytes32 received_hash;
    }
    Subnet ss;
    function join(uint id,bytes32 hash) public{
        Ap[] storage temp_aps =ss.aps;
        temp_aps.push(Ap(id,hash,0x0000000000000000000000000000000000000000000000000000000000000000));
        ss.index[msg.sender] = ss.node_num; 
        ss.node_num++;
    }
    event wrong_value_detected(uint id,bytes32 received_hash);
    //do care
    function get_hash(bytes32 new_hash) public{
        Ap storage temp_ap = ss.aps[ss.index[msg.sender]];
        temp_ap.received_hash = new_hash;
    }
    function check() public{//return list, which have promblem AP and it have to 
                            //has some informations to push alarm
        for(uint i=0;i<ss.node_num;i++){
            Ap memory temp_ap =ss.aps[i];
            //process by using temp_ap's element
            if(temp_ap.received_hash==0x0000000000000000000000000000000000000000000000000000000000000000) continue;
            if(temp_ap.original_hash!=temp_ap.received_hash){
                emit wrong_value_detected(temp_ap.id,temp_ap.received_hash);
            }else{
               temp_ap.received_hash=0x0000000000000000000000000000000000000000000000000000000000000000; 
            }
            //
        }
    }
}
'''
# web3.py
rpc_url = "http://127.0.0.1:41960"
w3 = Web3(HTTPProvider(rpc_url))
# w3 = Web3(IPCProvider("./chain-data/geth.ipc"))
# 지갑 주소를 unlock 해준다. 순서대로 지갑 주소, 비밀번호, unlock할 시간 (0은 영원히)
compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol["<stdin>:ChainSmokers"]
# 지갑 주소를 unlock 해준다. 순서대로 지갑 주소, 비밀번호, unlock할 시간 (0은 영원히)
w3.personal.unlockAccount(w3.eth.accounts[0], "1234", 0)
w3.eth.defaultAccount = w3.eth.accounts[0]
# 컨트랙트 어드레스를 대입 후 인스턴스 생성
contract_instance = w3.eth.contract(address="0xe0343e2281c67de802ea2249a92d26853181e8aa",abi=contract_interface['abi'],)
while True:
    button = input("1. join(uint id,bytes32 hash) 2. get_hash(bytes32 new_hash) 3. function check()")
    if button == '1':
        st = input("hash value");
        contract_instance.functions.join(0,"0x0000000000000000000000000000000000000000000000000000000000000000").transact()
    elif button == '2':
        contract_instance.functions.get_hash("0000000000000000000000000000000000000000000000000000000000000001").transact()
    elif button == '3':
        contract_instance.functions.check().transact();