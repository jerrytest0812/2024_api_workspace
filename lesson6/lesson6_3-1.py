from pprint import pprint
import tools


def main():
    data:list[dict] = tools.get_aqi('aqi.xlsx')
    pprint(data)


if __name__ == '__main__':
    main()