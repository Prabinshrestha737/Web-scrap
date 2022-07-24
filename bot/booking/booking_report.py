# This file is going to include method that will parse the specific data we need from each one of the deal boxes.




class BookingReport:
    def __init__(self, boxes_section_element):
        self.boxes_selection_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()
    
    
    def pull_deal_boxes(self):
        self.boxes_selection_element.find_element_by_class_name(
            ''
        )