# Latam-Airlines-Flights-Scraper

This repository contains a flight scraper tool that retrieves flight information from the LATAM Airlines website. It allows users to search for flights based on specific departure and return dates, as well as origin and destination airports.

---

## Set Up and Usage

1. Clone the repository:

   ```
   git clone git@github.com:SantiagoAlarconDS/Latam-Airlines-Flights-Scraper.git
   cd Latam-Airlines-Flights-Scraper
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```
   python main.py
   ```

4. Follow the prompts to enter the departure and return dates, as well as the origin and destination airports. The tool will generate the appropriate URLs and scrape flight information from the LATAM Airlines website.

    For instance:
   - Enter the departure date (DD/MM/YYYY): 05/10/2023
   - Enter the return date (DD/MM/YYYY): 08/10/2023
   - Enter the origin airport code (IATA airport code): MIA
   - Enter the destination airport code (IATA airport code): BOG


5. If you want to search for different dates, enter "yes" when prompted. Repeat step 4 for each search.

6. The flight information will be saved in an Excel file in the `Flights` directory. Each search will create a separate directory based on the departure and return dates, along with the airport codes.

   - File path: `Flights/[departure_date]*[return_date]_[airport_codes]/flights_[departure_date]_[return_date]_[airport_codes].xlsx`

7. The flight search is completed once all desired searches are performed.


---
# Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the project's GitHub repository.

---
# Disclaimer
This script is intended for educational purposes only. Use it responsibly and adhere to the terms and conditions of the Latam Airlines website. The scraping process should not be abused or used for any malicious activities.

---
## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and enhance the flight scraper tool as per your requirements.

For any questions or issues, please contact [lsascol01@gmail.com](mailto:lsascol01@gmail.com).

