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
