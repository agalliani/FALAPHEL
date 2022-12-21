Checking if there is anything in the serial buffer. 
If there is, it will deserialize the JSON object and then check the operation. 

If the operation is STOP, it will call the FiniteStateMachine with 0. 

If the operation is CONFIG_CUSTOM,
then it will read the data from the JSON object and store it in the configArray.
Finally it will call the FiniteStateMachine with 1. 

If the operation is CHARGE_SCAN, it will call the FiniteStateMachine with 2. 
If the operation is CHARGE_SCAN_FULL_MATRIX.
It will then set the configSetup variable to the value of the "setup" key in the JSON document.
It will then call the FiniteStateMachine function with the value 3.

If the operation is not any of the above, it will print "Unknown operation request".
