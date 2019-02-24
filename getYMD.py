# import necessary modules
import pandas as pd

# works for the following condition: the year part is 2 digits, from 1951 to 2050
def getyear(file_name, column_name, start, end):

    # upload the file, read the targeted column as string, fill the empty with 'missing'
    df = pd.read_csv(file_name, header=0, skip_blank_lines=False, converters={column_name: lambda x: str(x)})

    df.replace('', 'missing', inplace=True)

    # in order to pick the last digit of the original data, add '_' to the tail
    date = df[column_name] + '_'

    # create a list to store the year which is extracted
    year = [None] * df.shape[0]

    
    for i in range(len(year)):
        if date[i] == 'missing_':
            year[i] = 'missing'

        elif int(date[i][start - 1: end]) > 50:
            year[i] = '19' + date[i][start - 1: end]

        else:
            year[i] = '20' + date[i][start - 1: end]

        df['year'] = year

    return df


def getmonth(file_name, column_name, start, end):

    df = pd.read_csv(file_name, header=0, skip_blank_lines=False, converters={column_name: lambda x: str(x)})

    df.replace('', 'missing', inplace=True)

    date = df[column_name] + '_'

    month = [None] * df.shape[0]

    for i in range(len(month)):
        if date[i] == 'missing_':
            month[i] = 'missing'

        else:
            month[i] = date[i][start - 1: end]

        df['month'] = month

    return df


def getday(file_name, column_name, start, end):
    df = pd.read_csv(file_name, header=0, skip_blank_lines=False, converters={column_name: lambda x: str(x)})

    df.replace('', 'missing', inplace=True)

    date = df[column_name] + '_'

    day = [None] * df.shape[0]

    for i in range(len(day)):
        if date[i] == 'missing_':
            day[i] = 'missing'

        else:
            day[i] = date[i][start - 1: end]

        df['day'] = day

    return df