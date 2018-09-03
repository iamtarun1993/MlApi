# MlApi

Sample REST API structure to get linear-regression value.

$.ajax({
type: "POST",
url: "https://demo-ml-api.herokuapp.com/regression/linear_regression", 
data: { x_train: x_train, y_train: y_train,x_test:x_test },
dataType: "json",
success: function(result){
console.log(result)
}});

# If you are using the api wait for some time for 1st request. Server may be in the state of sleep. Let it start.


Showing details of bhav copy published by BSE 
https://demo-ml-api.herokuapp.com/Zerodha

# simple REST API for get bank data
1.To fetch bank details by IFSC
https://demo-ml-api.herokuapp.com/fyle/branch_details/bank_ifsc_code

Ex: https://demo-ml-api.herokuapp.com/fyle/branch_details/sbin0011545

2. To fetch all bank details by name and city
https://demo-ml-api.herokuapp.com/fyle/bank_list/bank_name/bank_city

Ex: https://demo-ml-api.herokuapp.com/fyle/bank_list/canara bank/kolkata
