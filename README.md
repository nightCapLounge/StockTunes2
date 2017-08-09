# StockTunes

This is a small, fun project to explore using a REST API and Flask to create music out of stock market data.  The current project is just an end to end proof of concept with no real substance.

Theoretically, with a refined enough model that deeply expresses the trends of a stock, a person should be able to make intuitive and accurate market predictions simply by listening to and learning what a stock sounds like when it exhibits certain behavior.  Humans are astonishingly good at pattern recognition, especially when it comes to hearing.  StockTunes is an interesting alternative to gazing at charts.  


## The API

The REST API is built with the OpenAPI 3.0 standard in mind.  

There are only GET requests present in the API, as stock market data is immutable.  POST requests and DELETE requests will emerge when storage of MIDI files or users are built into the program.  PUT requests are pedantic.


### Resilience

The API is built to be resilient if the user wants it to be.  The data collection mechanisms behind the actual API can be categorized into aggregate and basic operations.  Basic operations query a single source of data, and aggregate operations query many.  That being said, all aggregate operations allow the user to send a "resilient" flag with the requests.  This tells the API to return as much data as possible without throwing an error, even if parts of the aggregation fail.  

An example of this can be found when getting the data dump for a stock: e.g. "/api/stock/GOOGL" returns many data points about a stock that are separately retrieved.  Using the parameter "resilient" as True will tell the API to get as much data in that query as possible -- for instance, return the average daily volume even if everything else is unavailable.  


### API Zones

There are two primary zones of the API -- the stock zone and the midi zone.  These are created as namespaces in Flask.  The stock zone queries the Yahoo Finance API for stock data.  The midi zone performs midi operations on historical stock data.  

#### Stocks

A user can get a data dump of a stock by submitting a GET request in the following form: "/api/stock/<ticker:string>".

Specific data can be retrieved about the stock with a GET request in the following form: "/api/stock/<ticker:string>/<metric:string>".


#### MIDI

A midi file can be produced with a GET request in the following format "/api/midi/<ticker:string>?start=%Y-%m-%d&end=%y-%m-%d".
The start parameter is the beginning of the historical frame, and the end parameter is the end of the historical frame.  


## The Model

At the moment, StockTunes uses the simplest possible model for turning data into music.  Given a stream of stock data, a field from the stream is selected (e.g. Adjusted Close), and if the field goes up in a discrete timestep, a major chord from a given key is randomly selected, and if the data trends downward, a minor chord is randomly selected.  There is one chord per time step.  The tones from the chord that are played are then randomly selected and written to MIDI.  


## React Front-end

There is a bare-bones React front end to accompany the application.  It allows the user to choose a stock and a time range, and produce MIDI from that data.  There is currently minimal error handling in this section of the application.  



