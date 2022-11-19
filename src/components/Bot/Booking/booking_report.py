import re
from selenium.webdriver.remote.webelement import WebElement


class BookingReport():
    def __init__(self, boxes_section_elts: WebElement):
        self.boxes_section_elts = boxes_section_elts
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_elts.find_elements_by_class_name('d20f4628d0')

    def pull_deals_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element_by_class_name(
                'a23c043802').get_attribute('innerText').strip()
            price = deal_box.find_element_by_class_name(
                'bd73d13072').get_attribute('innerText').strip()
            score = deal_box.find_element_by_class_name(
                'd10a6220b4').get_attribute('innerText').strip()
            collection.append(
                [hotel_name, price, score]
            )
        return collection
