
import React from 'react'
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import keydown from 'react-keydown';
import styles from '../css/stock.scss';

export default class Stock extends React.Component {


    constructor(props) {
        super(props);
        this.state = {
        };
        this.getMidi = this.getMidi.bind(this);
    }

    getMidi(){
        var _this = this;
        document.getElementById("midi-form").submit();
    }

    render() {
        return (
            <div className="row stock">
                <div className="col-md-12">
                    <div className="container">
                        <div className="row">
                            <div className="col-md-12">
                                <h2>{ this.props.query != "" ? this.props.query : "Choose a stock ..." }</h2>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-6 col-sm-12">
                                <table>
                                    <tbody>
                                    {
                                        this.props.stockData.map((stock, index )=> (
                                            <ul>
                                                <li className="stockRow" key={index}>
                                                    <h4>{stock.metric}</h4>
                                                    <p><span>{stock.data.value}</span> <span>({stock.data.unit})</span></p>
                                                </li>
                                            </ul>
                                        ))
                                    }
                                    </tbody>
                                </table>
                            </div>
                            <div className="col-md-6 col-sm-12">
                                { this.props.stockData.length > 0 &&
                                    <div>
                                        <div className="text-center">
                                            <button className="midi-button" onClick={this.getMidi}>Get MIDI</button>
                                            <form action={'http://localhost:5000/api/midi/' + this.props.query} method="GET" id="midi-form">
                                                <input type="text" value="2014-09-01" name="start"/>
                                                <input type="text" value="2014-11-01" name="end"/>
                                            </form>
                                        </div>
                                        <br/>
                                        <div className="text-center">
                                            <small>Transform this stock's historical data into MIDI.</small>
                                        </div>
                                    </div>
                                }
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

