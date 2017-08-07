
import React from 'react'
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import keydown from 'react-keydown';
import styles from '../css/searchbar.scss';

export default class SearchBar extends React.Component {


    constructor(props) {
        super(props);
        this.state = {
        };
        this.handleQueryChange = this.handleQueryChange.bind(this);
    }

    handleQueryChange(e){
      this.props.onQueryChange(e.target.value);
    }

    render() {
        return (
            <div className="searchbar">
                <div className="text-center">
                    <input id="search-input" type="text" name="search" value={this.props.query}  onChange={this.handleQueryChange} placeholder="Enter a stock ticker ..." autoFocus/>
                </div>
                <br/>
                <br/>
                <div className="text-center">
                    <button className="search-button" onClick={this.props.submitQuery}>Search</button>
                </div>
            </div>
        )
    }
}

