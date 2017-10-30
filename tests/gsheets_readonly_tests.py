import unittest
from gsheets_readonly import gsheets_readonly

class GsheetsReadonlyTests(unittest.TestCase):

    def test_get_gSheet(self):
        gsheet_id = '17qWseEvbuwUmgIpubFL2WIHvyMtYX0I9CpqThmyrlNA' # sheet used for testing
        gid = '192128846'
        reader = gsheets_readonly.get_gSheet(gsheet_id)
        self.assertTrue(str(type(reader)), '_csv.reader')

        reader = gsheets_readonly.get_gSheet(gsheet_id, gid)
        self.assertTrue(str(type(reader)), '_csv.reader')

    def test_get_headers(self):
        gsheet_id = '17qWseEvbuwUmgIpubFL2WIHvyMtYX0I9CpqThmyrlNA' # sheet used for testing
        gid = '192128846'
        header_sheet1 = ['date','name','employer','description_in_kind','prior_total','amount','in_kind', 'total', 'ytd']
        header_sheet2 = ['date','vendor','street1','city','state','zip','purpose','amount']

        reader = gsheets_readonly.get_gSheet(gsheet_id)
        check_sheet_headers(self, reader, header_sheet1)

        reader = gsheets_readonly.get_gSheet(gsheet_id, gid)
        check_sheet_headers(self, reader, header_sheet2)


    def test_get_row_data(self):
        gsheet_id = '17qWseEvbuwUmgIpubFL2WIHvyMtYX0I9CpqThmyrlNA' # sheet used for testing
        gid = '192128846'
        data_sheet1 = [
            {'data': ['7/25/17', 'Jane Doe', 'abc 123', '', '', '$250.00', '', '$250.00', '$250.00'], 'empty_row': False},
            {'data': [], 'empty_row': True},
            {'data': ['7/1/17', 'John Doe', 'hogwarts', '', '', '$1,000.00', '', '$1,000.00', '$1,000.00'], 'empty_row': False}
        ]
        data_sheet2 = [
            {'data': ['05/19/2017','123 abc','987 1st street','Minneapolis','MN','55406','testing','$100.00'], 'empty_row': False},
        ]

        reader1 = gsheets_readonly.get_gSheet(gsheet_id)
        check_sheet_data(self, reader1, data_sheet1)

        reader2 = gsheets_readonly.get_gSheet(gsheet_id, gid)
        check_sheet_data(self, reader2, data_sheet2)

def check_sheet_headers(self, reader, data):
    headers = next(reader) # get first row
    self.assertEqual(headers, data)

def check_sheet_data(self, reader, data):
    counter = 0
    headers = next(reader) # get first row
    for row in reader:
        row_results = gsheets_readonly.get_row_data(row, headers)
        self.assertEqual(row_results['empty_row'], data[counter]['empty_row'])
        if not row_results['empty_row']:
            row_data = row_results['data']
            check_data = data[counter]['data']
            for idx, val in enumerate(headers):
                self.assertEqual(row_data[val], check_data[idx])
        counter += 1

# docker run -it --rm python/gsheets python3 -m unittest discover -s tests -p "*_tests.py"

