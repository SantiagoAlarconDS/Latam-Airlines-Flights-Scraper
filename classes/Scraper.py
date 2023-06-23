import os
import pandas as pd
from time import sleep
from typing import List,Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class FlightScraper:
    def __init__(self):
        """
        Initialize the FlightScraper.

        Sets up the Chrome WebDriver with incognito mode.

        """
        # Set up Chrome driver options
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')

        # Initialize Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    def get_prices(self, flight, id: int) -> List[Dict]:
        """
        Get the prices of available fares for a flight.

        Args:
            flight: The flight element containing the fares.
            id: The ID of the flight.

        Returns:
            A list of dictionaries, where each dictionary represents a fare and contains the following keys:
            - 'type': The type of the fare.
            - 'currency': The currency of the fare.
            - 'value': The value of the fare.
            - 'id': The ID of the flight.

        """
        # Find all the fare elements
        fares = flight.find_elements(
            by=By.XPATH, value='.//ol[@aria-label="Tarifas disponibles."]/li')
        prices = []
        for fare in fares:
            # Get the fare name
            name = fare.find_element(
                by=By.XPATH, value='.//div[@class="columnBrandstyle__BrandHeader-sc__sc-1e0tr9m-4 fCLxWc"]/span').text
            
            # Get the currency name
            currency = fare.find_element(
                by=By.XPATH, value='.//span[@class="display-currencystyle__CurrencyAmount-sc__sc-19mlo29-2 fMjBKP currency"]').text
            
            # Get the fare value
            value = fare.find_element(
                by=By.XPATH, value='.//span[@class="display-currencystyle__CurrencyAmount-sc__sc-19mlo29-2 fMjBKP"]').text
            
            # Create a dictionary with fare details and flight ID
            data_dict = {
                'type': name,
                'currency': currency,
                'value': value,
                'id': id
            }

            prices.append(data_dict)
        
        return prices

    def get_stopover_data(self, flight, id:int) -> List[Dict]:
        """
            Get stopover information for a flight.

            Args:
                flight: The flight element containing the stopover data.
                id: The ID of the flight.

            Returns:
                A list of dictionaries, where each dictionary represents a stopover and contains the following keys:
                - 'origin': The origin of the stopover.
                - 'dep_time': The departure time of the stopover.
                - 'destination': The destination of the stopover.
                - 'arr_time': The arrival time of the stopover.
                - 'flight_duration': The duration of the stopover flight.
                - 'flight_number': The flight number of the stopover.
                - 'aircraft_model': The model of the aircraft for the stopover flight.
                - 'stopover_duration': The duration of the stopover.
                - 'id': The ID of the flight.

        """         
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, './/i[@class="sc-ESujJ ezFxxY airlineImagestyle__Styled-sc__sc-1cylcv8-0 dDzMhn"]')))
        segments = self.driver.find_elements(
            by=By.XPATH, value='.//section[@class="itinerarystyle__Section-sc__sc-1n97ky6-1 ddwMQK"]')
        stopover_info = []
        n_stopovers = len(segments) - 1
        counter = 0

        for segment in segments:
            # Origin
            origin = segment.find_element(
                by=By.XPATH, value='.//div[@class="path-infostyle__Top-sc__sc-xj1cll-2 eZnnpl"]//div[@class="iataCode"]/span').text
            # Departure time
            dep_time = segment.find_element(
                by=By.XPATH, value='.//div[@class="path-infostyle__Top-sc__sc-xj1cll-2 eZnnpl"]//div[@class="iataCode"]/span[@class="time"]').text
            # Destination
            destination = segment.find_element(
                by=By.XPATH, value='.//div[@class="path-infostyle__Bottom-sc__sc-xj1cll-4 jMpZeH"]//div[@class="iataCode"]/span').text
            # Arrival time
            arr_time = segment.find_element(
                by=By.XPATH, value='.//div[@class="path-infostyle__Bottom-sc__sc-xj1cll-4 jMpZeH"]//div[@class="iataCode"]/span[@class="time"]').text
            # Flight duration
            flight_duration = segment.find_element(
                by=By.XPATH, value='.//div[@class="path-infostyle__Middle-sc__sc-xj1cll-3 ksaVIu"]/span[@class="time"]').text
            # Flight number
            flight_number = segment.find_element(
                by=By.XPATH, value='.//div[@class="incoming-outcoming-title"]//div').text
            # Aircraft model
            aircraft_model = segment.find_element(
                by=By.XPATH, value='.//span[@class="airplane-code"]').text

            # Stopovers
            stopovers = self.driver.find_elements(
                by=By.XPATH, value='.//section[@class="itinerarystyle__Section-sc__sc-1n97ky6-1 ddwMLI"]')

            # Stopover duration
            if counter < n_stopovers:
                stopover_duration = stopovers[counter].find_element(
                    by=By.XPATH, value='.//div[@class="connection-infostyle__ConnectionInformation-sc__sc-1qity98-2 bOpeBi"]//span[@class="time"]').text
                counter += 1
            else:
                stopover_duration = ''

            # Create a dictionary to store the data
            data_dict = {'origin': origin,
                         'dep_time': dep_time,
                         'destination': destination,
                         'arr_time': arr_time,
                         'flight_duration': flight_duration,
                         'flight_number': flight_number,
                         'aircraft_model': aircraft_model,
                         'stopover_duration': stopover_duration,
                         'id': id}

            stopover_info.append(data_dict)

        return stopover_info

    def get_times(self, flight, id:int)-> List[Dict]:
        """
        Get the departure time, arrival time, and duration of a flight.

        Args:
            flight: The flight element containing the time information.
            id: The ID of the flight.

        Returns:
            A list containing a dictionary with the following keys:
            - 'departure_time': The departure time of the flight.
            - 'arrival_time': The arrival time of the flight.
            - 'duration': The duration of the flight.
            - 'id': The ID of the flight.

        """
        # Get hours
        hours = flight.find_elements(
            by=By.XPATH, value='.//span[@class="card-flightstyle__TextHourFlight-sc__sc-16r5pdw-18 kKmcWo"]')
        # Departure time
        departure = hours[0].text
        # Arrival time
        arrival = hours[1].text
        # Duration
        duration = flight.find_element(
            by=By.XPATH, value='.//span[@class="card-flightstyle__TextTotalTimeFlight-sc__sc-16r5pdw-20 fuxJTD"]').text

        return [{'departure_time': departure, 'arrival_time': arrival, 'duration': duration, 'id': id}]

    def get_info(self) -> List[Dict]:
        """
        Get flight information for each flight element (prices, times, and stopovers) on the page.

        Returns:
            A list of dictionaries, where each dictionary contains flight information including prices, times, and stopovers.

        """
        
        flights = self.driver.find_elements(
            by=By.XPATH, value='//li[@class="body-flightsstyle__ListItemAvailableFlights-sc__sc-1p74not-5 ixybDA"]')
        print(f'Found {len(flights)} flights.')
        print('Starting scraping...')
        info = []
        i = 0
        for flight in flights:
            # Get general flight times
            times = self.get_times(flight, i)
            # Click the "flight" button to view details of the pop-up
            flight.find_element(
                by=By.XPATH, value='.//a[@data-reference="modal-air-offers"]').click()
            stopovers = self.get_stopover_data(flight, i)
            # Close the details pop-up
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, './/span[@class="MuiButton-label"]/i[@class="sc-fnykZs dXtIeu"]')))
            close_button = self.driver.find_element(
                by=By.XPATH, value='.//span[@class="MuiButton-label"]/i[@class="sc-fnykZs dXtIeu"]').click()
            # Click the flight to view prices
            flight.click()
            prices = self.get_prices(flight, i)

            info.append({'prices': prices, 'times': times,
                        'stopovers': stopovers})
            i += 1
        return info

    def normalize(self, data: List[dict]) -> pd.DataFrame:
        """
        Normalize the data by extracting nested structures and create a Pandas DataFrame.

        Args:
            data: A list of dictionaries containing the data to be normalized.

        Returns:
            A Pandas DataFrame with the normalized data.

        """
        
        # Extract stopovers data and create a DataFrame
        stopovers = pd.json_normalize(data, record_path='stopovers')

        # Extract prices data and create a DataFrame
        prices = pd.json_normalize(data, record_path='prices')

        # Extract times data and create a DataFrame
        times = pd.json_normalize(data, record_path='times')

        # Merge prices, stopovers, and times DataFrames based on 'id'
        df = prices.merge(stopovers, on='id')
        df = df.merge(times, on='id')

        return df

    def scrape_latam(self, urls) -> pd.DataFrame:
        """
        Scrape flight information from LATAM website using the provided URLs.

        Args:
            urls: A list of URLs to scrape.

        Returns:
            A Pandas DataFrame containing the scraped flight information.

        """

    
        delay = 20

        # If it's a single string, convert it to a list
        # Future function
        if type(urls) == str:
             urls = [urls]

        info = []
        for url in urls:
            print('Scraping URL:', url)
            self.driver.get(url)
            try:
                # Wait for the flight list element to be visible
                flight_list = WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(
                    (By.XPATH, '//li[@class="body-flightsstyle__ListItemAvailableFlights-sc__sc-1p74not-5 ixybDA"]')))
                print("Page is ready!")
                
                # Extract flight information
                info = self.get_info()  
            except TimeoutException:
                print("Loading took too much time!")
            except NoSuchElementException:
                print("Element not found")
        
        # Quit the Chrome driver
        self.driver.close()

        # Normalize the extracted flight information
        df = self.normalize(info)

        return df
