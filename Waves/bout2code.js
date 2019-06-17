/* https://cryptin.eu/video-how-to-create-a-smart-contract-on-waves-platform-smart-assets/
#A Smart Asset which checks for a data transaction to enable or disable token burning
#If EnableBurn is set to true burning of the token is allowed. Else it is not.
#Address defined for data transaction:
*/

let AddressWithData = Address(base58'3P9joJaAYxoTR1oWr38bNrQSrnpqAZVzbm6')

let EnableBurn = extract(getBoolean(AddressWithData, "EnableBurn"))

if (EnableBurn) then

match (tx) {
    case _ => true
}

else

match (tx) {
    case b:BurnTransaction => false
    case _ => true
  }
