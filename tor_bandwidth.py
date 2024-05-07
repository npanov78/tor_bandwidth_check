import logging

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def read_bridges_from_file(filename):
    with open(filename, 'r') as file:
        bridges = file.readlines()
    return [bridge.strip() for bridge in bridges]


def get_advertised_bandwidth(bridge, driver):
    bridge = bridge.split()[2]
    url = f"https://metrics.torproject.org/rs.html#search/{bridge}"

    try:
        driver.get(url)
        time.sleep(1.5)
        data = driver.page_source

        bandwidth_match = float(re.search(r'<dd>([\d.]+)\s*([MGTP])?iB/s</dd>',
                                    data).group(1))

        if bandwidth_match is None:
            logging.error(f'Bridge {bridge}: error getting bandwith')
            return None
        return bandwidth_match
    except Exception as e:
        return None


def main():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    bridge_file = 'bridges.txt'  # Change this to your bridge file name
    bridge_list = read_bridges_from_file(bridge_file)

    bandwidth_list = [(bridge, bandwidth) for bridge in bridge_list if (bandwidth := get_advertised_bandwidth(bridge, driver)) is not None]

    sorted_bandwidth = sorted(bandwidth_list, key=lambda x: x[1], reverse=True)

    top_3_bridges = sorted_bandwidth[:3]

    with open('best_bridges.txt', 'w') as file:
        for bridge, bandwidth in top_3_bridges:
            logging.info(f'Bridge {bridge}: bandwidth - {bandwidth} MiB/s')
            file.write(f'Bridge {bridge}\n')
    driver.quit()


if __name__ == "__main__":
    logging.info('start')
    main()

