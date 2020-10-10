class track:
    def clock(self, last_box, base_number, base_index):

        while (base_number-last_box)>last_box :
            base_number=base_number-last_box


        distance=base_number-last_box
        return base_index-(last_box-distance)

    def anti_clock(self,last_box,base_number,base_index):

        while (base_number - last_box) > last_box:
            base_number = base_number - last_box

        distance = base_number - last_box
        return base_index-distance
