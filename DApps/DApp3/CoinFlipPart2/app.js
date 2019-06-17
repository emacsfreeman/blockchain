(function (Contract) {
    var web3;
    var instance;

    function init(cb) {
        web3 = new Web3(
            (window.web3 && window.web3.currentProvider) ||
            new Web3.providers.HttpProvider(Contract.endpoint));

        var contract_interface = web3.eth.contract(Contract.abi);
        instance = contract_interface.at(Contract.address);
        cb();
    }

    function getBalance() {
        instance.getBalance(function (error, result) {
            if(error)
                alert(error);
            else {
                $("#balance").html(result.toString());
            }
        });
    }

    function flip() {
        let val = parseInt($("#bet").val());
        instance.flip.sendTransaction({from: "0x95c2332b26bb22153a689ae619d81a6c59e0a804", gas: 100000, value: val}, function (error, result){
            if (error) {
                alert(error);
            }
            else {
                alert("SUCCESS");
            }
        });
    }

    $(document).ready(function () {
        init(function () {
            getBalance();
        });
        $("#submit").click(function (){
            flip();
        });
    });
})(Contracts['CoinFlip']);
