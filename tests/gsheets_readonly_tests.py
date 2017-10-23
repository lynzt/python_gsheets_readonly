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
        data = [
            ['7/25/17', 'Jane Doe', 'abc 123', '', '', '$250.00', '', '$250.00', '$250.00'],
            ['7/1/17', 'John Doe', 'hogwarts', '', '', '$1,000.00', '', '$1,000.00', '$1,000.00']
        ]
        counter = 0
        for row in reader:
            if counter == 0:
                continue
            row_data = g_sheets.get_row_data(row, headers)
            self.assertEqual(row_data, data[counter])
            self.assertEqual(row_data[counter]['date'], data[counter][0])
            self.assertEqual(row_data[counter]['name'], data[counter][1])
            self.assertEqual(row_data[counter]['employer'], data[counter][2])
            self.assertEqual(row_data[counter]['Description of In- Kind Donation'], data[counter][3])
            self.assertEqual(row_data[counter]['Previous Total for the Year'], data[counter][4])
            self.assertEqual(row_data[counter]['$ Received This Period'], data[counter][5])
            self.assertEqual(row_data[counter]['value in kind'], data[counter][6])
            self.assertEqual(row_data[counter]['Total from Source'], data[counter][7])
            self.assertEqual(row_data[counter]['Year To Date'], data[counter][8])
            counter += 1

# docker run -it --rm python/gsheets python3 -m unittest discover -s tests -p "*_tests.py"
