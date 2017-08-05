
import React from 'react'
import PropTypes from 'prop-types'

const Todo = ({ onClick, completed, text }) => (
            <div className="container-fluid">
                <div className="row">
                    <div className="col-md-12 search-col">
                        <div>
                            <div className="text-center">
                                <h1>StockTunes</h1>
                                <small>Make intuitive market predictions by listening to stocks.</small>
                            </div>   
                            <br/>
                            <br/>
                            <div className="text-center">
                                <input id="search-input" type="text" name="search" placeholder="Enter a stock ticker ..." autoFocus/>
                            </div>
                            <br/>
                            <br/>
                            <div className="text-center">
                                <button className="search-button" onClick={this.SubmitQuery}>Search</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-12">
                        <div className="container">
                            <div className="row">
                                <div className="col-md-12">
                                    <h1>{ this.state.query }</h1>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )

Todo.propTypes = {
  onClick: PropTypes.func.isRequired,
  completed: PropTypes.bool.isRequired,
  text: PropTypes.string.isRequired
}

export default StockTunes


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
            <div className="container-fluid">
                <div className="row">
                    <div className="col-md-12 search-col">
                        <div>
                            <div className="text-center">
                                <h1>StockTunes</h1>
                                <small>Make intuitive market predictions by listening to stocks.</small>
                            </div>   
                            <br/>
                            <br/>
                            <div className="text-center">
                                <input id="search-input" type="text" name="search" placeholder="Enter a stock ticker ..." autoFocus/>
                            </div>
                            <br/>
                            <br/>
                            <div className="text-center">
                                <button className="search-button" onClick={this.SubmitQuery}>Search</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-12">
                        <div className="container">
                            <div className="row">
                                <div className="col-md-12">
                                    <h1>{ this.state.query }</h1>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}


ReactDOM.render(
  <StockTunes />,
  document.getElementById('main')
);