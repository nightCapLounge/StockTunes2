(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){

class StockTunes extends React.Component {


    constructor(props) {
        super(props);
        this.state = {
            query: ""
        };
    }


    SubmitQuery(){
        this.state.query = query;
        fetch('http://localhost:5000/api/stock/' + query)
            // Evaluate the response status
            .then(function(response){
                if (response.status >= 200 && response.status < 300) {
                    return response
                } else {
                    var error = new Error(response.statusText)
                    error.response = response
                    throw error
                }
            })
            // Parse that JSON
            .then(function(response){
                return response.json()
            })
            // Report the result
            .then(function(data){
               console.log('request succeeded with JSON response', data)
            })
    }

    render() {
        return (
            React.createElement("div", {className: "container-fluid"}, 
                React.createElement("div", {className: "row"}, 
                    React.createElement("div", {className: "col-md-12 search-col"}, 
                        React.createElement("div", null, 
                            React.createElement("div", {className: "text-center"}, 
                                React.createElement("h1", null, "StockTunes"), 
                                React.createElement("small", null, "Make intuitive market predictions by listening to stocks.")
                            ), 
                            React.createElement("br", null), 
                            React.createElement("br", null), 
                            React.createElement("div", {className: "text-center"}, 
                                React.createElement("input", {id: "search-input", type: "text", name: "search", placeholder: "Enter a stock ticker ...", autoFocus: true})
                            ), 
                            React.createElement("br", null), 
                            React.createElement("br", null), 
                            React.createElement("div", {className: "text-center"}, 
                                React.createElement("button", {className: "search-button", onClick: this.SubmitQuery}, "Search")
                            )
                        )
                    )
                ), 
                React.createElement("div", {className: "row"}, 
                    React.createElement("div", {className: "col-md-12"}, 
                        React.createElement("div", {className: "container"}, 
                            React.createElement("div", {className: "row"}, 
                                React.createElement("div", {className: "col-md-12"}, 
                                    React.createElement("h1", null,  this.state.query)
                                )
                            )
                        )
                    )
                )
            )
        )
    }
}


ReactDOM.render(
  React.createElement(StockTunes, null),
  document.getElementById('main')
);

},{}]},{},[1]);
