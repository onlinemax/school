# Data collected from
# https://climate.weather.gc.ca/climate_normals/index_e.html
#
# Monthly average temperature data for 13 locations across Canada.
#
# Each sublist contains the following information:
# ['LOCATION NAME', 'PROVINCE OR TERRITORY', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
#
avgtemp = [
    ['EDMONTON (AIRPORT)', 'AB', -12.3, -10.4, -5.3, 3.5, 10.1, 14.1, 16.2, 15.1, 10.3, 3.4, -5.2, -11.0],
    ['VICTORIA (AIRPORT)', 'BC', 4.6, 5.0, 6.8, 9.1, 12.6, 15.2, 17.2, 17.1, 14.5, 10.2, 6.5, 4.4],
    ['WINNIPEG RICHARDSON (AIRPORT)', 'MB', -16.3, -14.1, -6.1, 3.8, 11.1, 17.1, 19.5, 18.7, 13.3, 5.1, -4.4, -12.7],
    ['MONCTON', 'NB', -8.4, -7.6, -2.6, 3.6, 10.0, 15.3, 19.3, 18.7, 14.2, 8.1, 2.1, -4.4],
    ["ST. JOHN'S (AIRPORT)", 'NL', -4.2, -4.7, -2.2, 1.8, 6.3, 10.8, 16.0, 16.5, 12.8, 7.8, 3.4, -1.0],
    ['HALIFAX STANFIELD (AIRPORT)', 'NS', -5.7, -5.2, -0.9, 4.5, 10.1, 15.2, 19.2, 19.2, 15.2, 9.2, 3.8, -1.9],
    ['YELLOWKNIFE (AIRPORT)', 'NT', -25.5, -22.7, -16.6, -5.5, 5.3, 13.8, 17.1, 14.5, 7.6, -1.0, -12.6, -21.8],
    ['IQALUIT', 'NU', -26.0, -27.0, -22.4, -13.5, -3.2, 3.9, 8.1, 7.5, 2.9, -3.2, -11.1, -18.9],
    ['TORONTO PEARSON (AIRPORT)', 'ON', -5.0, -4.4, 0.6, 7.0, 13.7, 19.2, 22.1, 21.1, 16.9, 10.0, 4.1, -1.6],
    ['CHARLOTTETOWN (AIRPORT)', 'PE', -7.3, -7.3, -2.6, 3.0, 9.1, 14.6, 19.0, 18.8, 14.6, 8.6, 3.2, -2.7],
    ['MONTREAL TRUDEAU (AIRPORT)', 'QC', -9.2, -8.0, -2.0, 6.2, 13.9, 19.0, 21.7, 20.6, 16.0, 8.9, 2.3, -5.0],
    ['SASKATOON DIEFENBAKER (AIRPORT)', 'SK', -15.4, -13.4, -6.1, 3.9, 10.9, 15.6, 18.3, 17.4, 11.9, 3.7, -5.6, -13.0],
    ['IVVAVIK NAT. PARK', 'YT', -24.1, -23.2, -21.8, -11.0, 1.0, 10.2, 12.6, 8.9, 2.8, -9.2, -18.8, -22.9],
]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
          "Nov", "Dec"]

# Add your code below this line.
def avg(list):
    accum = 0
    for item in list:
        accum += item
    return accum / len(list)
def standard_deviation(list):
    mean = avg(list)
    accum = 0
    for item in list:
        accum += (item - mean)**2
    accum /= len(list)
    return accum**(1/2)
for temp in avgtemp:
    print(temp[1], round(avg(temp[2:]), 2), round(standard_deviation(temp[2:]), 2))
for i in range(12):
    print(months[i], round(avg([x[i + 2] for x in avgtemp]), 2))

