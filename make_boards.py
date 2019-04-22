from bs4 import BeautifulSoup
import requests
import csv


def generate():
    """
    Makes post requests to a website to generate 16 by 16 sudoku boards. Uses BeautifulSoup to parse the HTML
    and then writes to a CSV.
    """
    with open('16x16.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        # Can change this for more puzzles, each post request makes 5 puzzles
        for i in range(10):
            # An array of arrays that are 256 elements of a 16 by 16 sudoku
            big_puzzles = []
            
            # niv 1 is easy, niv 2 is 'confirmed'
            form = {'niv': 1}
            url = "https://www.sudoku-puzzles-online.com/cgi-bin/hexadoku/print-5-grid-hexadoku.cgi"
            r = requests.post(url, data=form)
            html = r.text

            soup = BeautifulSoup(html, 'lxml')  # Parse the HTML as a string

            # Find all the tables with the class of grid since these are the sudoku tables
            tables = soup.find_all('table', class_="grid")

            # For every sudoku on the page
            for table in tables:
                new_table = []
                rows = table.find_all('tr')

                # Iterate through all rows
                for k in rows:
                    # Iterate through each entry in the row
                    for j in k.find_all('td'):
                        number = 0
                        if j.contents[0] == 'A':
                            number = 11
                        elif j.contents[0] == 'B':
                            number = 12
                        elif j.contents[0] == 'C':    
                            number = 13
                        elif j.contents[0] == 'D':
                            number = 14
                        elif j.contents[0] == 'E':
                            number = 15
                        elif j.contents[0] == 'F':
                            number = 16
                        elif j.contents[0] == ' ':
                            number = 0
                        elif j.contents[0] == 'Â\xa0':
                            number = 0
                        else:
                            number = int(j.contents[0])+1    
                        new_table.append(number)

                big_puzzles.append(new_table)

            for puzzle in big_puzzles:
                writer.writerow(puzzle[i] for i in range(len(puzzle)))
