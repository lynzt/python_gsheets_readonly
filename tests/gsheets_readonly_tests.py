import unittest
from gsheets_readonly import gsheets_readonly

class GsheetsReadonlyTests(unittest.TestCase):

    def test_get_gSheet(self):
        gsheet_id = '17qWseEvbuwUmgIpubFL2WIHvyMtYX0I9CpqThmyrlNA' # sheet used for testing
        reader = gsheets_readonly.get_gSheet(gsheet_id)
        self.assertTrue(str(type(reader)), '_csv.reader')

    def test_get_headers(self):
        gsheet_id = '17qWseEvbuwUmgIpubFL2WIHvyMtYX0I9CpqThmyrlNA' # sheet used for testing
        reader = gsheets_readonly.get_gSheet(gsheet_id)
        headers = next(reader) # get first row
        self.assertEqual(headers,['date', 'name', 'employer', 'Description of In- Kind Donation', 'Previous Total for the Year',
        '$ Received This Period', 'value in kind', 'Total from Source', 'Year To Date'])

    def test_get_row_data(self):
        gsheet_id = '17qWseEvbuwUmgIpubFL2WIHvyMtYX0I9CpqThmyrlNA' # sheet used for testing
        reader = gsheets_readonly.get_gSheet(gsheet_id)
        headers = next(reader) # get first row
        check_results = [
            {'data': ['7/25/17', 'Jane Doe', 'abc 123', '', '', '$250.00', '', '$250.00', '$250.00'], 'empty_row': False},
            {'data': [], 'empty_row': True},
            {'data': ['7/1/17', 'John Doe', 'hogwarts', '', '', '$1,000.00', '', '$1,000.00', '$1,000.00'], 'empty_row': False}
        ]
        counter = 0
        for row in reader:
            row_results = gsheets_readonly.get_row_data(row, headers)
            self.assertEqual(row_results['empty_row'], check_results[counter]['empty_row'])
            if not row_results['empty_row']:
                row_data = row_results['data']
                check_data = check_results[counter]['data']
                self.assertEqual(row_data['date'], check_data[0])
                self.assertEqual(row_data['name'], check_data[1])
                self.assertEqual(row_data['employer'], check_data[2])
                self.assertEqual(row_data['Description of In- Kind Donation'], check_data[3])
                self.assertEqual(row_data['Previous Total for the Year'], check_data[4])
                self.assertEqual(row_data['$ Received This Period'], check_data[5])
                self.assertEqual(row_data['value in kind'], check_data[6])
                self.assertEqual(row_data['Total from Source'], check_data[7])
                self.assertEqual(row_data['Year To Date'], check_data[8])
            counter += 1

# docker run -it --rm python/gsheets python3 -m unittest discover -s tests -p "*_tests.py"
