from pprint import pprint
import tools


def main():
   sitenames = tools.get_sitenames('aqi.xlsx')
   print(sitenames)


if __name__ == '__main__':
    main()