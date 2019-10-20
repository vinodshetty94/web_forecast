import argparse
from .utils import *
from datetime import datetime


def main():
	# create argument parser object 
	parser = argparse.ArgumentParser(description = "Weather Reporter") 
  
	parser.add_argument("-q", "--query", type = str, nargs = 1, 
	                    metavar = "location", default = None, help = "Location") 

	parser.add_argument("-d", "--date", type = datetime , nargs = 1,
	                    metavar = "date", default = datetime.now(), help = "Enter date to find weather")

    parser.add_argument("-t", "--type", type=str, nargs=1,
						metavar="type", default="tenday", help="type available [hourbyhour, 5day, tenday,  monthly, today, weekend")
	# parse the arguments from standard input 
	args = parser.parse_args()

	weather_data = get_weather(args.query, args.date, args.type)
	print_weather_details(weather_data)


if __name__ == "__main__":
	main()