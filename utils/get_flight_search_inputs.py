from utils.build_url import build_url

def get_flight_search_inputs(url_base: str):
    urls = []
    departure_dates = []
    return_dates = []

    # Prompt the user for departure and return dates
    departure_date = input("Enter the departure date (DD/MM/YYYY): ")
    departure_dates.append(departure_date)
    return_date = input("Enter the return date (DD/MM/YYYY): ")
    return_dates.append(return_date)

    # Prompt the user for the origin and destination airports
    origin = input("Enter the origin airport code: ")
    destination = input("Enter the destination airport code: ")

    # Build the URL using the scraper's build_url method
    url = build_url(url_base, departure_date, return_date, origin, destination)
    urls.append(url)  # Append the generated URL to the list

    # Prompt the user if they want to search for a different date
    search_different_flights = input(
        "Do you want to search for a different date? (yes/no): ")

    while search_different_flights.lower() == 'yes':
        # If yes, prompt for new departure and return dates
        departure_date = input("Enter the departure date (DD/MM/YYYY): ")
        return_date = input("Enter the return date (DD/MM/YYYY): ")
        departure_dates.append(departure_date)
        return_dates.append(return_date)

        # Build the URL using the scraper's build_url method
        url = build_url(url_base, departure_date,
                        return_date, origin, destination)
        urls.append(url)  # Append the generated URL to the list

        # Prompt the user again if they want to search for a different date
        search_different_flights = input(
            "Do you want to search for a different date? (yes/no): ")

    return urls, departure_dates, return_dates, origin, destination
