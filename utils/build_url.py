def build_url(base_url: str, outbound: str, inbound: str, origin: str, destination: str, cabin: str = 'ECONOMY') -> str:
        """
        Build the URL for a flight search.

        Args:
            base_url: The base URL for the flight search.
            outbound: The outbound date in the format 'dd-mm-yyyy'.
            inbound: The inbound date in the format 'dd-mm-yyyy'.
            origin: The origin airport code.
            destination: The destination airport code.
            cabin: The cabin class (default is 'ECONOMY').

        Returns:
            The complete URL for the flight search.

        """
        
        url = f"{base_url}origin={origin}"
        url += f"&outbound={outbound[6:]}-{outbound[3:5]}-{outbound[0:2]}T12%3A00%3A00.000Z"
        url += f"&destination={destination}"
        url += f"&inbound={inbound[6:]}-{inbound[3:5]}-{inbound[0:2]}T12%3A00%3A00.000Z"
        url += f"&adt=1&chd=0&inf=0&trip=RT&cabin={cabin}&redemption=false&sort=RECOMMENDED"
        return url