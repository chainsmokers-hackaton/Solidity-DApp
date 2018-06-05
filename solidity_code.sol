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
    function check() public returns (bool ret){//return list, which have promblem AP and it have to 
                            //has some informations to push alarm
        for(uint i=0;i<ss.node_num;i++){
            Ap memory temp_ap =ss.aps[i];
            //process by using temp_ap's element
            if(temp_ap.received_hash==0x0000000000000000000000000000000000000000000000000000000000000000) continue;
            if(temp_ap.original_hash!=temp_ap.received_hash){
                emit wrong_value_detected(temp_ap.id,temp_ap.received_hash);
                ret = false;
                return ret;
            }else{
               temp_ap.received_hash=0x0000000000000000000000000000000000000000000000000000000000000000; 
               ret = true;
               return ret;
            }
            //
        }
    }
}