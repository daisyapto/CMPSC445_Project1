import pandas as pd
import xarray as xr

#Debugging
# Show all rows
pd.set_option('display.max_rows', None)

# Debugging
# Show all columns
pd.set_option('display.max_columns', None)

def dataCollection():
    file1 = "/Users/daisyaptovska/Desktop/psu/S26/cmpsc445/project1/data/ch4_annmean_gl.csv"
    file2 = "/Users/daisyaptovska/Desktop/psu/S26/cmpsc445/project1/data/co2_annmean_mlo.csv"
    file3 = "/Users/daisyaptovska/Desktop/psu/S26/cmpsc445/project1/data/n2o_annmean_gl.csv"
    colIDs1 = ["(CH4)", "(CO2)", "(N2O)"] # file 1, 2, and 3 attributes IDs for the main data table
    fileSet1 = [file1, file2, file3]

    file4 = "/Users/daisyaptovska/Desktop/psu/S26/cmpsc445/project1/data/GLB.Ts+dSST.csv"
    file5 = "/Users/daisyaptovska/Desktop/psu/S26/cmpsc445/project1/data/tsi_v03r00_yearly_s1610_e2025_c20260305.nc"
    colIDs2 = ["(Land-Ocean Global Means)", "(Solar Irradiance)"] # file 4 and 5 attributes IDs for the main data table

    file6 = "/Users/daisyaptovska/Desktop/psu/S26/cmpsc445/project1/data/co2-long-term-concentration/co2-long-term-concentration.csv"
    colID3 = "(Long-term CO2 Concentration)"

    frames = []

    try:
        count1 = 0
        for file in fileSet1:
            with open(file, 'r') as f:
                content = [line.rstrip('\n') for line in f]
                content = [item.split(",") for item in content if "#" not in item and item != ""]
            # Debug statement
            # print(content)
            cols = content[0]
            for i in range(len(cols)):
                cols[i] += f" {colIDs1[count1]}"
            cols[0] = 'year'
            frame = pd.DataFrame(content[1:], columns=cols)
            frames.append(frame)
            # Debug statement
            # print(frame)
            count1 += 1

        with open(file4, 'r') as f:
            content = [line.rstrip('\n') for line in f]
            content = [item.split(",") for item in content]
            # Debug statement
            # print(content)
        cols = content[1]
        for i in range(len(cols)):
            cols[i] += f" {colIDs2[0]}"
        cols[0] = 'year'
        frame = pd.DataFrame(content[2:], columns=cols)
        frames.append(frame)
        # Debug statement
        # print(frame)

        file5data = xr.open_dataset(file5)
        # print(file5data.attrs)
        # Debug statements
        # print(file5data)
        file5data = file5data.to_dataframe()
        # Debug statements
        # print(file5data[:20])
        # print(file5data.shape)
        # print(file5data[0:2])
        #print(file5data.head)
        """
        Original file reading for solar irradiation when thought I was going to use a .csv file instead of .nc file
        content = [line.rstrip('\n') for line in file5data]
        content = [item.split(",") for item in content]
        # print(content)
        cols = content[1]
        for i in range(len(cols)):
            cols[i] += f" {colIDs2[0]}"
        cols[0] = 'year'
        frame = pd.DataFrame(content[2:], columns=cols)
        frames.append(frame)
        """
        file5data = file5data.reset_index()
        file5data.drop(columns=['time_bnds', 'bounds'], inplace=True)
        file5data['time'] =  file5data['time'].apply(lambda x: str(x)[:4])
        file5data['time'] = file5data['time'].apply(lambda x: float(x))
        file5data.drop_duplicates(subset=['time'], keep='first', inplace=True)
        file5data = file5data.rename(columns={'time': 'year'})
        # Debug statements
        # file5data = file5data.dropna(subset=['time'])
        # print(type(file5data['time']))
        # print(file5data)
        # print(frame)
        frames.append(file5data)

        with open(file6, 'r') as f:
            content = [line.rstrip('\n') for line in f]
            content = [item.split(",") for item in content]
            # Debug statement
            # print(content)
        cols = content[0]
        # print(cols)
        for i in range(len(cols)):
            cols[i] += f" {colID3}"
        cols[2] = 'year'
        frame = pd.DataFrame(content[1:], columns=cols)
        frames.append(frame)
        # Debug statement
        # print(frame)

    except FileNotFoundError:
        print(f"Error: A file was not found.")

    # Debug statement
    # print(frames)
    return frames

# Testing function
# dataCollection()