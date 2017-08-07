
import React from 'react'
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import styles from '../css/main.scss'
import SearchBar from './searchbar.js'
import Stock from './stock.js'

class StockTunes extends React.Component {


    constructor(props) {
        super(props);
        this.state = {
          query : "",
          stockData : [],
          stockErrors : []
        };
        this.handleQueryChange = this.handleQueryChange.bind(this);
        this.submitQuery = this.submitQuery.bind(this);
        this.displayStock = this.displayStock.bind(this);
    }

    handleSearch(q){
      this.query = q;
    }

    handleQueryChange(q){
      this.setState({
        query : q,
        stockData : []
      });
    }

    displayStock(data){
      this.setState({
        stockData : data
      })
    }

    submitQuery(){
      var _this = this;
      fetch('http://localhost:5000/api/stock/' + this.state.query)
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
              _this.displayStock(data)
          })
    }


    render() {
        return (
          <div className="app">
              <div className="container-fluid">
                  <div className="row">
                      <div className="col-md-12 search-col">
                          <div>
                              <div className="text-center brand-header">
                                  <h1>StockTunes</h1>
                                  <small>Make intuitive market predictions by listening to stocks.</small>
                              </div>   
                              <SearchBar query={this.state.query} onSearch={this.handleSearch} onQueryChange={this.handleQueryChange} submitQuery={this.submitQuery}/>
                          </div>
                      </div>
                  </div>
                  <Stock query={this.state.query}  stockData={this.state.stockData}/>
              </div>
          </div>

        )
    }
}


ReactDOM.render(
  <StockTunes />,
  document.getElementById('root')
);