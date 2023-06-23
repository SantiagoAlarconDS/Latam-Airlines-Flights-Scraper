import os


def save_flight_information(df, departure_date_formatted, return_date_formatted, airport_codes) -> None:
    # Create directories for saving the files if they don't exist
    if not os.path.isdir('./Flights'):
        os.mkdir('./Flights')
    if not os.path.isdir(f'./Flights/{departure_date_formatted}*{return_date_formatted}_{airport_codes}'):
        os.mkdir(
            f'./Flights/{departure_date_formatted}*{return_date_formatted}_{airport_codes}')

    # Save the flight information to an Excel file
    df.to_excel(f'./Flights/{departure_date_formatted}*{return_date_formatted}_{airport_codes}/flights_{departure_date_formatted}_{return_date_formatted}_{airport_codes}.xlsx', index=False)
    print(
        f"flights_{departure_date_formatted}_{return_date_formatted}_{airport_codes}.xlsx saved.")
    print("\n")
    print("\n")
