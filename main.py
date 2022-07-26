import time

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

link = 'https://rozetka.com.ua/ua/'

filter_params = {
    'brands': ['OnePlus', 'Samsung', 'Xiaomi', ],
    'RAM': [' 8 ГБ ', ' 12 ГБ ', ],
    'memory': [' 128 ГБ ', ' 256 ГБ ', ],
    'display': ['6" - 6.49"', '6.5" та більше', ],
    'CPU': ['Qualcomm Snapdragon', ],
    'price_range': ['10000-20000'],
}
sort_by = 'Новинки'
count_to_compare = 5

display_filter = {
    'До 4"': 'До 4',
    '4.1" - 4.5"': '4.1',
    '4.6" - 5"': '4.6',
    '5.1" - 5.5"': '5.1',
    '5.55" - 6"': '5.55',
    '6" - 6.49"': '6.49',
    '6.5" та більше': '6.5',
}

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
try:
    driver.get(link)
    logger.info(f'Get link - {link}')
    link = driver.find_element(
        By.XPATH,
        '//a[@class="menu-categories__link" and contains(text(), "Смартфони, ТВ і електроніка")]'
    )
    time.sleep(2)
    link.click()
    logger.info(f'Click on category "Смартфони, ТВ і електроніка"')

    time.sleep(2)
    mobile = driver.find_element(by=By.XPATH, value='//ul[@class="portal-grid portal-grid_type_1_4"]//li'
                                                    '//a[contains(text(), "Мобільні телефони")]')

    mobile.click()
    logger.info(f'Click on category "Мобільні телефони"')

    time.sleep(2)

    for key in filter_params:
        for item in filter_params[key]:
            if key in ['RAM', 'memory']:
                driver.find_element(By.XPATH,
                                    f'//a[@class="tile-filter__link" and contains(text(), "{item}")]').click()
            elif key == 'price_range':
                _min, _max = filter_params[key][0].split('-')
                min_price = driver.find_element(By.XPATH, '//form//div[@class="slider-filter__inner"]//input[1]')

                max_price = driver.find_element(By.XPATH, '//form//div[@class="slider-filter__inner"]//input[2]')
                min_price.clear()
                min_price.send_keys(_min)

                max_price.clear()
                max_price.send_keys(_max)
                driver.find_element(By.XPATH, '//form//div[@class="slider-filter__inner"]//button').click()
            elif key == 'display':
                driver.find_element(By.XPATH,
                                    f'//a[@class="checkbox-filter__link" and contains(text(), {display_filter[item]})]').click()
            else:
                driver.find_element(By.XPATH,
                                    f'//a[@class="checkbox-filter__link" and contains(text(), "{item}")]').click()
            time.sleep(3)
    logger.info(f'Filtered by params')

    time.sleep(2)
    sort_select = Select(driver.find_element(by=By.XPATH, value='//div[@class="catalog-settings"]//select'))
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_UP)
    sort_select.select_by_visible_text(sort_by)
    logger.info(f'Sort by {sort_by}')

    result_products_list = driver.find_element(
        by=By.XPATH,
        value='//section[@class="content content_type_catalog"]//ul'
    ).find_elements(by=By.TAG_NAME, value='app-compare-button')

    for i in range(count_to_compare):
        try:
            result_products_list[i].click()
        except IndexError:
            break
    logger.info(f'Add to compare {count_to_compare} products')

    compare_list = driver.find_element(by=By.XPATH, value='//ul[@class="header-actions"]//li[5]//button')
    compare_list.click()

    logger.info(f'Click on compare list')

    time.sleep(2)
    compare_page = driver.find_element(by=By.XPATH, value='//div[@class="modal__content"]//ul//li//a')
    compare_page.click()
    logger.info(f'Get compare page')

    time.sleep(2)
    only_differences = driver.find_element(by=By.XPATH, value='//section//div[@class="comparison-settings"]//button')
    only_differences.click()

    logger.info(f'Click on "Тільки відмінності"')

    time.sleep(2)
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
