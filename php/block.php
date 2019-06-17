<?php

  class Block {
    private $previousHash;
    private $transactions=[];
    private $blockHash;
    function __construct($previousHash, $transactions){
      $this->previousHash = $previousHash;
      $this->transactions = $transactions;
      $contents = [md5(serialize($transactions)), $previousHash];
      $this->blockHash = md5(serialize($contents));
    }
    function getPreviousHash(){
      return $this->previousHash;
    }

    function getTransactions(){
      return $this->transactions;
    }

    function getBlockHash(){
      return $this->blockHash;
    }
  }

 ?>
