from classes.Scraper import FlightScraper
from utils.save_flight_information import save_flight_information
from utils.get_flight_search_inputs import get_flight_search_inputs

if __name__ == "__main__":
    try:
        # Set up the base URL
        url_base = 'https://www.latamairlines.com/co/es/ofertas-vuelos?' 

        urls, departure_dates, return_dates, origin, destination = get_flight_search_inputs(url_base)

        # Iterate over the generated URLs and scrape flight information
        for index,url in enumerate(urls):
            
            # Create an instance of the FlightScraper
            scraper = FlightScraper()
            
            # Scrape flight information from the LATAM website
            df = scraper.scrape_latam(url)
            
            # Format the date strings for file naming
            departure_date_formatted = departure_dates[index].replace('/', '-')
            return_date_formatted = return_dates[index].replace('/', '-')
            airport_codes = f"{origin.upper()}_{destination.upper()}"

            save_flight_information(df,departure_date_formatted,return_date_formatted,airport_codes)
        
        print("Flight search completed.")
        scraper.driver.quit()
    
    except Exception as e:
        print('An error occurred:', str(e))
