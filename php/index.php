<?php

  include("block.php");
  $genesisTransaction = ["a sends 11 bitcoins to b", "b sends 44 bitcoins to c"];
  $genesisBlock = new Block(0, $genesisTransaction);
  $block1Transaction = ["a sends 11 bitcoins to b", "b sends 44 bitcoins to c"];
  $block1 = new Block($genesisBlock->getBlockHash(), $block1Transaction);
  $block2Transaction = ["a sends 11 bitcoins to b", "b sends 44 bitcoins to c"];
  $block2 = new Block($block1->getBlockHash(), $block2Transaction);
  echo "Genesis Block: ".$genesisBlock->getBlockHash();
  echo "<br>Block 1: ".$block1->getBlockHash();
  echo "<br>Block 2: ".$block2->getBlockHash();

 ?>
