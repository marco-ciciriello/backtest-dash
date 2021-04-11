# Streamlit Stock Dashboard

View information about a company, covering the following:

* **Overview** - what it does, and who runs it
* **Fundamentals** - exciting things like price ratios, quarterly reports and dividends
* **Technicals** - TBD
* **News** - the latest company news from IEX Cloud
* **Ownership** - institutional ownership and insider transactions
* **Stocktwits** - what Twitter has to say about the company

# Feature dependencies

Much functionality of this app is built on top of IEX Cloud data. In order to view the Overview and News screens,
a free IEX Cloud is required. To view the Fundamentals and Ownership screens, a paid IEX Cloud plan is required. 
More information can be found at https://iexcloud.io.

# Set up Local Environment

```python
  # Create virtual environment
  python3 -m venv venv

  # Activate environment
  source venv/bin/activate

  # Install dependencies
  pip install -r requirements.txt
```

# Run the Streamlit app

```python
streamlit run app.py

# App launching on port 8051...
```

# Libraries

| Name           | Type   | Description                                                                                                                                                                                                          |
| -------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| redis          | 3.5.3  | The Python interface to the Redis key-value store. |
| requests         | 2.25.1 | Requests is a simple, yet elegant HTTP library. |
| streamlit      | 0.80.0 | Open-source app framework for Machine Learning and Data Science teams. Create beautiful data apps in hours, not weeks. All in pure Python. |
