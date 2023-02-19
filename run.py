import requests
import xmltodict


def main():
    _version = 4
    _id = "12345"
    _number = 12345
    _type_xml = 12
    _history_not_contain = 0
    url = \
        f'https://api.houjin-bangou.nta.go.jp/{_version}/num' \
        f'?id={_id}' \
        f'&number={_number}' \
        f'&type={_type_xml}&history={_history_not_contain}'
    res = requests.get(url)

    if res.status_code == 200:
        res_dict = xmltodict.parse(res.text)
        print(res_dict)


if __name__ == "__main__":
    main()
