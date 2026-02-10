import requests

class ParliamentAPI:
    BASE_URL = 'https://www.ourcommons.ca/en/parliament-api/'  # Example API URL

    def get_members(self):
        response = requests.get(f'{self.BASE_URL}members')
        return response.json() if response.status_code == 200 else None

    def get_member_by_id(self, member_id):
        response = requests.get(f'{self.BASE_URL}members/{member_id}')
        return response.json() if response.status_code == 200 else None

    def search_bill(self, bill_number):
        response = requests.get(f'{self.BASE_URL}bills/{bill_number}')
        return response.json() if response.status_code == 200 else None

# Example usage:
# api = ParliamentAPI()
# members = api.get_members()