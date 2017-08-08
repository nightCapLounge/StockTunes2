
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
                                <small>{this.props.query != "" && this.props.stockData.length == 0 ? "Press search to get data" : ""}</small>
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
                                        </div>
                                        <br/>
                                        <div className="text-center">
                                            <small>Transform this stock's historical data into MIDI.</small>
                                        </div>
                                        <br/>
                                        <div className="text-center">
                                            <form action={'http://localhost:5000/api/midi/' + this.props.query} method="GET" id="midi-form">
                                                <div className="form-group row">
                                                    <input class="form-control" type="date" name="start" />
                                                    <span> to </span>
                                                    <input class="form-control" type="date" name="end" />
                                                </div>
                                            </form>
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

